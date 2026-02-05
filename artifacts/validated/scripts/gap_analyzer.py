#!/usr/bin/env python3
"""
Gap Analyzer for Arkansas Public-Finance Validated Artifacts

Discovers gaps in the artifact network based on three canonical gap types:
  - INCOMPLETE_CHAIN: References to artifacts that don't exist
  - MISSING_VALIDATION: Money flows or authorities without field_validation coverage
  - ORPHAN_REFERENCE: Pattern-matched references that imply missing artifacts

Outputs:
  - Gap records as JSON files in _gaps/ directory
  - Stub artifacts for missing targets in _stubs/ directory
  - Summary report to console

Usage:
  python gap_analyzer.py                    # Full gap analysis with stubs
  python gap_analyzer.py --no-stubs         # Analysis only, no stub generation
  python gap_analyzer.py --type INCOMPLETE_CHAIN  # Filter by gap type
  python gap_analyzer.py --summary          # Summary statistics only
  python gap_analyzer.py --json             # Output full report as JSON

See docs/canonical_gap_definitions.md for gap type definitions.
"""

import json
import os
import re
import argparse
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional

# Base directory (script location -> parent)
BASE_DIR = Path(__file__).resolve().parent.parent
GAPS_DIR = BASE_DIR / "_gaps"
STUBS_DIR = BASE_DIR / "_stubs"

# Gap type constants
GAP_INCOMPLETE_CHAIN = "INCOMPLETE_CHAIN"
GAP_MISSING_VALIDATION = "MISSING_VALIDATION"
GAP_ORPHAN_REFERENCE = "ORPHAN_REFERENCE"

# Artifact ID patterns for detection
ARTIFACT_PATTERNS = {
    "money_flow": [
        r"MF-[A-Z0-9\-]+",
        r"AR_FY\d{4}_[A-Z0-9_]+",
    ],
    "authority_reference": [
        r"AUTH-[A-Z0-9\-]+",
        r"AR-AUTH-[A-Z0-9\-]+",
    ],
    "evidence_item": [
        r"EVID-[A-Z0-9\-]+",
        r"EV-[A-Z0-9\-]+",
    ],
    "field_validation": [
        r"FV-[A-Z0-9\-]+",
    ],
}


def load_artifacts() -> Dict[str, dict]:
    """Load all artifacts from the repository into a dict keyed by ID."""
    artifacts = {}
    categories = ["money_flow", "authority_reference", "evidence_item", "field_validation"]
    
    for category in categories:
        cat_path = BASE_DIR / category
        if not cat_path.exists():
            continue
            
        for item in cat_path.iterdir():
            # Skip hidden, batch folders, and .github
            if item.name.startswith(".") or "batch" in item.name.lower():
                continue
                
            artifact = None
            artifact_id = None
            
            if item.is_file() and item.suffix == ".json":
                try:
                    with open(item, "r", encoding="utf-8") as f:
                        artifact = json.load(f)
                except (json.JSONDecodeError, IOError):
                    continue
            elif item.is_dir() and (item.name.endswith(".yaml") or item.name.endswith(".json")):
                inner = item / "0.json"
                if inner.exists():
                    try:
                        with open(inner, "r", encoding="utf-8") as f:
                            artifact = json.load(f)
                    except (json.JSONDecodeError, IOError):
                        continue
            
            if artifact:
                if category == "money_flow":
                    artifact_id = artifact.get("flow_id")
                elif category == "authority_reference":
                    artifact_id = artifact.get("authority_id")
                elif category == "evidence_item":
                    artifact_id = artifact.get("evidence_id")
                elif category == "field_validation":
                    artifact_id = artifact.get("fv_id")
                
                if artifact_id:
                    artifacts[artifact_id] = {
                        "category": category,
                        "data": artifact,
                        "path": str(item)
                    }
    
    return artifacts


def extract_artifact_references(text: str) -> List[Tuple[str, str]]:
    """
    Extract potential artifact ID references from text.
    Returns list of (matched_id, expected_category) tuples.
    """
    if not text:
        return []
    
    found = []
    for category, patterns in ARTIFACT_PATTERNS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                found.append((match.group(0), category))
    
    return found


