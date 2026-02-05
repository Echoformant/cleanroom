#!/usr/bin/env python3
"""
Artifact Linkage Analyzer for Arkansas Public-Finance Validated Artifacts

Discovers and displays relationships between artifacts across:
- money_flow/
- authority_reference/
- evidence_item/
- field_validation/

Usage:
  python linkage_analyzer.py                     # Show all linkages by volume
  python linkage_analyzer.py --artifact <ID>     # Show links for specific artifact
  python linkage_analyzer.py --category <TYPE>   # Show links for category (money_flow, authority_reference, etc.)
  python linkage_analyzer.py --export-db         # Export to SQLite database
  python linkage_analyzer.py --export-json       # Export to JSON graph format
"""

import json
import os
import re
import argparse
import sqlite3
from datetime import datetime
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

# Base directory (script location -> parent)
BASE_DIR = Path(__file__).resolve().parent.parent


def load_artifacts() -> Dict[str, dict]:
    """Load all artifacts from the repository into a dict keyed by ID."""
    artifacts = {}
    categories = ["money_flow", "authority_reference", "evidence_item", "field_validation"]
    
    for category in categories:
        cat_path = BASE_DIR / category
        if not cat_path.exists():
            continue
            
        for item in cat_path.iterdir():
            # Skip .github and batch folders for now
            if item.name.startswith(".") or "batch" in item.name.lower():
                continue
                
            artifact = None
            artifact_id = None
            
            if item.is_file() and item.suffix == ".json":
                # Root-level pretty-printed JSON
                try:
                    with open(item, "r", encoding="utf-8") as f:
                        artifact = json.load(f)
                except (json.JSONDecodeError, IOError):
                    continue
            elif item.is_dir() and (item.name.endswith(".yaml") or item.name.endswith(".json")):
                # Folder with 0.json inside
                inner = item / "0.json"
                if inner.exists():
                    try:
                        with open(inner, "r", encoding="utf-8") as f:
                            artifact = json.load(f)
                    except (json.JSONDecodeError, IOError):
                        continue
            
            if artifact:
                # Extract ID based on category
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


def extract_references(text: str, all_ids: Set[str]) -> Set[str]:
    """Extract artifact IDs mentioned in a text field."""
    if not text:
        return set()
    
    found = set()
    for artifact_id in all_ids:
        if artifact_id in text:
            found.add(artifact_id)
    
    # Also look for partial matches (e.g., Act 776 -> ACT776)
    # Extract act numbers
    act_pattern = r"Act\s*(\d+)"
    for match in re.finditer(act_pattern, text, re.IGNORECASE):
        act_num = match.group(1)
        for artifact_id in all_ids:
            if f"ACT{act_num}" in artifact_id.upper():
                found.add(artifact_id)
    
    # Extract ACA section references
    aca_pattern = r"§?\s*(\d+-\d+-\d+)"
    for match in re.finditer(aca_pattern, text):
        section = match.group(1)
        for artifact_id in all_ids:
            if section in artifact_id:
                found.add(artifact_id)
    
    return found


def build_linkage_graph(artifacts: Dict[str, dict]) -> Dict[str, List[Tuple[str, str]]]:
    """
    Build a graph of linkages between artifacts.
    Returns: {artifact_id: [(linked_id, relationship_type), ...]}
    """
    all_ids = set(artifacts.keys())
    links = defaultdict(list)
    
    for artifact_id, info in artifacts.items():
        data = info["data"]
        category = info["category"]
        
        # Evidence items link via 'section' field to money flows
        if category == "evidence_item":
            section = data.get("section", "")
            refs = extract_references(section, all_ids)
            for ref in refs:
                if ref != artifact_id:
                    links[artifact_id].append((ref, "section→flow"))
                    links[ref].append((artifact_id, "flow←evidence"))
        
        # Field validations link via 'evidence_basis' array
        if category == "field_validation":
            evidence_basis = data.get("evidence_basis", [])
            for basis in evidence_basis:
                refs = extract_references(basis, all_ids)
                for ref in refs:
                    if ref != artifact_id:
                        links[artifact_id].append((ref, "evidence_basis→"))
                        links[ref].append((artifact_id, "←field_validation"))
        
        # Authority references link via 'governs' array
        if category == "authority_reference":
            governs = data.get("governs", [])
            for gov in governs:
                refs = extract_references(gov, all_ids)
                for ref in refs:
                    if ref != artifact_id:
                        links[artifact_id].append((ref, "governs→"))
                        links[ref].append((artifact_id, "←authority"))
        
        # Money flows link via 'statutory_basis' to authorities
        if category == "money_flow":
            statutory = data.get("statutory_basis", "")
            refs = extract_references(statutory, all_ids)
            for ref in refs:
                if ref != artifact_id:
                    links[artifact_id].append((ref, "statutory_basis→"))
                    links[ref].append((artifact_id, "←money_flow"))
        
        # Check citation field in authorities
        if category == "authority_reference":
            citation = data.get("citation", "")
            refs = extract_references(citation, all_ids)
            for ref in refs:
                if ref != artifact_id:
                    links[artifact_id].append((ref, "citation→"))
                    links[ref].append((artifact_id, "←citation"))
    
    # Deduplicate links
    for artifact_id in links:
        links[artifact_id] = list(set(links[artifact_id]))
    
    return dict(links)


