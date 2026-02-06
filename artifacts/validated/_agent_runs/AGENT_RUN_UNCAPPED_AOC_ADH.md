# AGENT_RUN: Uncapped Exhaustive Schema Cycle
## Mode: Run Until Exhaustion

**Mode:** GPT Agent (Uncapped)  
**Expected Output:** As many artifacts as can be generated before exhaustion  

---

## INSTRUCTIONS

You are a legal-financial research agent for Operation NAMI Clearlane. Your task is to perform an **uncapped schema cycle** — continue generating artifacts until no new artifacts can be tied to any anchor.

Research Arkansas public finance law, appropriations, and audit records. Generate validated artifacts that link together into a coherent graph.

---

## TERMINATION CONDITION

Continue cycling through anchors until:

**No new artifacts can be generated** — every implied artifact already exists in your output.

There is NO turn limit. There is NO artifact count cap.

Each turn: pick the most densely-connected unprocessed artifact as the new anchor and generate all artifacts it implies.

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

## STARTING ANCHORS

Begin with these high-value anchors. After exhausting each, move to the next unprocessed artifact with the most implied connections.

### Primary Anchor: AOC Specialty Courts (unexplored lane)

```json
{
  "authority_id": "AUTH-AR-ACA-19-5-1144",
  "authority_type": "statute",
  "citation": "Ark. Code Ann. § 19-5-1144",
  "administering_body": "Administrative Office of the Courts (AOC)",
  "governs": [
    "Accountability Court Fund",
    "Drug court funding",
    "Mental health court funding",
    "Specialty court operations"
  ],
  "effects": {
    "access_limiting": false,
    "appeal_mechanism": false
  },
  "editor_status": "pending"
}
```

### Secondary Anchor: Arkansas Department of Health (unexplored lane)

```json
{
  "authority_id": "AUTH-AR-ACA-20-7-109",
  "authority_type": "statute",
  "citation": "Ark. Code Ann. § 20-7-109",
  "administering_body": "Arkansas Department of Health (ADH)",
  "governs": [
    "ADH authority to receive and disburse federal funds",
    "Public health program administration",
    "ADH grant management"
  ],
  "effects": {
    "access_limiting": false,
    "appeal_mechanism": false
  },
  "editor_status": "pending"
}
```

---

## CYCLING RULES

1. **Pick anchor:** Select the artifact with the most unprocessed implied connections
2. **Generate all implied artifacts:** Every authority, money flow, evidence item, and validation the anchor implies
3. **Cross-reference:** New artifacts must reference existing artifacts where applicable (use IDs in `governs[]`, `section`, `evidence_basis[]`, `statutory_basis`)
4. **Track processed anchors:** Do not re-anchor on an artifact you've already used
5. **Repeat:** Continue until no new artifacts can be generated

---

## OUTPUT FORMAT

Return a single JSON object:

```json
{
  "batch_id": "BATCH-UNCAPPED-<DATE>",
  "mode": "uncapped-exhaustive",
  "generated_at": "YYYY-MM-DD",
  "total_turns": <actual_count>,
  "artifacts": {
    "money_flow": [...],
    "authority_reference": [...],
    "evidence_item": [...],
    "field_validation": [...]
  },
  "turn_log": [
    {"turn": 1, "anchor_id": "...", "anchor_type": "...", "artifacts_generated": 0},
    ...
  ],
  "exhaustion_reason": "Why cycling stopped (e.g., 'all implied artifacts generated', 'no new connections found')",
  "research_notes": "Summary of what was discovered and any gaps remaining"
}
```

---

## BEGIN

Start with the AOC Specialty Courts anchor (AUTH-AR-ACA-19-5-1144). Generate all implied artifacts, then continue cycling until exhaustion.
