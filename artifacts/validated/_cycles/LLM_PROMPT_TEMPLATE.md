# Composite Schema Cycling — LLM Prompt Template

Copy this template and paste the contents of `turn_N_prompt.json` where indicated.

---

## System Context

You are an artifact extraction assistant for Operation NAMI Clearlane / VECTOR 1. Your task is to generate schema-valid artifacts based on an anchor artifact.

**Rules:**
- Output ONLY valid JSON matching the schemas below
- Set `editor_status` to `"pending"` for all generated artifacts
- Do NOT add fields not in the schema
- Do NOT add commentary or explanation outside the JSON
- If you cannot determine a field value from the anchor, use `"[UNKNOWN - requires research]"`
- Do NOT reuse any artifact IDs listed in `used_artifacts`

**ID Naming Conventions:**
- `money_flow`: Start with `MF-AR-` or `AR_FY20XX_`
- `authority_reference`: Start with `AUTH-AR-` or `AR-AUTH-`
- `evidence_item`: Start with `EVID-AR-` or `EV-AR-`
- `field_validation`: Start with `FV-AR-`

---

## Anchor Artifact

The anchor is a validated artifact. Use it to infer what related artifacts should exist in the other three categories.

---

## Your Task

Given the composite schema below, fill each slot's template with a plausible artifact that would logically relate to the anchor.

**Paste the contents of `turn_N_prompt.json` here:**

```json
[PASTE turn_N_prompt.json CONTENTS HERE]
```

---

## Expected Output Format

Return a JSON object with this structure:

```json
{
  "money_flow": {
    "flow_id": "MF-AR-...",
    "source": "...",
    "intermediary": "...",
    "destination": "...",
    "amount": 0,
    "fund_type": "state",
    "fiscal_year": "2026",
    "restrictions": {
      "medicaid": false,
      "dhs_controlled": false
    },
    "statutory_basis": "...",
    "editor_status": "pending"
  },
  "evidence_item": {
    "evidence_id": "EVID-AR-...",
    "section": "...",
    "claim_summary": "...",
    "evidence_type": "budget",
    "source": {
      "title": "...",
      "url": "...",
      "retrieval_date": "2026-02-04"
    },
    "confidence_level": "medium",
    "editor_status": "pending"
  },
  "field_validation": {
    "fv_id": "FV-AR-...",
    "jurisdiction": "Arkansas",
    "validating_entity": "...",
    "alignment_status": "open",
    "evidence_basis": [],
    "disclosure_level": "public",
    "editor_status": "pending"
  }
}
```

Only include the three slots you're filling (exclude the anchor category from your response).

---

## Schema Reference

### money_flow
| Field | Type | Notes |
|-------|------|-------|
| flow_id | string | Unique ID |
| source | string | Funding source entity |
| intermediary | string | Pass-through or "None" |
| destination | string | Receiving entity |
| amount | number | USD integer, 0 if unknown |
| fund_type | enum | "state", "federal", "settlement" |
| fiscal_year | string | "2026" or "2025-2026" |
| restrictions.medicaid | boolean | Medicaid-reimbursable? |
| restrictions.dhs_controlled | boolean | DHS-disbursed? |
| statutory_basis | string | Legal authority citation |
| editor_status | enum | Always "pending" |

### evidence_item
| Field | Type | Notes |
|-------|------|-------|
| evidence_id | string | Unique ID |
| section | string | Related flow/authority ID |
| claim_summary | string | What the evidence proves |
| evidence_type | enum | "budget", "audit", "policy" |
| source.title | string | Document name |
| source.url | string | Official AR.gov URL |
| source.retrieval_date | string | ISO date |
| confidence_level | enum | "high", "medium", "low" |
| editor_status | enum | Always "pending" |

### field_validation
| Field | Type | Notes |
|-------|------|-------|
| fv_id | string | Unique ID |
| jurisdiction | string | Always "Arkansas" |
| validating_entity | string | Auditor/validator name |
| alignment_status | enum | "captured", "open", "mixed" |
| evidence_basis | array | IDs of supporting evidence |
| disclosure_level | enum | "public", "restricted" |
| editor_status | enum | Always "pending" |

### authority_reference
| Field | Type | Notes |
|-------|------|-------|
| authority_id | string | Unique ID |
| authority_type | enum | "statute", "regulation", "policy" |
| citation | string | Full legal citation |
| administering_body | string | Agency name |
| governs | array | IDs this authority governs |
| effects.access_limiting | boolean | Limits access? |
| effects.appeal_mechanism | boolean | Has appeal process? |
| editor_status | enum | Always "pending" |