def print_artifact_links(artifact_id: str, artifacts: Dict[str, dict], links: Dict[str, List[Tuple[str, str]]]):
    """Print all links for a specific artifact."""
    if artifact_id not in artifacts:
        print(f"❌ Artifact '{artifact_id}' not found.")
        print(f"   Hint: Try partial match search...")
        matches = [aid for aid in artifacts.keys() if artifact_id.lower() in aid.lower()]
        if matches:
            print(f"   Possible matches: {matches[:5]}")
        return
    
    info = artifacts[artifact_id]
    print(f"\n{'='*80}")
    print(f"📄 {artifact_id}")
    print(f"   Category: {info['category']}")
    print(f"   Path: {info['path']}")
    print(f"{'='*80}")
    
    artifact_links = links.get(artifact_id, [])
    if not artifact_links:
        print("   No linkages found.")
        return
    
    print(f"\n   🔗 Linkages ({len(artifact_links)} total):\n")
    
    # Group by relationship type
    by_type = defaultdict(list)
    for linked_id, rel_type in artifact_links:
        by_type[rel_type].append(linked_id)
    
    for rel_type, linked_ids in sorted(by_type.items()):
        print(f"   [{rel_type}]")
        for lid in sorted(linked_ids):
            cat = artifacts.get(lid, {}).get("category", "unknown")
            print(f"      → {lid} ({cat})")
        print()


def print_category_links(category: str, artifacts: Dict[str, dict], links: Dict[str, List[Tuple[str, str]]]):
    """Print all links for artifacts in a specific category."""
    category_ids = [aid for aid, info in artifacts.items() if info["category"] == category]
    
    if not category_ids:
        print(f"❌ No artifacts found in category '{category}'")
        print(f"   Available categories: money_flow, authority_reference, evidence_item, field_validation")
        return
    
    print(f"\n{'='*80}")
    print(f"📁 Category: {category} ({len(category_ids)} artifacts)")
    print(f"{'='*80}\n")
    
    # Collect all external links
    external_links = defaultdict(list)
    for artifact_id in category_ids:
        for linked_id, rel_type in links.get(artifact_id, []):
            if artifacts.get(linked_id, {}).get("category") != category:
                external_links[artifact_id].append((linked_id, rel_type))
    
    # Sort by number of external links
    sorted_ids = sorted(external_links.keys(), key=lambda x: len(external_links[x]), reverse=True)
    
    for artifact_id in sorted_ids[:20]:  # Top 20
        ext_links = external_links[artifact_id]
        print(f"📄 {artifact_id} ({len(ext_links)} external links)")
        for linked_id, rel_type in ext_links[:5]:
            cat = artifacts.get(linked_id, {}).get("category", "?")
            print(f"   {rel_type} {linked_id} ({cat})")
        if len(ext_links) > 5:
            print(f"   ... and {len(ext_links) - 5} more")
        print()


def print_volume_ranking(artifacts: Dict[str, dict], links: Dict[str, List[Tuple[str, str]]]):
    """Print artifacts ranked by number of linkages (descending)."""
    print(f"\n{'='*80}")
    print(f"📊 Linkage Volume Ranking (Top 30)")
    print(f"{'='*80}\n")
    
    # Count links per artifact
    link_counts = [(aid, len(links.get(aid, []))) for aid in artifacts.keys()]
    link_counts.sort(key=lambda x: x[1], reverse=True)
    
    # Print top 30
    for i, (artifact_id, count) in enumerate(link_counts[:30], 1):
        if count == 0:
            break
        cat = artifacts[artifact_id]["category"]
        print(f"{i:3}. [{count:3} links] {artifact_id}")
        print(f"      Category: {cat}")
        
        # Show sample links
        sample_links = links.get(artifact_id, [])[:3]
        for linked_id, rel_type in sample_links:
            print(f"      {rel_type} {linked_id}")
        print()


