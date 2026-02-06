# AGENT_RUN: Exhaustive 4-Turn Schema Cycle
## Anchor: AR-AUTH-25-10-129 (DHS Federal Fund Conformity)

**Mode:** GPT Agent  
**Expected Output:** 40-60 artifacts across all 4 categories  

---

## INSTRUCTIONS

You are a legal-financial research agent for Operation NAMI Clearlane. Your task is to perform an **exhaustive 4-turn schema cycle** starting from the anchor authority below.

Research Arkansas public finance law, appropriations, and audit records. Generate validated artifacts that link together into a coherent graph.

---

## CANONICAL SCHEMA DEFINITIONS

### money_flow

Tracks money moving between government entities.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `flow_id` | string | ✓ | Unique ID. Pattern: `MF-AR-*` or `MF-US-*` |
| `source` | string | ✓ | Entity providing funds |
| `intermediary` | string | ✓ | Pass-through entity, or `"None"` if direct |
| `destination` | string | ✓ | Entity receiving funds |
| `amount` | integer | ✓ | USD amount (no commas/decimals). Use `0` if variable, explain in statutory_basis |
| `fund_type` | enum | ✓ | `"state"` \| `"federal"` \| `"settlement"` |
| `fiscal_year` | string | ✓ | `"2026"` or `"2025-2026"` for biennia |
| `restrictions.medicaid` | boolean | ✓ | True only if Medicaid-reimbursable destination |
| `restrictions.dhs_controlled` | boolean | ✓ | True if DHS disburses |
| `statutory_basis` | string | ✓ | Citation to authorizing law or appropriation |
| `editor_status` | enum | ✓ | `"pending"` for new artifacts |

**Example:**
```json
{
  "flow_id": "MF-AR-DHS-FEDERAL-MATCH-FY2026",
  "source": "U.S. Department of Health and Human Services",
  "intermediary": "None",
  "destination": "Arkansas Department of Human Services",
  "amount": 148000000,
  "fund_type": "federal",
  "fiscal_year": "2026",
  "restrictions": {
    "medicaid": true,
    "dhs_controlled": true
  },
  "statutory_basis": "Ark. Code Ann. § 25-10-129(b); 42 CFR § 433.10",
  "editor_status": "pending"
}
```

---

### authority_reference

Statutes, rules, and acts that authorize fund use.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `authority_id` | string | ✓ | Unique ID. Pattern: `AUTH-AR-*` or `AUTH-US-*` |
| `authority_type` | enum | ✓ | `"statute"` \| `"regulation"` \| `"act"` |
| `citation` | string | ✓ | Full legal citation. Preserve § symbols and dashes |
| `administering_body` | string | ✓ | Agency responsible for implementation |
| `governs` | array[string] | ✓ | What this authority controls. May include flow IDs |
| `effects.access_limiting` | boolean | ✓ | True if restricts access to services |
| `effects.appeal_mechanism` | boolean | ✓ | True if provides appeal rights |
| `editor_status` | enum | ✓ | `"pending"` for new artifacts |

**Example:**
```json
{
  "authority_id": "AUTH-AR-ACA-25-10-129",
  "authority_type": "statute",
  "citation": "Ark. Code Ann. § 25-10-129(b)",
  "administering_body": "Arkansas Department of Human Services (DHS)",
  "governs": [
    "DHS authority to promulgate rules for federal fund conformity",
    "Federal matching fund requirements",
    "MF-AR-DHS-FEDERAL-MATCH-FY2026"
  ],
  "effects": {
    "access_limiting": false,
    "appeal_mechanism": false
  },
  "editor_status": "pending"
}
```

---

### evidence_item

Budget/legal evidence supporting appropriation claims.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `evidence_id` | string | ✓ | Unique ID. Pattern: `EVID-AR-*` or `EV-*` |
| `section` | string | ✓ | Links to a flow_id or authority_id |
| `claim_summary` | string | ✓ | What the evidence proves. Include line citations if available |
| `evidence_type` | enum | ✓ | `"budget"` \| `"audit"` \| `"policy"` |
| `source.title` | string | ✓ | Document title |
| `source.issuing_body` | string | ✓ | Agency or legislature |
| `source.url` | string | ✓ | Official URL |
| `confidence_level` | enum | ✓ | `"high"` \| `"medium"` \| `"low"` |
| `editor_status` | enum | ✓ | `"pending"` for new artifacts |