def find_incomplete_chains(artifacts: Dict[str, dict]) -> List[dict]:
    """
    GAP-001: INCOMPLETE_CHAIN
    Find references to artifacts that don't exist.
    """
    gaps = []
    all_ids = set(artifacts.keys())
    timestamp = datetime.now(timezone.utc).isoformat()
    
    for artifact_id, info in artifacts.items():
        data = info["data"]
        category = info["category"]
        
        fields_to_check = []
        
        if category == "money_flow":
            fields_to_check.append(("statutory_basis", data.get("statutory_basis", "")))
        
        elif category == "authority_reference":
            for i, gov in enumerate(data.get("governs", [])):
                fields_to_check.append((f"governs[{i}]", gov))
            fields_to_check.append(("citation", data.get("citation", "")))
        
        elif category == "evidence_item":
            fields_to_check.append(("section", data.get("section", "")))
            fields_to_check.append(("claim_summary", data.get("claim_summary", "")))
        
        elif category == "field_validation":
            for i, basis in enumerate(data.get("evidence_basis", [])):
                fields_to_check.append((f"evidence_basis[{i}]", basis))
        
        for field_name, field_value in fields_to_check:
            refs = extract_artifact_references(field_value)
            for ref_id, expected_category in refs:
                # Normalize for comparison
                ref_upper = ref_id.upper()
                matched = False
                for existing_id in all_ids:
                    if existing_id.upper() == ref_upper or ref_upper in existing_id.upper():
                        matched = True
                        break
                
                if not matched and ref_id != artifact_id:
                    gap_id = f"GAP-INCOMPLETE-{artifact_id[:30]}-{ref_id[:30]}"
                    gaps.append({
                        "gap_id": gap_id,
                        "gap_type": GAP_INCOMPLETE_CHAIN,
                        "source_artifact": artifact_id,
                        "source_category": category,
                        "source_field": field_name,
                        "target_reference": ref_id,
                        "target_category": expected_category,
                        "detected_at": timestamp,
                        "stub_generated": False,
                        "stub_path": None
                    })
    
    return gaps


def find_missing_validation(artifacts: Dict[str, dict]) -> List[dict]:
    """
    GAP-002: MISSING_VALIDATION
    Find money_flow and authority_reference artifacts without field_validation coverage.
    """
    gaps = []
    timestamp = datetime.now(timezone.utc).isoformat()
    
    # Collect all evidence_basis references from field_validations
    validated_refs = set()
    for artifact_id, info in artifacts.items():
        if info["category"] == "field_validation":
            for basis in info["data"].get("evidence_basis", []):
                # Extract artifact IDs from the evidence_basis string
                refs = extract_artifact_references(basis)
                for ref_id, _ in refs:
                    validated_refs.add(ref_id.upper())
                # Also add the raw string in case it's a direct ID
                validated_refs.add(basis.upper())
    
    # Check money_flow and authority_reference for coverage
    for artifact_id, info in artifacts.items():
        if info["category"] in ["money_flow", "authority_reference"]:
            # Check if this artifact is referenced by any field_validation
            is_validated = False
            for validated in validated_refs:
                if artifact_id.upper() in validated or validated in artifact_id.upper():
                    is_validated = True
                    break
            
            if not is_validated:
                gap_id = f"GAP-NOVALIDATION-{artifact_id[:50]}"
                gaps.append({
                    "gap_id": gap_id,
                    "gap_type": GAP_MISSING_VALIDATION,
                    "source_artifact": artifact_id,
                    "source_category": info["category"],
                    "source_field": None,
                    "target_reference": f"[field_validation for {artifact_id}]",
                    "target_category": "field_validation",
                    "detected_at": timestamp,
                    "stub_generated": False,
                    "stub_path": None
                })
    
    return gaps


def find_orphan_references(artifacts: Dict[str, dict]) -> List[dict]:
    """
    GAP-003: ORPHAN_REFERENCE
    Find pattern-matched references that imply missing artifacts.
    """
    gaps = []
    all_ids = set(artifacts.keys())
    all_ids_upper = {aid.upper() for aid in all_ids}
    timestamp = datetime.now(timezone.utc).isoformat()
    
    # Already found in incomplete_chains - we need to find additional orphans
    # Focus on section field in evidence_items pointing to flows
    for artifact_id, info in artifacts.items():
        if info["category"] == "evidence_item":
            section = info["data"].get("section", "")
            if not section:
                continue
            
            # Extract flow-like patterns from section
            flow_patterns = [
                r"AR_FY\d{4}_[A-Z0-9_]+",
                r"MF-[A-Z][A-Za-z0-9\-]+",
            ]
            
            for pattern in flow_patterns:
                for match in re.finditer(pattern, section):
                    ref_id = match.group(0)
                    # Check if this flow exists
                    ref_upper = ref_id.upper()
                    exists = any(ref_upper == aid.upper() or ref_upper in aid.upper() 
                                for aid in all_ids)
                    
                    if not exists:
                        gap_id = f"GAP-ORPHAN-{artifact_id[:30]}-{ref_id[:30]}"
                        gaps.append({
                            "gap_id": gap_id,
                            "gap_type": GAP_ORPHAN_REFERENCE,
                            "source_artifact": artifact_id,
                            "source_category": "evidence_item",
                            "source_field": "section",
                            "target_reference": ref_id,
                            "target_category": "money_flow",
                            "detected_at": timestamp,
                            "stub_generated": False,
                            "stub_path": None
                        })
    
    return gaps


