# Single Artifact Batch Cycling — Agent Mode Instructions

**Method:** Take one anchor artifact and exhaust ALL possible related artifacts in a single batch.

Unlike Composite Schema Cycling (which rotates through 4 turns with one artifact per slot), this method asks the LLM to generate **as many artifacts as it can find** from one anchor.

---

## How It Works

1. Start with an anchor artifact (e.g., a statute)
2. LLM researches and generates ALL related artifacts:
   - Multiple money_flows (every appropriation tied to this statute)
   - Multiple evidence_items (every budget document, audit, report)
   - Multiple field_validations (every compliance check)
   - Multiple authority_references (every related statute/rule)
3. Return everything as a batch
4. Save to `_batched_turns/BATCH-{anchor_id}/`

---

## Current Batch

**Anchor:** AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND  
**Citation:** Arkansas Code Annotated §19-5-1144  
**Administering Body:** Arkansas Administrative Office of the Courts (AOC)  
**Governs:** AR_FY2026_AOC_SPECIALTY_COURT_JUVENILE_DRUG_PROGRAMS_STATE_FUNDS_ACT776_SEC31

---

## Your Task

Research Arkansas Code §19-5-1144 (Accountability Court Fund) and related appropriations thoroughly. Generate ALL artifacts you can find:

### Generate Multiple money_flow Artifacts
Find every appropriation that flows through or is governed by this statute:
- FY2026 specialty court funding
- Juvenile drug court programs
- Adult drug court programs
- DWI courts
- Veterans courts
- Any other accountability court funding

### Generate Multiple evidence_item Artifacts
Find every supporting document:
- Act 776 of 2025 (relevant sections)
- AOC budget documents
- Legislative audit reports
- Grant awards
- Program reports

### Generate Multiple authority_reference Artifacts
Find related statutes and rules:
- Other sections of ACA Title 19 Chapter 5
- ACA Title 16 (Courts)
- Administrative rules governing specialty courts
- Federal grant requirements (if applicable)

### Generate Multiple field_validation Artifacts
Document validation sources:
- Legislative audit findings
- AOC annual reports
- Federal compliance reports

---

## Output Format

Return a JSON array of artifacts:

```json
{
  "batch_id": "BATCH-AUTH-AR-ACA-19-5-1144",
  "anchor_id": "AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND",
  "generated_at": "2026-02-05",
  "artifacts": {
    "money_flow": [
      { "flow_id": "MF-AR-...", ... },
      { "flow_id": "MF-AR-...", ... },
      ...
    ],
    "authority_reference": [
      { "authority_id": "AUTH-AR-...", ... },
      ...
    ],
    "evidence_item": [
      { "evidence_id": "EVID-AR-...", ... },
      ...
    ],
    "field_validation": [
      { "fv_id": "FV-AR-...", ... },
      ...
    ]
  },
  "research_notes": "Optional notes about sources consulted"
}
```

---

## Save Location

Save your batch response to:
```
C:\Threshold\cleanroom\artifacts\validated\_batched_turns\BATCH-AUTH-AR-ACA-19-5-1144\batch_response.json
```

---

## Schema Reference

### money_flow
```json
{
  "flow_id": "MF-AR-...",
  "source": "funding source entity",
  "intermediary": "pass-through or None",
  "destination": "receiving entity",
  "amount": 0,
  "fund_type": "state|federal",
  "fiscal_year": "2026",
  "restrictions": { "medicaid": false, "dhs_controlled": false },
  "statutory_basis": "legal citation",
  "editor_status": "pending"
}
```

### authority_reference
```json
{
  "authority_id": "AUTH-AR-...",
  "authority_type": "statute|regulation|policy",
  "citation": "formal citation",
  "administering_body": "agency name",
  "governs": ["what this governs"],
  "effects": { "access_limiting": false, "appeal_mechanism": false },
  "editor_status": "pending"
}
```

### evidence_item
```json
{
  "evidence_id": "EVID-AR-...",
  "section": "related flow or authority ID",
  "claim_summary": "what this evidence proves",
  "evidence_type": "budget|audit|policy",
  "source": { "title": "doc title", "issuing_body": "issuer", "url": "URL" },
  "confidence_level": "high|medium|low",
  "editor_status": "pending"
}
```

### field_validation
```json
{
  "fv_id": "FV-AR-...",
  "jurisdiction": "Arkansas",
  "validating_entity": "auditor/validator",
  "alignment_status": "captured|open|mixed",
  "evidence_basis": ["supporting artifact IDs"],
  "disclosure_level": "public|restricted",
  "editor_status": "pending"
}
```

---

## Rules

- Generate as MANY artifacts as you can find with real data
- Use actual Arkansas statute citations, appropriation amounts, URLs
- Every artifact gets `editor_status: "pending"`
- Unique IDs for each artifact
- Don't skip anything — exhaustive is the goal