**Example:**
```json
{
  "evidence_id": "EVID-AR-DHS-FEDERAL-CONFORMITY-2026",
  "section": "AUTH-AR-ACA-25-10-129",
  "claim_summary": "Ark. Code § 25-10-129(b) directs DHS to promulgate rules necessary to conform DHS programs to federal law in order to receive federal funds.",
  "evidence_type": "policy",
  "source": {
    "title": "Arkansas Code § 25-10-129 - Federal fund conformity",
    "issuing_body": "Arkansas General Assembly",
    "url": "https://law.justia.com/codes/arkansas/title-25/chapter-10/subchapter-1/section-25-10-129/"
  },
  "confidence_level": "high",
  "editor_status": "pending"
}
```

---

### field_validation

Compliance checks and audit alignment records.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fv_id` | string | ✓ | Unique ID. Pattern: `FV-AR-*` |
| `jurisdiction` | string | ✓ | Always `"Arkansas"` for state artifacts |
| `validating_entity` | string | ✓ | Auditor or agency performing validation |
| `alignment_status` | enum | ✓ | `"captured"` (compliant) \| `"open"` (issue found) \| `"mixed"` |
| `evidence_basis` | array[string] | ✓ | List of evidence_ids and authority_ids supporting validation |
| `disclosure_level` | enum | ✓ | `"public"` \| `"restricted"` |
| `editor_status` | enum | ✓ | `"pending"` for new artifacts |

**Example:**
```json
{
  "fv_id": "FV-AR-DHS-FEDERAL-CONFORMITY-2026",
  "jurisdiction": "Arkansas",
  "validating_entity": "Arkansas Legislative Audit",
  "alignment_status": "captured",
  "evidence_basis": [
    "EVID-AR-DHS-FEDERAL-CONFORMITY-2026",
    "AUTH-AR-ACA-25-10-129"
  ],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

---

## ANCHOR ARTIFACT

```json
{
  "authority_id": "AUTH-AR-ACA-25-10-129",
  "authority_type": "statute",
  "citation": "Ark. Code Ann. § 25-10-129(b)",
  "administering_body": "Arkansas Department of Human Services (DHS)",
  "governs": [
    "DHS authorization to promulgate rules for federal fund conformity",
    "Federal matching fund requirements",
    "State plan amendments"
  ],
  "effects": {
    "access_limiting": false,
    "appeal_mechanism": false
  },
  "editor_status": "pending"
}
```

---

## TURN STRUCTURE

### TURN 1: Authority → Money Flows
**Anchor Type:** authority_reference  
**Generate:** 8-12 money_flow artifacts

Starting from `AUTH-AR-ACA-25-10-129` (DHS federal fund conformity), identify all money flows authorized or governed by this statute and related DHS authorities.

---

### TURN 2: Money Flow → Authorities + Evidence
**Anchor Type:** money_flow (pick the largest from Turn 1)  
**Generate:** 5-8 authority_reference + 6-10 evidence_item

From the largest money flow generated in Turn 1, identify additional statutes, federal regulations, and budget/audit evidence.

---

### TURN 3: Evidence → Field Validations + More Flows
**Anchor Type:** evidence_item (pick audit or budget evidence from Turn 2)  
**Generate:** 3-5 field_validation + 5-8 money_flow

From the evidence items in Turn 2, identify audit findings and additional funding streams.

---

### TURN 4: Validation → Complete the Graph
**Anchor Type:** field_validation (pick from Turn 3)  
**Generate:** Fill gaps - any category needed

Complete the cycle by adding evidence for unvalidated flows and authorities for statutory gaps.

---

## OUTPUT FORMAT

Return a single JSON object:

```json
{
  "batch_id": "BATCH-AUTH-AR-25-10-129-EXHAUSTIVE",
  "anchor_id": "AUTH-AR-ACA-25-10-129",
  "mode": "exhaustive-4-turn",
  "generated_at": "2025-02-05",
  "total_turns": 4,
  "artifacts": {
    "money_flow": [...],
    "authority_reference": [...],
    "evidence_item": [...],
    "field_validation": [...]
  },
  "turn_log": [
    {"turn": 1, "anchor_id": "AUTH-AR-ACA-25-10-129", "anchor_type": "authority_reference", "artifacts_generated": 0},
    {"turn": 2, "anchor_id": "...", "anchor_type": "money_flow", "artifacts_generated": 0},
    {"turn": 3, "anchor_id": "...", "anchor_type": "evidence_item", "artifacts_generated": 0},
    {"turn": 4, "anchor_id": "...", "anchor_type": "field_validation", "artifacts_generated": 0}
  ],
  "research_notes": "Summary of what was discovered and any gaps remaining"
}
```

---

## BEGIN

Start with Turn 1. Generate money flows governed by Ark. Code Ann. § 25-10-129(b) and related DHS authorities.