def generate_stub(gap: dict, artifacts: Dict[str, dict]) -> Optional[dict]:
    """Generate a stub artifact for a gap."""
    target_category = gap["target_category"]
    target_ref = gap["target_reference"]
    timestamp = gap["detected_at"]
    
    gap_metadata = {
        "generated_by": "gap_analyzer",
        "gap_type": gap["gap_type"],
        "source_artifact": gap["source_artifact"],
        "detected_at": timestamp
    }
    
    if target_category == "money_flow":
        return {
            "flow_id": target_ref,
            "source": "[GAP STUB - source needed]",
            "intermediary": "None",
            "destination": "[GAP STUB - destination needed]",
            "amount": 0,
            "fund_type": "state",
            "fiscal_year": "2026",
            "restrictions": {
                "medicaid": False,
                "dhs_controlled": False
            },
            "statutory_basis": "[GAP STUB - statutory basis needed]",
            "editor_status": "pending",
            "_gap_metadata": gap_metadata
        }
    
    elif target_category == "authority_reference":
        return {
            "authority_id": target_ref,
            "authority_type": "statute",
            "citation": "[GAP STUB - citation needed]",
            "administering_body": "[GAP STUB - administering body needed]",
            "governs": ["[GAP STUB - governs entries needed]"],
            "effects": {
                "access_limiting": False,
                "appeal_mechanism": False
            },
            "editor_status": "pending",
            "_gap_metadata": gap_metadata
        }
    
    elif target_category == "evidence_item":
        return {
            "evidence_id": target_ref,
            "section": "[GAP STUB - section needed]",
            "claim_summary": "[GAP STUB - claim summary needed]",
            "evidence_type": "budget",
            "source": {
                "title": "[GAP STUB - title needed]",
                "issuing_body": "[GAP STUB - issuing body needed]"
            },
            "confidence_level": "low",
            "editor_status": "pending",
            "_gap_metadata": gap_metadata
        }
    
    elif target_category == "field_validation":
        # For missing validation, create a stub FV
        source_id = gap["source_artifact"]
        fv_id = f"FV-GAP-{source_id[:40]}"
        return {
            "fv_id": fv_id,
            "jurisdiction": "Arkansas",
            "validating_entity": "[GAP STUB - validating entity needed]",
            "alignment_status": "open",
            "evidence_basis": [source_id],
            "disclosure_level": "restricted",
            "editor_status": "pending",
            "_gap_metadata": gap_metadata
        }
    
    return None


def save_gaps_and_stubs(gaps: List[dict], generate_stubs: bool = True):
    """Save gap records and optionally generate stubs."""
    # Create directories
    GAPS_DIR.mkdir(exist_ok=True)
    if generate_stubs:
        STUBS_DIR.mkdir(exist_ok=True)
    
    for gap in gaps:
        # Save gap record
        gap_filename = f"{gap['gap_id']}.json"
        gap_path = GAPS_DIR / gap_filename
        
        if generate_stubs and gap["target_category"]:
            stub = generate_stub(gap, {})
            if stub:
                # Determine stub filename
                if gap["target_category"] == "field_validation":
                    stub_id = stub.get("fv_id", gap["target_reference"])
                else:
                    stub_id = gap["target_reference"]
                
                stub_filename = f"{stub_id}.json"
                stub_path = STUBS_DIR / stub_filename
                
                # Save stub
                with open(stub_path, "w", encoding="utf-8") as f:
                    json.dump(stub, f, indent=2, ensure_ascii=False)
                    f.write("\n")
                
                gap["stub_generated"] = True
                gap["stub_path"] = str(stub_path)
        
        # Save gap record
        with open(gap_path, "w", encoding="utf-8") as f:
            json.dump(gap, f, indent=2, ensure_ascii=False)
            f.write("\n")


def deduplicate_gaps(gaps: List[dict]) -> List[dict]:
    """Remove duplicate gaps based on source+target combination."""
    seen = set()
    unique = []
    for gap in gaps:
        key = (gap["source_artifact"], gap["target_reference"], gap["gap_type"])
        if key not in seen:
            seen.add(key)
            unique.append(gap)
    return unique


