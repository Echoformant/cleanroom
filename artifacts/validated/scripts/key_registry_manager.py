#!/usr/bin/env python3
"""
Key Registry Manager

Syncs key_registry.yaml to SQLite and provides lookup functions.

Usage:
    python key_registry_manager.py sync      # Sync YAML to SQLite
    python key_registry_manager.py lookup    # Interactive lookup
    python key_registry_manager.py stats     # Show registry stats
"""

import sqlite3
import yaml
import argparse
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
REGISTRY_YAML = SCRIPT_DIR.parent / "_formulas" / "key_registry" / "key_registry.yaml"
REGISTRY_SQL = SCRIPT_DIR.parent / "_formulas" / "key_registry" / "key_registry.sql"
DB_PATH = SCRIPT_DIR.parent / "_data" / "artifacts_graph.db"


def load_yaml_registry():
    """Load registry from YAML."""
    if not REGISTRY_YAML.exists():
        print(f"YAML not found: {REGISTRY_YAML}")
        return []
    with open(REGISTRY_YAML, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or []


def init_db(conn):
    """Initialize the key_registry table."""
    if REGISTRY_SQL.exists():
        with open(REGISTRY_SQL, 'r', encoding='utf-8') as f:
            sql = f.read()
        # Execute only the CREATE statements, not the INSERTs
        for stmt in sql.split(';'):
            if 'CREATE' in stmt.upper() and 'INSERT' not in stmt.upper():
                try:
                    conn.execute(stmt)
                except sqlite3.Error:
                    pass  # Table/index may already exist
    conn.commit()


def sync_yaml_to_db():
    """Sync YAML registry to SQLite."""
    records = load_yaml_registry()
    if not records:
        print("No records to sync.")
        return
    
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    
    # Clear existing data
    conn.execute("DELETE FROM key_registry")
    
    # Insert records
    for rec in records:
        conn.execute("""
            INSERT INTO key_registry 
            (entity_name, uei, ein, assistance_listing, state_fund_code, 
             duns_legacy, aka_names, status, source_of_truth, valid_from, valid_to)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            rec.get('entity_name'),
            rec.get('uei'),
            rec.get('ein'),
            '|'.join(rec.get('assistance_listing', [])) or None,
            '|'.join(rec.get('state_fund_code', [])) or None,
            rec.get('duns_legacy'),
            '|'.join(rec.get('aka_names', [])) or None,
            rec.get('status', 'active'),
            rec.get('source_of_truth'),
            rec.get('valid_from'),
            rec.get('valid_to')
        ))
    
    conn.commit()
    print(f"Synced {len(records)} records to {DB_PATH}")
    conn.close()


def lookup_entity(query):
    """Lookup entity by any key."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Search across all key fields
    cur = conn.execute("""
        SELECT * FROM key_registry
        WHERE entity_name LIKE ?
           OR uei = ?
           OR ein = ?
           OR assistance_listing LIKE ?
           OR state_fund_code LIKE ?
           OR aka_names LIKE ?
    """, (
        f'%{query}%',
        query,
        query,
        f'%{query}%',
        f'%{query}%',
        f'%{query}%'
    ))
    
    results = cur.fetchall()
    conn.close()
    return results


def interactive_lookup():
    """Interactive lookup mode."""
    print("Key Registry Lookup (Ctrl+C to exit)")
    print("-" * 40)
    while True:
        try:
            query = input("\nSearch: ").strip()
            if not query:
                continue
            results = lookup_entity(query)
            if not results:
                print("  No matches.")
            else:
                for row in results:
                    print(f"\n  Entity: {row['entity_name']}")
                    if row['uei']: print(f"  UEI: {row['uei']}")
                    if row['ein']: print(f"  EIN: {row['ein']}")
                    if row['assistance_listing']: print(f"  AL: {row['assistance_listing']}")
                    if row['state_fund_code']: print(f"  State Codes: {row['state_fund_code']}")
                    if row['aka_names']: print(f"  AKA: {row['aka_names']}")
                    print(f"  Status: {row['status']}")
        except KeyboardInterrupt:
            print("\n\nExiting.")
            break


def show_stats():
    """Show registry statistics."""
    conn = sqlite3.connect(DB_PATH)
    
    total = conn.execute("SELECT COUNT(*) FROM key_registry").fetchone()[0]
    active = conn.execute("SELECT COUNT(*) FROM key_registry WHERE status='active'").fetchone()[0]
    with_uei = conn.execute("SELECT COUNT(*) FROM key_registry WHERE uei IS NOT NULL").fetchone()[0]
    with_ein = conn.execute("SELECT COUNT(*) FROM key_registry WHERE ein IS NOT NULL").fetchone()[0]
    with_al = conn.execute("SELECT COUNT(*) FROM key_registry WHERE assistance_listing IS NOT NULL").fetchone()[0]
    with_state = conn.execute("SELECT COUNT(*) FROM key_registry WHERE state_fund_code IS NOT NULL").fetchone()[0]
    
    print("\nKey Registry Stats")
    print("=" * 30)
    print(f"Total entities:     {total}")
    print(f"Active:             {active}")
    print(f"With UEI:           {with_uei}")
    print(f"With EIN:           {with_ein}")
    print(f"With AL/CFDA:       {with_al}")
    print(f"With State Codes:   {with_state}")
    
    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Key Registry Manager")
    parser.add_argument("command", choices=["sync", "lookup", "stats"], 
                        help="Command to run")
    args = parser.parse_args()
    
    if args.command == "sync":
        sync_yaml_to_db()
    elif args.command == "lookup":
        interactive_lookup()
    elif args.command == "stats":
        show_stats()


if __name__ == "__main__":
    main()
