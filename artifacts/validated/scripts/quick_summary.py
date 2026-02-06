#!/usr/bin/env python3
"""Quick summary report for NAMI Arkansas leadership."""
import json
import sys
from pathlib import Path

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE = Path(__file__).parent.parent
data = json.load(open(BASE / '_data/artifacts_graph.json', encoding='utf-8'))
nodes = data['nodes']

mf = [n for n in nodes if n['category'] == 'money_flow']
auth = [n for n in nodes if n['category'] == 'authority_reference']
evid = [n for n in nodes if n['category'] == 'evidence_item']
fv = [n for n in nodes if n['category'] == 'field_validation']

total = sum(n.get('data',{}).get('amount',0) for n in mf if n.get('data',{}).get('amount'))

print('='*65)
print('   OPERATION NAMI CLEARLANE - ARTIFACT SUMMARY')
print('   Arkansas Public Finance Validated Dossier')
print('   Generated: February 5, 2026')
print('='*65)
print()
print(f'   Total Validated Artifacts:  {len(nodes):,}')
print(f'   +-- Money Flows:            {len(mf)}')
print(f'   +-- Legal Authorities:      {len(auth)}')
print(f'   +-- Evidence Items:         {len(evid)}')
print(f'   +-- Field Validations:      {len(fv)}')
print()
print(f'   Total Cross-References:     {len(data["edges"]):,}')
print(f'   Tracked State/Federal:      ${total:,}')
print()
print('='*65)
print('   TOP 10 MONEY FLOWS BY AMOUNT')
print('='*65)
for i, n in enumerate(sorted(mf, key=lambda x: x.get('data',{}).get('amount',0), reverse=True)[:10], 1):
    d = n.get('data',{})
    amt = d.get('amount', 0)
    dest = d.get('destination', 'Unknown')[:45]
    fy = d.get('fiscal_year', '')
    print(f'   {i:2}. ${amt:>12,}  -> {dest}')
print()
print('='*65)
print('   KEY LEGAL AUTHORITIES')
print('='*65)
for n in auth[:8]:
    d = n.get('data', {})
    cite = d.get('citation', n['id'])
    body = d.get('administering_body', '')[:40]
    print(f'   * {cite}')
    if body:
        print(f'     ({body})')
print()
print('='*65)
print('   This dossier tracks Arkansas appropriations, specialty court')
print('   funding, DHS behavioral health flows, and audit findings.')
print('   All artifacts are law-anchored with statutory citations.')
print('='*65)
