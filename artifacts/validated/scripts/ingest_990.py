#!/usr/bin/env python3
"""
Ingest IRS Form 990 data from moonlight facts.csv into validated artifacts.

Creates:
- money_flow artifacts for government grants received (upstream)
- money_flow artifacts for Schedule I grants paid (downstream)
- evidence_item artifacts linking to 990 source

Usage:
    python scripts/ingest_990.py [--dry-run] [--limit N] [--ein EIN]
    python scripts/ingest_990.py --stats
"""

import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# Paths
MOONLIGHT_FACTS = Path("C:/Threshold/moonlight/data/teos/out/facts.csv")
VALIDATED_ROOT = Path(__file__).parent.parent
MONEY_FLOW_DIR = VALIDATED_ROOT / "money_flow"
EVIDENCE_DIR = VALIDATED_ROOT / "evidence_item"
REGISTRY_DIR = VALIDATED_ROOT / "_990_registry"

# Fact key patterns
PATTERNS = {
    "org_name": re.compile(r"^org\.name$"),
    "govt_grants": re.compile(r"GovernmentGrants(Amt)?(\[0\])?$"),
    "total_contributions": re.compile(r"TotalContributions(Amt)?(\[0\])?$"),
    "gross_receipts": re.compile(r"GrossReceipts(Amt)?(\[0\])?$"),
    # Schedule I - grants paid out
    "sched_i_recipient_name": re.compile(r"ScheduleI.*RecipientTable\[(\d+)\].*BusinessName(Line1)?(Txt)?(\[0\])?$"),
    "sched_i_recipient_ein": re.compile(r"ScheduleI.*RecipientTable\[(\d+)\].*(RecipientEIN|EINOfRecipient)(\[0\])?$"),
    "sched_i_cash_grant": re.compile(r"ScheduleI.*RecipientTable\[(\d+)\].*CashGrantAmt(\[0\])?$"),
    "sched_i_purpose": re.compile(r"ScheduleI.*RecipientTable\[(\d+)\].*PurposeOfGrantTxt(\[0\])?$"),
    "sched_i_city": re.compile(r"ScheduleI.*RecipientTable\[(\d+)\].*(City|CityNm)(\[0\])?$"),
    "sched_i_state": re.compile(r"ScheduleI.*RecipientTable\[(\d+)\].*(State|StateAbbreviationCd)(\[0\])?$"),
}


