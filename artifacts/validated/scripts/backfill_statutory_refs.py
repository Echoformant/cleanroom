#!/usr/bin/env python3
"""
Backfill statutory_basis_refs arrays for money_flow artifacts.

Parses the text statutory_basis field, matches patterns to existing 
authority/evidence IDs, and populates statutory_basis_refs array.

Usage:
    python scripts/backfill_statutory_refs.py              # Dry run
    python scripts/backfill_statutory_refs.py --apply      # Apply changes
    python scripts/backfill_statutory_refs.py --report     # Show match report
"""

import json
import re
import os
import sys
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent
MONEY_FLOW_DIR = WORKSPACE / "money_flow"
AUTHORITY_DIR = WORKSPACE / "authority_reference"
EVIDENCE_DIR = WORKSPACE / "evidence_item"


def load_all_ids():
    """Load all authority and evidence IDs for matching."""
    ids = {}
    
    # Load authorities
    for f in AUTHORITY_DIR.glob("*.json"):
        if f.is_file():
            try:
                data = json.loads(f.read_text(encoding='utf-8'))
                aid = data.get('authority_id', f.stem)
                citation = data.get('citation', '')
                ids[aid] = {'type': 'authority', 'citation': citation}
            except:
                pass
    
    # Load evidence
    for f in EVIDENCE_DIR.glob("*.json"):
        if f.is_file():
            try:
                data = json.loads(f.read_text(encoding='utf-8'))
                eid = data.get('evidence_id', f.stem)
                section = data.get('section', '')
                ids[eid] = {'type': 'evidence', 'section': section}
            except:
                pass
    
    return ids


def build_citation_index(all_ids):
    """Build index from citation text patterns to artifact IDs."""
    index = {}
    
    for aid, info in all_ids.items():
        if info['type'] == 'authority':
            citation = info.get('citation', '')
            if citation:
                # Normalize citation for matching
                normalized = normalize_citation(citation)
                if normalized:
                    index[normalized] = aid
            
            # Also index from ID patterns
            # AUTH-AR-ACA-20-77-107 -> "20-77-107"
            match = re.search(r'(\d+-\d+-\d+)', aid)
            if match:
                index[match.group(1)] = aid
            
            # AUTH-US-OPIOID-SETTLEMENT-CVS -> "opioid settlement cvs"
            if 'OPIOID-SETTLEMENT' in aid:
                settlement = aid.split('OPIOID-SETTLEMENT-')[-1].lower()
                index[f"opioid settlement {settlement}"] = aid
    
    return index


def normalize_citation(text):
    """Normalize citation text for matching."""
    if not text:
        return None
    
    # Extract code section patterns like "20-77-107" or "§ 20-77-107"
    patterns = [
        r'(\d{1,2}-\d{1,2}-\d+)',           # 20-77-107
        r'§\s*(\d{1,2}-\d{1,2}-\d+)',        # § 20-77-107
        r'Ark\.?\s*Code\s*§?\s*(\d{1,2}-\d{1,2}-\d+)',  # Ark. Code § 20-77-107
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    
    return None


def find_matching_refs(statutory_basis, citation_index, all_ids):
    """Find artifact IDs that match the statutory_basis text."""
    if not statutory_basis:
        return []
    
    refs = []
    
    # Direct code section match
    sections = re.findall(r'\d{1,2}-\d{1,2}-\d+', statutory_basis)
    for section in sections:
        if section in citation_index:
            refs.append(citation_index[section])
    
    # Settlement name matches
    settlement_names = ['cvs', 'walgreens', 'walmart', 'kroger', 'teva', 
                        'allergan', 'janssen', 'distributor']
    text_lower = statutory_basis.lower()
    for name in settlement_names:
        if name in text_lower:
            key = f"opioid settlement {name}"
            if key in citation_index:
                refs.append(citation_index[key])
    
    # MOU match
    if 'mou' in text_lower or 'memorandum' in text_lower:
        for aid in all_ids:
            if 'MOU' in aid:
                refs.append(aid)
    
    # QSF match
    if 'qsf' in text_lower or 'qualified settlement fund' in text_lower:
        for aid in all_ids:
            if 'QSF' in aid:
                refs.append(aid)
    
    return list(set(refs))  # Deduplicate


def process_money_flows(apply=False, report=False):
    """Process all money_flow artifacts and backfill refs."""
    all_ids = load_all_ids()
    citation_index = build_citation_index(all_ids)
    
    results = {
        'updated': [],
        'already_has_refs': [],
        'no_matches': [],
        'no_statutory_basis': []
    }
    
    for f in sorted(MONEY_FLOW_DIR.glob("*.json")):
        if not f.is_file():
            continue
        
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
        except:
            continue
        
        flow_id = data.get('flow_id', f.stem)
        statutory_basis = data.get('statutory_basis', '')
        existing_refs = data.get('statutory_basis_refs', [])
        
        if existing_refs:
            results['already_has_refs'].append(flow_id)
            continue
        
        if not statutory_basis:
            results['no_statutory_basis'].append(flow_id)
            continue
        
        matched_refs = find_matching_refs(statutory_basis, citation_index, all_ids)
        
        if not matched_refs:
            results['no_matches'].append({
                'id': flow_id,
                'statutory_basis': statutory_basis[:100]
            })
            continue
        
        results['updated'].append({
            'id': flow_id,
            'refs': matched_refs
        })
        
        if apply:
            data['statutory_basis_refs'] = matched_refs
            f.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    
    return results


def main():
    apply = '--apply' in sys.argv
    report = '--report' in sys.argv
    
    print("Backfilling statutory_basis_refs...")
    print(f"Mode: {'APPLY' if apply else 'DRY RUN'}")
    print()
    
    results = process_money_flows(apply=apply, report=report)
    
    print(f"Updated (or would update): {len(results['updated'])}")
    for item in results['updated'][:10]:
        print(f"  {item['id']} -> {item['refs']}")
    if len(results['updated']) > 10:
        print(f"  ... and {len(results['updated']) - 10} more")
    
    print(f"\nAlready has refs: {len(results['already_has_refs'])}")
    print(f"No statutory_basis: {len(results['no_statutory_basis'])}")
    print(f"No matches found: {len(results['no_matches'])}")
    
    if report and results['no_matches']:
        print("\n--- NO MATCHES (may need manual linking or new authorities) ---")
        for item in results['no_matches']:
            print(f"  {item['id']}: {item['statutory_basis']}")
    
    if not apply:
        print("\nRun with --apply to save changes")


if __name__ == "__main__":
    main()
