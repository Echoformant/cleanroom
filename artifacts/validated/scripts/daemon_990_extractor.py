#!/usr/bin/env python3
"""
990 Extraction Daemon — Ollama-Powered Background Processor

This script runs continuously, processing IRS Form 990 text files one at a time.
Outputs markdown summaries for human review, which can be converted to JSON later.

Usage:
    python daemon_990_extractor.py [--queue-dir DIR] [--output-dir DIR] [--model MODEL]

Requirements:
    - Ollama running locally: ollama serve
    - A small model loaded: ollama pull llama3.2:3b (or similar)
    - 990 text files in queue directory

Design notes:
    - One EIN at a time to keep context fresh
    - Markdown output (easier for small models)
    - Throttled loop with cooldown between files
    - Moves processed files to avoid reprocessing
"""

import os
import sys
import time
import json
import shutil
import argparse
import requests
from pathlib import Path
from datetime import datetime

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_QUEUE_DIR = "_990_queue"
DEFAULT_OUTPUT_DIR = "_990_extracted"
DEFAULT_DONE_DIR = "_990_done"
DEFAULT_MODEL = "llama3.2:latest"
OLLAMA_URL = "http://localhost:11434/api/generate"
COOLDOWN_SECONDS = 1  # Time between processing files
MAX_CONTEXT_CHARS = 8000  # Truncate long files

# ============================================================================
# Extraction Prompt
# ============================================================================

EXTRACTION_PROMPT = """You are extracting key information from an IRS Form 990 filing.

Read the following 990 data and extract these fields into a clean markdown summary:

## Required Fields
- **EIN**: The 9-digit employer identification number
- **Organization Name**: Legal name
- **Tax Year**: Filing year (YYYY)
- **Total Revenue**: From Part I
- **Total Expenses**: From Part I
- **Net Assets**: End of year
- **Program Service Revenue**: If available
- **Contributions/Grants**: Total received
- **Number of Employees**: If stated
- **State**: Where incorporated

## Key People (if listed)
- Officers, Directors, Key Employees with titles

## Programs (Schedule O or Part III)
- Brief description of top 2-3 programs

## Red Flags (if any)
- Missing required sections
- Large unusual transactions
- Governance issues

---
990 DATA:
{content}

---
OUTPUT (Markdown format):
"""

# ============================================================================
# Functions
# ============================================================================

def ensure_dirs(queue_dir, output_dir, done_dir):
    """Create directories if they don't exist."""
    Path(queue_dir).mkdir(parents=True, exist_ok=True)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(done_dir).mkdir(parents=True, exist_ok=True)


def get_pending_files(queue_dir):
    """Get list of unprocessed 990 files."""
    queue = Path(queue_dir)
    extensions = ['.txt', '.xml', '.json', '.csv']
    files = []
    for ext in extensions:
        files.extend(queue.glob(f'*{ext}'))
    return sorted(files)


def read_file_content(filepath, max_chars=MAX_CONTEXT_CHARS):
    """Read and optionally truncate file content."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if len(content) > max_chars:
            content = content[:max_chars] + "\n\n[TRUNCATED - file too long]"
        return content
    except Exception as e:
        return f"[ERROR reading file: {e}]"


def call_ollama(prompt, model=DEFAULT_MODEL):
    """Call Ollama API and return response."""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 1500
                }
            },
            timeout=120
        )
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            return f"[ERROR: Ollama returned {response.status_code}]"
    except requests.exceptions.ConnectionError:
        return "[ERROR: Cannot connect to Ollama. Is 'ollama serve' running?]"
    except Exception as e:
        return f"[ERROR: {e}]"


def process_990_file(filepath, output_dir, model):
    """Process a single 990 file and output markdown."""
    filename = filepath.stem
    content = read_file_content(filepath)
    
    prompt = EXTRACTION_PROMPT.format(content=content)
    
    print(f"  ⏳ Calling Ollama ({model})...")
    result = call_ollama(prompt, model)
    
    # Create output markdown
    output_path = Path(output_dir) / f"{filename}_extracted.md"
    header = f"""# 990 Extraction: {filename}

**Source File:** {filepath.name}  
**Processed:** {datetime.now().isoformat()}  
**Model:** {model}

---

"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(header + result)
    
    return output_path


def move_to_done(filepath, done_dir):
    """Move processed file to done directory."""
    dest = Path(done_dir) / filepath.name
    shutil.move(str(filepath), str(dest))


def get_processed_log(output_dir):
    """Get set of already processed filenames from log."""
    log_path = Path(output_dir) / "_processed.log"
    if log_path.exists():
        return set(log_path.read_text().strip().split('\n'))
    return set()


def log_processed(output_dir, filename):
    """Log a processed filename."""
    log_path = Path(output_dir) / "_processed.log"
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{filename}\n")


def run_daemon(queue_dir, output_dir, done_dir, model, once=False, no_move=False):
    """Main daemon loop."""
    ensure_dirs(queue_dir, output_dir, done_dir)
    
    print("=" * 60)
    print("990 Extraction Daemon")
    print("=" * 60)
    print(f"Queue:  {queue_dir}")
    print(f"Output: {output_dir}")
    print(f"Done:   {done_dir}")
    print(f"Model:  {model}")
    print("=" * 60)
    print()
    
    # Load already processed files (for --no-move mode)
    processed = get_processed_log(output_dir) if no_move else set()
    if no_move and processed:
        print(f"Already processed: {len(processed)} files (will skip)")
    
    iteration = 0
    while True:
        iteration += 1
        files = get_pending_files(queue_dir)
        
        # Filter out already processed if using --no-move
        if no_move:
            files = [f for f in files if f.name not in processed]
        
        if not files:
            if once:
                print("No files to process. Exiting.")
                break
            print(f"[{datetime.now().strftime('%H:%M:%S')}] No files in queue. Sleeping 30s...")
            time.sleep(30)
            continue
        
        file_to_process = files[0]
        print(f"\n[{iteration}] Processing: {file_to_process.name}")
        
        try:
            output_path = process_990_file(file_to_process, output_dir, model)
            print(f"  ✅ Output: {output_path.name}")
            if no_move:
                log_processed(output_dir, file_to_process.name)
                processed.add(file_to_process.name)
                print(f"  📝 Logged as processed")
            else:
                move_to_done(file_to_process, done_dir)
                print(f"  📦 Moved to done folder")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        
        if once:
            if len(files) <= 1:
                break
        
        print(f"  💤 Cooldown {COOLDOWN_SECONDS}s...")
        time.sleep(COOLDOWN_SECONDS)


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="990 Extraction Daemon")
    parser.add_argument("--queue-dir", default=DEFAULT_QUEUE_DIR, help="Input directory")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="Output directory")
    parser.add_argument("--done-dir", default=DEFAULT_DONE_DIR, help="Processed files directory")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Ollama model to use")
    parser.add_argument("--once", action="store_true", help="Process queue once then exit")
    parser.add_argument("--no-move", action="store_true", help="Don't move files, track via log instead")
    
    args = parser.parse_args()
    
    try:
        run_daemon(
            args.queue_dir,
            args.output_dir,
            args.done_dir,
            args.model,
            args.once,
            getattr(args, 'no_move', False)
        )
    except KeyboardInterrupt:
        print("\n\nDaemon stopped by user.")


if __name__ == "__main__":
    main()