def parse_facts_csv(facts_path: Path, target_ein: str = None, limit: int = None):
    """
    Parse facts.csv into structured org data.
    Returns dict: {ein: {year: {fact_type: value}}}
    """
    orgs = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    row_count = 0
    
    print(f"📖 Reading {facts_path}...")
    
    with open(facts_path, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ein = row.get('entity_id', '').strip()
            year = row.get('tax_year', '').strip()
            fact_key = row.get('fact_key', '')
            fact_value = row.get('fact_value', '').strip()
            
            if not ein or not year or not fact_value:
                continue
                
            if target_ein and ein != target_ein:
                continue
            
            # Match against patterns
            if PATTERNS["org_name"].search(fact_key):
                orgs[ein][year]["org_name"] = fact_value
            elif PATTERNS["govt_grants"].search(fact_key):
                orgs[ein][year]["govt_grants"] = parse_amount(fact_value)
            elif PATTERNS["total_contributions"].search(fact_key):
                orgs[ein][year]["total_contributions"] = parse_amount(fact_value)
            elif PATTERNS["gross_receipts"].search(fact_key):
                orgs[ein][year]["gross_receipts"] = parse_amount(fact_value)
            
            # Schedule I grants paid
            for pattern_name in ["sched_i_recipient_name", "sched_i_recipient_ein", 
                                  "sched_i_cash_grant", "sched_i_purpose",
                                  "sched_i_city", "sched_i_state"]:
                match = PATTERNS[pattern_name].search(fact_key)
                if match:
                    idx = match.group(1)
                    field = pattern_name.replace("sched_i_", "")
                    if "grants_paid" not in orgs[ein][year]:
                        orgs[ein][year]["grants_paid"] = {}
                    if idx not in orgs[ein][year]["grants_paid"]:
                        orgs[ein][year]["grants_paid"][idx] = {}
                    orgs[ein][year]["grants_paid"][idx][field] = fact_value
                    break
            
            row_count += 1
            if limit and row_count >= limit:
                break
            if row_count % 500000 == 0:
                print(f"   Processed {row_count:,} rows...")
    
    print(f"   ✅ Processed {row_count:,} rows, found {len(orgs)} orgs")
    return orgs


def parse_amount(value: str) -> int:
    """Parse amount string to integer."""
    if not value or value == "RESTRICTED":
        return 0
    try:
        # Remove commas, decimals, dollar signs
        cleaned = re.sub(r'[,$]', '', value)
        return int(float(cleaned))
    except (ValueError, TypeError):
        return 0


def format_ein(ein: str) -> str:
    """Format EIN as XX-XXXXXXX."""
    ein = ein.replace("-", "").strip()
    if len(ein) == 9:
        return f"{ein[:2]}-{ein[2:]}"
    return ein


def sanitize_name(name: str) -> str:
    """Sanitize org name for use in flow_id."""
    # Take first 30 chars, uppercase, replace spaces/special chars
    name = name.upper()[:30]
    name = re.sub(r'[^A-Z0-9]', '-', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')


def create_money_flow_upstream(ein: str, year: str, org_data: dict) -> dict:
    """Create money_flow for government grants RECEIVED."""
    amount = org_data.get("govt_grants", 0)
    if amount <= 0:
        return None
    
    org_name = org_data.get("org_name", f"EIN {format_ein(ein)}")
    
    return {
        "flow_id": f"MF-990-{sanitize_name(org_name)}-GOVT-GRANTS-{year}",
        "source": "Government Grants (Federal/State)",
        "intermediary": "None",
        "destination": org_name,
        "amount": amount,
        "fund_type": "federal",  # Conservative assumption
        "fiscal_year": year,
        "restrictions": {
            "medicaid": False,
            "dhs_controlled": False
        },
        "statutory_basis": f"IRS Form 990 Part VIII Line 1e; EIN {format_ein(ein)} Tax Year {year}",
        "editor_status": "pending",
        "_990_source": {
            "ein": format_ein(ein),
            "tax_year": year,
            "fact_type": "GovernmentGrantsAmt"
        }
    }


def create_money_flow_downstream(ein: str, year: str, org_data: dict, grant_data: dict, idx: str) -> dict:
    """Create money_flow for Schedule I grants PAID."""
    amount = parse_amount(grant_data.get("cash_grant", "0"))
    if amount <= 0:
        return None
    
    source_name = org_data.get("org_name", f"EIN {format_ein(ein)}")
    recipient_name = grant_data.get("recipient_name", "Unknown Recipient")
    recipient_ein = grant_data.get("recipient_ein", "")
    purpose = grant_data.get("purpose", "")
    city = grant_data.get("city", "")
    state = grant_data.get("state", "")
    
    location = f"{city}, {state}" if city and state else ""
    
    return {
        "flow_id": f"MF-990-{sanitize_name(source_name)}-TO-{sanitize_name(recipient_name)}-{year}-{idx}",
        "source": source_name,
        "intermediary": "None",
        "destination": recipient_name,
        "amount": amount,
        "fund_type": "state",  # Passed through from grants
        "fiscal_year": year,
        "restrictions": {
            "medicaid": False,
            "dhs_controlled": False
        },
        "statutory_basis": f"IRS Form 990 Schedule I; EIN {format_ein(ein)} Tax Year {year}; Purpose: {purpose}" if purpose else f"IRS Form 990 Schedule I; EIN {format_ein(ein)} Tax Year {year}",
        "editor_status": "pending",
        "_990_source": {
            "source_ein": format_ein(ein),
            "recipient_ein": format_ein(recipient_ein) if recipient_ein else None,
            "recipient_location": location,
            "tax_year": year,
            "fact_type": "ScheduleI_RecipientTable"
        }
    }


def create_evidence_item(ein: str, year: str, org_data: dict) -> dict:
    """Create evidence_item for 990 filing."""
    org_name = org_data.get("org_name", f"EIN {format_ein(ein)}")
    govt_grants = org_data.get("govt_grants", 0)
    total_contrib = org_data.get("total_contributions", 0)
    grants_paid_count = len(org_data.get("grants_paid", {}))
    
    return {
        "evidence_id": f"EVID-990-{format_ein(ein).replace('-', '')}-{year}",
        "section": f"MF-990-{sanitize_name(org_name)}-GOVT-GRANTS-{year}",
        "claim_summary": f"IRS Form 990 for {org_name} (EIN {format_ein(ein)}) tax year {year} reports government grants of ${govt_grants:,}, total contributions of ${total_contrib:,}, and {grants_paid_count} grants paid to other organizations.",
        "evidence_type": "form-990",
        "source": {
            "title": f"IRS Form 990 - {org_name} - Tax Year {year}",
            "issuing_body": "Internal Revenue Service",
            "url": f"https://projects.propublica.org/nonprofits/organizations/{ein.replace('-', '')}"
        },
        "confidence_level": "high",
        "editor_status": "pending",
        "_990_source": {
            "ein": format_ein(ein),
            "tax_year": year
        }
    }


def generate_artifacts(orgs: dict, dry_run: bool = False):
    """Generate all artifacts from parsed org data."""
    stats = {
        "money_flow_upstream": 0,
        "money_flow_downstream": 0,
        "evidence_item": 0,
        "skipped": 0
    }
    
    all_artifacts = {
        "money_flow": [],
        "evidence_item": []
    }
    
    for ein, years in orgs.items():
        for year, org_data in years.items():
            if not year or not year.isdigit():
                continue
            
            # Upstream flow (govt grants received)
            upstream = create_money_flow_upstream(ein, year, org_data)
            if upstream:
                all_artifacts["money_flow"].append(upstream)
                stats["money_flow_upstream"] += 1
            
            # Downstream flows (Schedule I grants paid)
            for idx, grant_data in org_data.get("grants_paid", {}).items():
                downstream = create_money_flow_downstream(ein, year, org_data, grant_data, idx)
                if downstream:
                    all_artifacts["money_flow"].append(downstream)
                    stats["money_flow_downstream"] += 1
            
            # Evidence item
            if org_data.get("govt_grants", 0) > 0 or org_data.get("grants_paid"):
                evidence = create_evidence_item(ein, year, org_data)
                all_artifacts["evidence_item"].append(evidence)
                stats["evidence_item"] += 1
    
    return all_artifacts, stats


def write_artifacts(artifacts: dict, dry_run: bool = False):
    """Write artifacts to disk."""
    if dry_run:
        print("\n🔍 DRY RUN - No files written")
        print(f"   Would create {len(artifacts['money_flow'])} money_flow artifacts")
        print(f"   Would create {len(artifacts['evidence_item'])} evidence_item artifacts")
        
        # Show sample
        if artifacts["money_flow"]:
            print("\n📄 Sample money_flow:")
            print(json.dumps(artifacts["money_flow"][0], indent=2))
        if artifacts["evidence_item"]:
            print("\n📄 Sample evidence_item:")
            print(json.dumps(artifacts["evidence_item"][0], indent=2))
        return
    
    MONEY_FLOW_DIR.mkdir(exist_ok=True)
    EVIDENCE_DIR.mkdir(exist_ok=True)
    
    created = 0
    for flow in artifacts["money_flow"]:
        flow_id = flow["flow_id"]
        path = MONEY_FLOW_DIR / f"{flow_id}.json"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(flow, f, indent=2)
            f.write('\n')
        created += 1
    
    for evidence in artifacts["evidence_item"]:
        evid_id = evidence["evidence_id"]
        path = EVIDENCE_DIR / f"{evid_id}.json"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(evidence, f, indent=2)
            f.write('\n')
        created += 1
    
    print(f"\n✅ Created {created} artifacts")


def show_stats(orgs: dict):
    """Show statistics about the 990 data."""
    total_orgs = len(orgs)
    total_years = sum(len(years) for years in orgs.values())
    total_govt_grants = 0
    total_grants_paid = 0
    grants_paid_count = 0
    
    for ein, years in orgs.items():
        for year, org_data in years.items():
            total_govt_grants += org_data.get("govt_grants", 0)
            for grant in org_data.get("grants_paid", {}).values():
                amount = parse_amount(grant.get("cash_grant", "0"))
                total_grants_paid += amount
                grants_paid_count += 1
    
    print(f"""
📊 990 Data Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Organizations:          {total_orgs:,}
Org-Year combinations:  {total_years:,}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Government Grants Received:
  Total Amount:         ${total_govt_grants:,.0f}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Schedule I Grants Paid:
  Total Grants:         {grants_paid_count:,}
  Total Amount:         ${total_grants_paid:,.0f}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")


def main():
    parser = argparse.ArgumentParser(description="Ingest 990 data into validated artifacts")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument("--limit", type=int, help="Limit rows to process")
    parser.add_argument("--ein", type=str, help="Process only specific EIN")
    parser.add_argument("--stats", action="store_true", help="Show statistics only")
    args = parser.parse_args()
    
    if not MOONLIGHT_FACTS.exists():
        print(f"❌ Facts file not found: {MOONLIGHT_FACTS}")
        return
    
    # Parse the data
    orgs = parse_facts_csv(MOONLIGHT_FACTS, target_ein=args.ein, limit=args.limit)
    
    if args.stats:
        show_stats(orgs)
        return
    
    # Generate artifacts
    artifacts, stats = generate_artifacts(orgs, dry_run=args.dry_run)
    
    print(f"""
📦 Artifact Generation Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Money Flows (Upstream):   {stats['money_flow_upstream']:,}
Money Flows (Downstream): {stats['money_flow_downstream']:,}
Evidence Items:           {stats['evidence_item']:,}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total:                    {stats['money_flow_upstream'] + stats['money_flow_downstream'] + stats['evidence_item']:,}
""")
    
    # Write artifacts
    write_artifacts(artifacts, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
