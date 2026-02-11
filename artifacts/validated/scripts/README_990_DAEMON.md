# 990 Extraction Daemon

Overnight Ollama processor for IRS Form 990 data extraction.

## Setup

```powershell
# 1. Start Ollama (keep this terminal open)
ollama serve

# 2. Make sure you have a model pulled
ollama pull llama3.2:3b

# 3. Create queue directories
mkdir _990_queue
mkdir _990_extracted
mkdir _990_done
```

## Usage

```powershell
# Run daemon (loops forever)
python scripts/daemon_990_extractor.py

# Process queue once then exit
python scripts/daemon_990_extractor.py --once

# Use different model
python scripts/daemon_990_extractor.py --model llama3.2:latest

# Custom directories
python scripts/daemon_990_extractor.py --queue-dir "C:\990data\pending" --output-dir "C:\990data\extracted"
```

## Workflow

1. **Drop 990 files into `_990_queue/`**
   - Accepts: `.txt`, `.xml`, `.json`
   - Name files with EIN for easy tracking (e.g., `710499465_2023.txt`)

2. **Daemon processes one at a time**
   - Calls Ollama with extraction prompt
   - Outputs `{filename}_extracted.md` to `_990_extracted/`
   - Moves original to `_990_done/`
   - 5-second cooldown between files

3. **Review markdown output**
   - Check for quality/accuracy
   - Files needing review stay in output folder
   - Good extractions can be converted to JSON

## Converting to Artifacts

After review, convert markdown to JSON artifacts:

```python
# Example: parse markdown to evidence_item
import re

md_content = open("710499465_2023_extracted.md").read()

# Extract EIN from markdown
ein_match = re.search(r"\*\*EIN\*\*:\s*(\d{9}|\d{2}-\d{7})", md_content)
ein = ein_match.group(1).replace("-", "") if ein_match else "UNKNOWN"

artifact = {
    "evidence_id": f"EVID-990-{ein}-2023",
    "evidence_type": "budget",
    "section": "IRS Form 990",
    "claim_summary": "...",  # Extract from markdown
    "source": {
        "document": "Form 990",
        "ein": ein
    },
    "confidence_level": "medium",
    "editor_status": "pending"
}
```

## Tips

- **Overnight runs**: Start before bed, check results in morning
- **Model selection**: 3B models are fast but may miss nuance; 8B+ better for complex filings
- **Large files**: Truncated at 8000 chars; for full text use larger context model
- **Multiple instances**: Can run multiple daemons with different queue folders

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "Cannot connect to Ollama" | Run `ollama serve` in another terminal |
| Slow processing | Use smaller model or increase timeout |
| Missing fields in output | Larger model or better source file quality |
| Out of memory | Use quantized model (Q4_K_M) |