def print_summary(artifacts: Dict[str, dict], links: Dict[str, List[Tuple[str, str]]]):
    """Print a summary of all discovered linkages."""
    print(f"\n{'='*80}")
    print(f"📈 Linkage Summary")
    print(f"{'='*80}\n")
    
    # Count by category
    by_cat = defaultdict(int)
    for info in artifacts.values():
        by_cat[info["category"]] += 1
    
    print("Artifacts by category:")
    for cat, count in sorted(by_cat.items()):
        linked_count = sum(1 for aid, info in artifacts.items() 
                         if info["category"] == cat and links.get(aid))
        print(f"  {cat}: {count} total, {linked_count} with links")
    
    # Total unique links
    total_links = sum(len(v) for v in links.values()) // 2  # Divide by 2 for bidirectional
    print(f"\nTotal unique linkages: {total_links}")
    
    # Artifacts with no links
    no_links = [aid for aid in artifacts if not links.get(aid)]
    print(f"Artifacts with no links: {len(no_links)}")


def export_to_sqlite(artifacts: Dict[str, dict], links: Dict[str, List[Tuple[str, str]]]):
    """Export the artifact graph to SQLite database."""
    data_dir = BASE_DIR / "_data"
    data_dir.mkdir(exist_ok=True)
    db_path = data_dir / "artifacts_graph.db"
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            total_nodes INTEGER,
            total_edges INTEGER,
            orphan_count INTEGER
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nodes (
            id TEXT PRIMARY KEY,
            category TEXT NOT NULL,
            label TEXT,
            path TEXT,
            data JSON,
            first_seen TEXT,
            last_seen TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS edges (
            source TEXT NOT NULL,
            target TEXT NOT NULL,
            relationship TEXT NOT NULL,
            first_seen TEXT,
            last_seen TEXT,
            PRIMARY KEY (source, target, relationship),
            FOREIGN KEY (source) REFERENCES nodes(id),
            FOREIGN KEY (target) REFERENCES nodes(id)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS node_run_history (
            run_id INTEGER,
            node_id TEXT,
            link_count INTEGER,
            FOREIGN KEY (run_id) REFERENCES runs(run_id),
            FOREIGN KEY (node_id) REFERENCES nodes(id)
        )
    """)
    
    # Insert run record
    timestamp = datetime.now().isoformat()
    orphan_count = sum(1 for aid in artifacts if not links.get(aid))
    total_edges = sum(len(v) for v in links.values()) // 2
    
    cursor.execute("""
        INSERT INTO runs (timestamp, total_nodes, total_edges, orphan_count)
        VALUES (?, ?, ?, ?)
    """, (timestamp, len(artifacts), total_edges, orphan_count))
    run_id = cursor.lastrowid
    
    # Upsert nodes
    for artifact_id, info in artifacts.items():
        # Generate a short label
        label = artifact_id[:50] + "..." if len(artifact_id) > 50 else artifact_id
        
        cursor.execute("""
            INSERT INTO nodes (id, category, label, path, data, first_seen, last_seen)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                last_seen = excluded.last_seen,
                data = excluded.data,
                path = excluded.path
        """, (
            artifact_id,
            info["category"],
            label,
            info["path"],
            json.dumps(info["data"]),
            timestamp,
            timestamp
        ))
        
        # Record link count for this run
        link_count = len(links.get(artifact_id, []))
        cursor.execute("""
            INSERT INTO node_run_history (run_id, node_id, link_count)
            VALUES (?, ?, ?)
        """, (run_id, artifact_id, link_count))
    
    # Upsert edges (only one direction to avoid duplicates)
    seen_edges = set()
    for artifact_id, link_list in links.items():
        for linked_id, rel_type in link_list:
            # Normalize edge direction (smaller ID first)
            edge_key = tuple(sorted([artifact_id, linked_id])) + (rel_type,)
            if edge_key in seen_edges:
                continue
            seen_edges.add(edge_key)
            
            cursor.execute("""
                INSERT INTO edges (source, target, relationship, first_seen, last_seen)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(source, target, relationship) DO UPDATE SET
                    last_seen = excluded.last_seen
            """, (artifact_id, linked_id, rel_type, timestamp, timestamp))
    
    conn.commit()
    conn.close()
    
    print(f"\n✅ Exported to SQLite: {db_path}")
    print(f"   Run ID: {run_id}")
    print(f"   Nodes: {len(artifacts)}")
    print(f"   Edges: {total_edges}")
    print(f"   Orphans: {orphan_count}")


def export_to_json(artifacts: Dict[str, dict], links: Dict[str, List[Tuple[str, str]]]):
    """Export the artifact graph to JSON format for visualization."""
    data_dir = BASE_DIR / "_data"
    data_dir.mkdir(exist_ok=True)
    json_path = data_dir / "artifacts_graph.json"
    
    # Build nodes array
    nodes = []
    for artifact_id, info in artifacts.items():
        link_count = len(links.get(artifact_id, []))
        nodes.append({
            "id": artifact_id,
            "category": info["category"],
            "label": artifact_id[:40] + "..." if len(artifact_id) > 40 else artifact_id,
            "link_count": link_count,
            "is_orphan": link_count == 0
        })
    
    # Build edges array (deduplicated, one direction per relationship)
    edges = []
    seen_edges = set()
    for artifact_id, link_list in links.items():
        for linked_id, rel_type in link_list:
            # Normalize: always source < target alphabetically for consistency
            if artifact_id < linked_id:
                src, tgt = artifact_id, linked_id
            else:
                src, tgt = linked_id, artifact_id
            
            edge_key = (src, tgt, rel_type)
            if edge_key in seen_edges:
                continue
            seen_edges.add(edge_key)
            
            edges.append({
                "source": src,
                "target": tgt,
                "type": rel_type
            })
    
    # Build category stats
    category_stats = defaultdict(lambda: {"total": 0, "linked": 0, "orphan": 0})
    for artifact_id, info in artifacts.items():
        cat = info["category"]
        category_stats[cat]["total"] += 1
        if links.get(artifact_id):
            category_stats[cat]["linked"] += 1
        else:
            category_stats[cat]["orphan"] += 1
    
    # Assemble output
    output = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "orphan_count": sum(1 for n in nodes if n["is_orphan"]),
            "category_stats": dict(category_stats)
        },
        "nodes": nodes,
        "edges": edges
    }
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    
    print(f"\n✅ Exported to JSON: {json_path}")
    print(f"   Nodes: {len(nodes)}")
    print(f"   Edges: {len(edges)}")
    print(f"   Orphans: {output['metadata']['orphan_count']}")


def main():
    parser = argparse.ArgumentParser(description="Analyze artifact linkages")
    parser.add_argument("--artifact", "-a", help="Show links for specific artifact ID")
    parser.add_argument("--category", "-c", help="Show links for category")
    parser.add_argument("--summary", "-s", action="store_true", help="Show summary only")
    parser.add_argument("--export-db", action="store_true", help="Export to SQLite database (_data/artifacts_graph.db)")
    parser.add_argument("--export-json", action="store_true", help="Export to JSON graph (_data/artifacts_graph.json)")
    parser.add_argument("--export-all", action="store_true", help="Export to both SQLite and JSON")
    args = parser.parse_args()
    
    print("Loading artifacts...")
    artifacts = load_artifacts()
    print(f"Loaded {len(artifacts)} artifacts")
    
    print("Building linkage graph...")
    links = build_linkage_graph(artifacts)
    linked_count = sum(1 for v in links.values() if v)
    print(f"Found {linked_count} artifacts with linkages")
    
    if args.export_db or args.export_all:
        export_to_sqlite(artifacts, links)
    
    if args.export_json or args.export_all:
        export_to_json(artifacts, links)
    
    if args.export_db or args.export_json or args.export_all:
        # Just do exports, skip display
        if not (args.artifact or args.category or args.summary):
            return
    
    if args.artifact:
        print_artifact_links(args.artifact, artifacts, links)
    elif args.category:
        print_category_links(args.category, artifacts, links)
    elif args.summary:
        print_summary(artifacts, links)
    else:
        print_summary(artifacts, links)
        print_volume_ranking(artifacts, links)


if __name__ == "__main__":
    main()
