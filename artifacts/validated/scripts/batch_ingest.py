#!/usr/bin/env python3
"""
Batch Ingestion Script for Operation NAMI Clearlane

Ingests batch_response files and splits artifacts into individual files.
Automatically sets editor_status to 'accepted'.

Usage:
  python batch_ingest.py <batch_file.json>
  python batch_ingest.py <batch_file.json> --dry-run    # Preview without writing
  python batch_ingest.py <batch_file.json> --pending    # Keep as pending (don't accept)
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

# Category folder mapping
CATEGORY_FOLDERS = {
    "money_flow": "money_flow",
    "authority_reference": "authority_reference",
    "evidence_item": "evidence_item",
    "field_validation": "field_validation"
}

# ID field by category
ID_FIELDS = {
    "money_flow": "flow_id",
    "authority_reference": "authority_id",
    "evidence_item": "evidence_id",
    "field_validation": "fv_id"
}


def ingest_batch(batch_path: str, dry_run: bool = False, accept: bool = True):
    """Ingest a batch file and create individual artifact files."""
    
    batch_file = Path(batch_path)
    if not batch_file.exists():
        print(f"❌ Batch file not found: {batch_path}")
        return
    
    with open(batch_file, "r", encoding="utf-8") as f:
        batch = json.load(f)
    
    print(f"\n📦 Ingesting batch: {batch.get('batch_id', 'unknown')}")
    print(f"   Generated: {batch.get('generated_at', '?')}")
    print(f"   Mode: {batch.get('mode', '?')}")
    print(f"   Turns: {batch.get('total_turns', '?')}")
    print()
    
    artifacts = batch.get("artifacts", {})
    total_created = 0
    total_skipped = 0
    total_updated = 0
    
    for category, items in artifacts.items():
        if category not in CATEGORY_FOLDERS:
            print(f"⚠️  Unknown category: {category}")
            continue
        
        folder = BASE_DIR / CATEGORY_FOLDERS[category]
        folder.mkdir(exist_ok=True)
        id_field = ID_FIELDS[category]
        
        print(f"📁 {category}: {len(items)} artifacts")
        
        for artifact in items:
            artifact_id = artifact.get(id_field)
            if not artifact_id:
                print(f"   ⚠️  Missing ID field '{id_field}', skipping")
                continue
            
            # Update editor_status if accepting
            if accept:
                artifact["editor_status"] = "accepted"
            
            # Add ingestion metadata
            artifact["_ingested_from"] = batch.get("batch_id", "unknown")
            artifact["_ingested_at"] = datetime.now().isoformat()
            
            # Create filename
            filename = f"{artifact_id}.json"
            filepath = folder / filename
            
            # Check for existing folder-style artifact (ID.yaml/ or ID.json/)
            folder_style_yaml = folder / f"{artifact_id}.yaml"
            folder_style_json = folder / f"{artifact_id}.json"
            
            action = "CREATE"
            
            # Handle folder-style artifacts first (they may look like .json but be dirs)
            if folder_style_json.exists() and folder_style_json.is_dir():
                # Update the 0.json inside the folder
                filepath = folder_style_json / "0.json"
                action = "UPDATE (folder)"
                total_updated += 1
            elif folder_style_yaml.exists() and folder_style_yaml.is_dir():
                # Update the 0.json inside the folder
                filepath = folder_style_yaml / "0.json"
                action = "UPDATE (folder)"
                total_updated += 1
            elif filepath.exists() and filepath.is_file():
                action = "UPDATE"
                total_updated += 1
            else:
                total_created += 1
            
            if dry_run:
                print(f"   [DRY-RUN] {action}: {filepath.name}")
            else:
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(artifact, f, indent=2, ensure_ascii=False)
                    f.write("\n")  # Trailing newline
                print(f"   ✅ {action}: {filepath.name}")
    
    print()
    print(f"{'[DRY-RUN] ' if dry_run else ''}Summary:")
    print(f"   Created: {total_created}")
    print(f"   Updated: {total_updated}")
    print(f"   Total:   {total_created + total_updated}")
    
    if not dry_run:
        print(f"\n✅ Ingestion complete. Run linkage analyzer to see connections:")
        print(f"   python scripts/linkage_analyzer.py --export-all")


def main():
    parser = argparse.ArgumentParser(description="Ingest batch artifacts")
    parser.add_argument("batch_file", help="Path to batch_response JSON file")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument("--pending", action="store_true", help="Keep editor_status as pending")
    args = parser.parse_args()
    
    ingest_batch(args.batch_file, dry_run=args.dry_run, accept=not args.pending)


if __name__ == "__main__":
    main()
