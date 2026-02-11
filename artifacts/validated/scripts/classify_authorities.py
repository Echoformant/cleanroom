#!/usr/bin/env python3
"""
classify_authorities.py - Add jurisdiction classification to authority artifacts

Classification Dimensions:
1. jurisdiction: federal, state, local
2. source_type: constitution, statute, regulation, act, administrative, mou, court_order, settlement
3. issuing_body: Derived from administering_body or ID pattern

This script reads existing authorities and outputs a classification JSON
without modifying the original artifacts.
"""

import json
import os
import re
from collections import defaultdict
from pathlib import Path

# Classification rules based on ID patterns
JURISDICTION_PATTERNS = [
    # Federal
    (r'^AUTH-US-', 'federal'),
    (r'^FED-REG-', 'federal'),
    (r'SAMHSA|BJA|ONDCP|DOJ|CMS|HHS', 'federal'),
    (r'42-?USC|34-?USC|U\.?S\.?C\.', 'federal'),
    
    # State
    (r'^AUTH-AR-|^AR-AUTH-', 'state'),
    (r'ACA-\d+-\d+', 'state'),  # Arkansas Code Annotated
    (r'ACT\d+|ACT-\d+', 'state'),  # Session laws
    (r'^AUTH-AR-CONST', 'state'),  # Constitution
    (r'SB\d+|HB\d+', 'state'),  # Bills
]

# Source type normalization
TYPE_NORMALIZATION = {
    'statute': 'statute',
    'act': 'act', 
    'regulation': 'regulation',
    'administrative': 'administrative',
    'constitution': 'constitution',
    'court_order': 'court_order',
    'mou': 'mou',
    'memorandum': 'mou',
    'settlement': 'settlement',
    'policy': 'policy',
    'waiver': 'waiver',
    'appropriation': 'act',
    'federal_requirement': 'regulation',
    '': 'unknown',
    None: 'unknown'
}

# Issuing body extraction patterns
ISSUING_BODY_PATTERNS = [
    (r'DHS|Department of Human Services', 'DHS'),
    (r'AOC|Administrative Office.*Courts', 'AOC'),
    (r'SAMHSA', 'SAMHSA'),
    (r'BJA|Bureau of Justice', 'DOJ-BJA'),
    (r'ONDCP', 'ONDCP'),
    (r'CMS|Centers for Medicare', 'CMS'),
    (r'General Assembly|Legislature', 'General Assembly'),
    (r'Supreme Court', 'Supreme Court'),
    (r'Governor', 'Governor'),
]


def classify_jurisdiction(authority_id: str) -> str:
    """Determine jurisdiction from authority ID."""
    for pattern, jurisdiction in JURISDICTION_PATTERNS:
        if re.search(pattern, authority_id, re.IGNORECASE):
            return jurisdiction
    return 'state'  # Default to state for Arkansas repo


def normalize_type(authority_type: str) -> str:
    """Normalize authority type to canonical categories."""
    return TYPE_NORMALIZATION.get(authority_type, 'unknown')


def extract_issuing_body(authority: dict) -> str:
    """Extract issuing body from administering_body or ID."""
    admin_body = authority.get('administering_body', '')
    auth_id = authority.get('authority_id', '')
    
    # Check patterns in admin body first
    for pattern, body in ISSUING_BODY_PATTERNS:
        if re.search(pattern, admin_body, re.IGNORECASE):
            return body
        if re.search(pattern, auth_id, re.IGNORECASE):
            return body
    
    # Check for constitutional
    if 'CONST' in auth_id:
        return 'Constitution'
    
    # Federal patterns
    if classify_jurisdiction(auth_id) == 'federal':
        if 'USC' in auth_id:
            return 'US Congress'
        if 'CFR' in auth_id:
            return 'Federal Agency'
    
    return admin_body if admin_body else 'Unknown'


def classify_all_authorities(repo_root: Path) -> dict:
    """Classify all authority artifacts."""
    auth_dir = repo_root / 'authority_reference'
    classifications = {}
    stats = defaultdict(lambda: defaultdict(int))
    
    for path in auth_dir.glob('*.json'):
        if path.is_dir():
            # Handle folder-style artifacts
            inner = path / '0.json'
            if inner.exists():
                with open(inner, encoding='utf-8') as f:
                    auth = json.load(f)
            else:
                continue
        else:
            try:
                with open(path, encoding='utf-8') as f:
                    auth = json.load(f)
            except (PermissionError, json.JSONDecodeError):
                continue
        
        auth_id = auth.get('authority_id', path.stem)
        
        classification = {
            'authority_id': auth_id,
            'jurisdiction': classify_jurisdiction(auth_id),
            'source_type': normalize_type(auth.get('authority_type')),
            'issuing_body': extract_issuing_body(auth),
            'original_type': auth.get('authority_type', ''),
            'governs_count': len(auth.get('governs', [])),
        }
        
        classifications[auth_id] = classification
        
        # Collect stats
        stats['jurisdiction'][classification['jurisdiction']] += 1
        stats['source_type'][classification['source_type']] += 1
        stats['issuing_body'][classification['issuing_body']] += 1
    
    return {
        'classifications': classifications,
        'stats': {k: dict(v) for k, v in stats.items()},
        'total': len(classifications)
    }


def main():
    repo_root = Path(__file__).parent.parent
    
    print("Classifying authority artifacts...")
    result = classify_all_authorities(repo_root)
    
    # Save classification data
    output_path = repo_root / '_data' / 'authority_classifications.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n✅ Classified {result['total']} authorities")
    print(f"   Saved to: {output_path}")
    
    print("\n📊 Jurisdiction breakdown:")
    for j, count in sorted(result['stats']['jurisdiction'].items(), key=lambda x: -x[1]):
        print(f"   {j}: {count}")
    
    print("\n📊 Source type breakdown:")
    for t, count in sorted(result['stats']['source_type'].items(), key=lambda x: -x[1]):
        print(f"   {t}: {count}")
    
    print("\n📊 Top issuing bodies:")
    for b, count in sorted(result['stats']['issuing_body'].items(), key=lambda x: -x[1])[:10]:
        print(f"   {b}: {count}")


if __name__ == '__main__':
    main()