def print_summary(gaps: List[dict], artifacts: Dict[str, dict]):
    """Print summary statistics."""
    print(f"\n{'='*80}")
    print(f"📊 Gap Analysis Summary")
    print(f"{'='*80}\n")
    
    print(f"Total artifacts analyzed: {len(artifacts)}")
    print(f"Total gaps discovered: {len(gaps)}\n")
    
    # By type
    by_type = defaultdict(list)
    for gap in gaps:
        by_type[gap["gap_type"]].append(gap)
    
    print("Gaps by type:")
    for gap_type in [GAP_INCOMPLETE_CHAIN, GAP_MISSING_VALIDATION, GAP_ORPHAN_REFERENCE]:
        count = len(by_type.get(gap_type, []))
        print(f"  {gap_type}: {count}")
    
    # By source category
    print("\nGaps by source category:")
    by_source_cat = defaultdict(int)
    for gap in gaps:
        by_source_cat[gap["source_category"]] += 1
    for cat, count in sorted(by_source_cat.items()):
        print(f"  {cat}: {count}")
    
    # By target category
    print("\nMissing artifacts by expected category:")
    by_target_cat = defaultdict(int)
    for gap in gaps:
        by_target_cat[gap["target_category"]] += 1
    for cat, count in sorted(by_target_cat.items()):
        print(f"  {cat}: {count}")


def print_gaps_by_type(gaps: List[dict], gap_type: str):
    """Print gaps filtered by type."""
    filtered = [g for g in gaps if g["gap_type"] == gap_type]
    
    print(f"\n{'='*80}")
    print(f"🔍 {gap_type} Gaps ({len(filtered)} total)")
    print(f"{'='*80}\n")
    
    for gap in filtered[:30]:  # Limit to 30
        print(f"Source: {gap['source_artifact']}")
        print(f"  → Missing: {gap['target_reference']} ({gap['target_category']})")
        if gap.get("source_field"):
            print(f"  → Field: {gap['source_field']}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Analyze gaps in artifact network")
    parser.add_argument("--no-stubs", action="store_true", help="Don't generate stub artifacts")
    parser.add_argument("--type", choices=[GAP_INCOMPLETE_CHAIN, GAP_MISSING_VALIDATION, GAP_ORPHAN_REFERENCE],
                       help="Filter by gap type")
    parser.add_argument("--summary", action="store_true", help="Show summary only")
    parser.add_argument("--json", action="store_true", help="Output full report as JSON")
    args = parser.parse_args()
    
    print("Loading artifacts...")
    artifacts = load_artifacts()
    print(f"Loaded {len(artifacts)} artifacts")
    
    print("\nAnalyzing for gaps...")
    
    # Find all gap types
    gaps = []
    
    print("  → Checking for INCOMPLETE_CHAIN gaps...")
    gaps.extend(find_incomplete_chains(artifacts))
    
    print("  → Checking for MISSING_VALIDATION gaps...")
    gaps.extend(find_missing_validation(artifacts))
    
    print("  → Checking for ORPHAN_REFERENCE gaps...")
    gaps.extend(find_orphan_references(artifacts))
    
    # Deduplicate
    gaps = deduplicate_gaps(gaps)
    print(f"\nFound {len(gaps)} unique gaps")
    
    # Filter if requested
    if args.type:
        gaps = [g for g in gaps if g["gap_type"] == args.type]
        print(f"Filtered to {len(gaps)} gaps of type {args.type}")
    
    # Output
    if args.json:
        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "artifact_count": len(artifacts),
            "gap_count": len(gaps),
            "gaps": gaps
        }
        print(json.dumps(report, indent=2))
    elif args.summary:
        print_summary(gaps, artifacts)
    else:
        # Full run: save gaps and stubs, then print summary
        print("\nSaving gaps and generating stubs...")
        save_gaps_and_stubs(gaps, generate_stubs=not args.no_stubs)
        
        print_summary(gaps, artifacts)
        
        # Print details by type
        for gap_type in [GAP_INCOMPLETE_CHAIN, GAP_MISSING_VALIDATION, GAP_ORPHAN_REFERENCE]:
            type_gaps = [g for g in gaps if g["gap_type"] == gap_type]
            if type_gaps:
                print_gaps_by_type(gaps, gap_type)
        
        print(f"\n📁 Gap records saved to: {GAPS_DIR}")
        if not args.no_stubs:
            print(f"📁 Stub artifacts saved to: {STUBS_DIR}")


if __name__ == "__main__":
    main()
