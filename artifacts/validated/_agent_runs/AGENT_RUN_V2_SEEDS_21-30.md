# Agent Run: Exhaustive Cycling — Seeds 21-30

**Operation:** NAMI Clearlane / VECTOR 1  
**Mode:** Exhaustive Schema Cycling  
**Batch:** Seeds 21-30 (of 30)

## Mission

Continue exhaustive schema cycling from the anchor artifacts below. For each anchor, generate the three complementary artifact types. Output a single JSON array ready for `batch_ingest.py`.

## Critical Rules

1. **DO NOT RETURN A PARTIAL BATCH** — Complete all 10 seeds before returning
2. **DO NOT queue evidence or field_validation as anchors** — Only use existing authorities/money_flows as anchors
3. **One JSON array output** — All artifacts in one array
4. **Use canonical schemas exactly** — See schemas below

## Anchor Artifacts (Seeds 21-30)

For each anchor, generate 3 artifacts (the types it's missing):

| # | Anchor ID | Type | Generate |
|---|-----------|------|----------|
| 21 | AUTH-AR-CONST-ART16-SEC3 | authority | money_flow, evidence, field_validation |
| 22 | AUTH-AR-CONST-ART16-SEC12 | authority | money_flow, evidence, field_validation |
| 23 | AUTH-AR-CONSTITUTION-ART16-SEC11 | authority | money_flow, evidence, field_validation |
| 24 | AUTH-AR-CONSTITUTION-ART16-SEC13 | authority | money_flow, evidence, field_validation |
| 25 | MF-AR-HIGHWAY-FUND-ARDOT-FY2026 | money_flow | authority, evidence, field_validation |
| 26 | MF-AR-HIGHWAY-REVENUE-DISTRIBUTION-COUNTIES-FY2026 | money_flow | authority, evidence, field_validation |
| 27 | MF-AR-COUNTY-AID-FUND-DISTRIBUTION-FY2026 | money_flow | authority, evidence, field_validation |
| 28 | MF-AR-COURT-FINES-TO-JUSTICE-FUND-FY2026 | money_flow | authority, evidence, field_validation |
| 29 | AUTH-AR-PASSE-PROGRAM | authority | money_flow, evidence, field_validation |
| 30 | AUTH-AR-1115-WAIVER-ARHOME | authority | money_flow, evidence, field_validation |

## Canonical Schemas

### Money Flow (`MF-*`)
```json
{
  "flow_id": "MF-AR-{DESCRIPTIVE-NAME}-FY2026",
  "source": "Entity providing funds",
  "intermediary": "Pass-through entity or 'None'",
  "destination": "Entity receiving funds",
  "amount": 0,
  "fund_type": "state|federal",
  "fiscal_year": "FY2026",
  "restrictions": {
    "medicaid": false,
    "dhs_controlled": false
  },
  "statutory_basis": "Human-readable citation text",
  "statutory_basis_refs": ["AUTH-...", "EVID-..."],
  "editor_status": "pending"
}
```

### Authority Reference (`AUTH-*`)
```json
{
  "authority_id": "AUTH-AR-{CODE-SECTION}",
  "authority_type": "statute|regulation|act|administrative|court_order|mou|settlement",
  "citation": "Ark. Code § X-X-XXX",
  "administering_body": "Agency/entity with authority",
  "governs": ["MF-AR-...", "MF-AR-..."],
  "effects": "What this authority enables or restricts",
  "editor_status": "pending"
}
```

### Evidence Item (`EVID-*`)
```json
{
  "evidence_id": "EVID-AR-{SOURCE}-{SECTION}-{TOPIC}",
  "section": "MF-AR-... or AUTH-AR-...",
  "claim_summary": "What this evidence proves",
  "evidence_type": "budget|audit|policy",
  "source": {
    "document": "Document title",
    "url": "https://...",
    "retrieved": "2026-02-06"
  },
  "confidence_level": "high|medium|low",
  "editor_status": "pending"
}
```

### Field Validation (`FV-*`)
```json
{
  "fv_id": "FV-AR-{VALIDATOR}-{SUBJECT}-{YEAR}",
  "jurisdiction": "Arkansas",
  "validating_entity": "Legislative Audit | DFA | CMS | etc.",
  "alignment_status": "captured|open|mixed",
  "evidence_basis": ["EVID-...", "AUTH-..."],
  "disclosure_level": "public|limited|confidential",
  "editor_status": "pending"
}
```

## Output Format

Return a single JSON array:
```json
[
  { "flow_id": "MF-AR-...", ... },
  { "authority_id": "AUTH-AR-...", ... },
  { "evidence_id": "EVID-AR-...", ... },
  { "fv_id": "FV-AR-...", ... },
  ...
]
```

## After Completion

Save output to: `_agent_runs/batch_v2_seeds_21-30.json`

Then run:
```powershell
python scripts/batch_ingest.py _agent_runs/batch_v2_seeds_21-30.json
python scripts/linkage_analyzer.py --summary
```
