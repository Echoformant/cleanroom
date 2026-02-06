#!/usr/bin/env python3
"""Find orphan artifacts for cycling priority."""
import json
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent.parent
data = json.load(open(BASE / '_data/artifacts_graph.json', encoding='utf-8'))
nodes = data['nodes']

orphans = [n for n in nodes if n['is_orphan']]
print(f'Total orphans: {len(orphans)}')
print()
print('ORPHANS BY CATEGORY:')
cats = Counter(n['category'] for n in orphans)
for cat, count in cats.most_common():
    print(f'  {cat}: {count}')
print()
print('ORPHAN ARTIFACTS:')
for n in sorted(orphans, key=lambda x: x['category']):
    print(f'  [{n["category"][:12]:12}] {n["id"][:55]}')
