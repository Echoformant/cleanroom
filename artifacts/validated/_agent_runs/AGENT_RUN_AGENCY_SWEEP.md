# AGENT_RUN: Agency Sweep — Full State Coverage
## Mode: Sequential Agency Processing

**Mode:** GPT Agent (Agency Queue)  
**Expected Output:** 150+ artifacts across all major Arkansas state agencies  
**Date:** 2026-02-05

---

## MISSION

You are a legal-financial research agent for Operation NAMI Clearlane. Your task is to systematically process **every agency in the queue below**, generating all artifacts implied by each agency's appropriation act and enabling statutes.

**DO NOT STOP** until you have processed every agency in the queue.

---

## TERMINATION CONDITION

You may ONLY stop when:

1. **Every agency in the queue has been processed**, AND
2. **You have generated at least one money_flow for each agency**, AND
3. **Three consecutive anchor attempts yield zero new artifacts**

If you have not processed all 15 agencies, **you are not done**.

---

## AGENCY QUEUE

Process these agencies **in order**. For each agency:
1. Research the FY2025-2026 appropriation act
2. Research the enabling statute(s)
3. Generate ALL money_flow artifacts from the appropriation
4. Generate authority_reference for each governing statute/act
5. Generate evidence_item linking flows to budget documents
6. Generate field_validation where legislative audit data exists

Mark each agency ✓ as you complete it.

| # | Agency | Abbreviation | Appropriation Act (2025 session) |
|---|--------|--------------|----------------------------------|
| 1 | Administrative Office of the Courts | AOC | Act 776 of 2025 |
| 2 | Arkansas Department of Health | ADH | Act 538 of 2025 |
| 3 | Department of Human Services — Medical Services | DHS-MS | Act 504 of 2025 |
| 4 | Department of Human Services — Behavioral Health | DHS-OBHS | Act 504 of 2025 |
| 5 | Department of Human Services — Children & Family Services | DHS-DCFS | Act 504 of 2025 |
| 6 | Department of Human Services — County Operations | DHS-DCO | Act 504 of 2025 |
| 7 | Department of Human Services — Provider Services & Quality Assurance | DPSQA | Act 504 of 2025 |
| 8 | Department of Finance and Administration | DFA | Act 545 of 2025 |
| 9 | Arkansas Department of Education | ADE | Act 509 of 2025 |
| 10 | Department of Correction | ADC | Act 517 of 2025 |
| 11 | Arkansas State Police | ASP | Act 562 of 2025 |
| 12 | Arkansas Insurance Department | AID | Act 555 of 2025 |
| 13 | Department of Labor and Licensing | ADLL | Act 558 of 2025 |
| 14 | Arkansas Economic Development Commission | AEDC | Act 525 of 2025 |
| 15 | Department of Parks, Heritage and Tourism | ADPHT | Act 533 of 2025 |

---

## PER-AGENCY WORKFLOW

For each agency, follow this exact sequence:

### Step 1: Find the Appropriation Act
Research the agency's appropriation act from the 2025 Regular Session. The act number is provided in the queue above.

### Step 2: Extract Money Flows
For EACH line item in the appropriation act that transfers money:
- Create a `money_flow` artifact
- Use the section number in `statutory_basis`
- Include the exact dollar amount from the act

### Step 3: Find Enabling Statutes
Research Arkansas Code Annotated for the agency's:
- Enabling statute (creates the agency)
- Rulemaking authority
- Federal fund conformity requirements

Create `authority_reference` artifacts for each.

### Step 4: Link Evidence
Create `evidence_item` artifacts that:
- Reference the appropriation act section
- Quote the budget amount
- Link to the official act URL

### Step 5: Validate
If Arkansas Legislative Audit has findings for this agency:
- Create `field_validation` artifact
- Set `alignment_status` based on audit outcome
- Reference the evidence and authority in `evidence_basis`

### Step 6: Move to Next Agency
Do NOT cycle within one agency. Process the full queue breadth-first.

---

## CANONICAL SCHEMA DEFINITIONS

### money_flow

Tracks money moving between government entities.

**Required Fields (ALL must be present):**

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `flow_id` | string | `MF-AR-*` or `MF-US-*` | Unique identifier. Pattern: `MF-AR-{AGENCY}-{PROGRAM}-{FY}` |
| `source` | string | — | Entity providing funds. Use official name. |
| `intermediary` | string | `"None"` or entity name | Pass-through entity. Use `"None"` if direct transfer. NEVER omit. |
| `destination` | string | — | Entity receiving funds. Use official name. |
| `amount` | integer | ≥0 | USD amount. NO commas, NO decimals. Use `0` if variable (explain in statutory_basis). |
| `fund_type` | enum | `"state"` `"federal"` `"settlement"` | Source of funds. Use `"state"` for AR-appropriated even if federally matched. |
| `fiscal_year` | string | `"2026"` or `"2025-2026"` | Single year or biennium. |
| `restrictions.medicaid` | boolean | `true` `false` | True ONLY if destination is Medicaid-reimbursable. |
| `restrictions.dhs_controlled` | boolean | `true` `false` | True if DHS disburses or controls the funds. |
| `statutory_basis` | string | — | Full citation. Include act section: `"Act 504 of 2025 § 3"` |
| `editor_status` | enum | `"pending"` | Always `"pending"` for new artifacts. |

**Example:**
```json
{
  "flow_id": "MF-AR-DHS-MEDICAID-SERVICES-FY2026",
  "source": "Arkansas General Revenue",
  "intermediary": "None",
  "destination": "Department of Human Services - Division of Medical Services",
  "amount": 148000000,
  "fund_type": "state",
  "fiscal_year": "2026",
  "restrictions": {
    "medicaid": true,
    "dhs_controlled": true
  },
  "statutory_basis": "Act 504 of 2025 § 3; Ark. Code Ann. § 20-77-107",
  "editor_status": "pending"
}
```

---

### authority_reference

Statutes, rules, and acts that authorize fund use.

**Required Fields (ALL must be present):**

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `authority_id` | string | `AUTH-AR-*` or `AUTH-US-*` | Pattern: `AUTH-AR-ACA-{title}-{chapter}-{section}` or `AUTH-AR-ACT-{number}-{year}` |
| `authority_type` | enum | `"statute"` `"regulation"` `"act"` | Type of legal authority. |
| `citation` | string | — | Full legal citation. Preserve § symbols. Example: `"Ark. Code Ann. § 20-77-107"` |
| `administering_body` | string | — | Agency responsible for implementation. |
| `governs` | array[string] | — | List of what this authority controls. Include flow_ids where applicable. |
| `effects.access_limiting` | boolean | `true` `false` | True if restricts access to services. |
| `effects.appeal_mechanism` | boolean | `true` `false` | True if provides appeal rights. |
| `editor_status` | enum | `"pending"` | Always `"pending"` for new artifacts. |

**Example:**
```json
{
  "authority_id": "AUTH-AR-ACT-504-2025",
  "authority_type": "act",
  "citation": "Act 504 of 2025 (DHS Appropriation)",
  "administering_body": "Arkansas Department of Human Services",
  "governs": [
    "DHS Medical Services appropriation FY2026",
    "DHS OBHS appropriation FY2026",
    "MF-AR-DHS-MEDICAID-SERVICES-FY2026",
    "MF-AR-DHS-OBHS-OPERATIONS-FY2026"
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

**Required Fields (ALL must be present):**

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `evidence_id` | string | `EVID-AR-*` | Pattern: `EVID-AR-{ACT/STATUTE}-{SECTION}-{DESCRIPTION}` |
| `section` | string | — | Links to a `flow_id` or `authority_id`. Must reference existing artifact. |
| `claim_summary` | string | — | What the evidence proves. Include specific amounts and section numbers. |
| `evidence_type` | enum | `"budget"` `"audit"` `"policy"` | Type of evidence. |
| `source.title` | string | — | Document title. |
| `source.issuing_body` | string | — | Agency or legislature that issued it. |
| `source.url` | string | — | Official URL. Use `arkleg.state.ar.us` for acts. |
| `confidence_level` | enum | `"high"` `"medium"` `"low"` | Based on source reliability. |
| `editor_status` | enum | `"pending"` | Always `"pending"` for new artifacts. |

**Example:**
```json
{
  "evidence_id": "EVID-AR-ACT504-SEC3-MEDICAID-APPROPRIATION",
  "section": "MF-AR-DHS-MEDICAID-SERVICES-FY2026",
  "claim_summary": "Act 504 of 2025 Section 3 appropriates $148,000,000 from General Revenue for DHS Medical Services operations.",
  "evidence_type": "budget",
  "source": {
    "title": "Act 504 of 2025 — Department of Human Services Appropriation",
    "issuing_body": "Arkansas General Assembly",
    "url": "https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2F&file=504.pdf"
  },
  "confidence_level": "high",
  "editor_status": "pending"
}
```

---

### field_validation

Compliance checks and audit alignment records.

**Required Fields (ALL must be present):**

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `fv_id` | string | `FV-AR-*` | Pattern: `FV-AR-{AGENCY}-{FINDING}-{YEAR}` |
| `jurisdiction` | string | `"Arkansas"` | Always `"Arkansas"` for state artifacts. |
| `validating_entity` | string | — | Who performed the validation. Usually `"Arkansas Legislative Audit"`. |
| `alignment_status` | enum | `"captured"` `"open"` `"mixed"` | `captured` = compliant, `open` = issue found, `mixed` = partial compliance |
| `evidence_basis` | array[string] | — | List of `evidence_id` and `authority_id` values supporting this validation. |
| `disclosure_level` | enum | `"public"` `"restricted"` | Visibility of the validation record. |
| `editor_status` | enum | `"pending"` | Always `"pending"` for new artifacts. |

**Example:**
```json
{
  "fv_id": "FV-AR-DHS-MEDICAID-COMPLIANCE-2026",
  "jurisdiction": "Arkansas",
  "validating_entity": "Arkansas Legislative Audit",
  "alignment_status": "captured",
  "evidence_basis": [
    "EVID-AR-ACT504-SEC3-MEDICAID-APPROPRIATION",
    "AUTH-AR-ACT-504-2025",
    "AUTH-AR-ACA-20-77-107"
  ],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

---

## HANDLING MISSING EVIDENCE

If you cannot find supporting documentation for an artifact:

### Scenario 1: Appropriation Act Not Accessible
- **Action:** Create the money_flow anyway using the best available source
- **Mark:** Set `confidence_level: "low"` on the evidence_item
- **Note:** Add `"[UNVERIFIED - act text not accessed]"` to `claim_summary`

### Scenario 2: Statute Citation Cannot Be Verified
- **Action:** Create authority_reference with the citation you found referenced elsewhere
- **Mark:** Add `"[CITATION UNVERIFIED]"` suffix to `citation` field
- **Note:** Still include in `governs[]` — verification is a later step

### Scenario 3: No Audit Data Exists
- **Action:** Skip field_validation for that agency
- **Note:** Not every agency has audit findings — this is acceptable

### Scenario 4: URL Is Dead or Unknown
- **Action:** Use placeholder URL format: `"https://www.arkleg.state.ar.us/Acts/[PENDING]"`
- **Mark:** Set `confidence_level: "low"`
- **Note:** Real URL can be added during review

### Scenario 5: Amount Is Variable or Unknown
- **Action:** Set `amount: 0`
- **Mark:** Explain in `statutory_basis`: `"Amount varies; see Act XXX § Y for formula"`

### Scenario 6: No New Evidence Available, But Prior Artifact Supports
- **Action:** Reference the existing artifact ID in `evidence_basis`, `governs[]`, or `section`
- **Priority:** This is a **FALLBACK ONLY** — prefer creating new evidence
- **When valid:**
  - A previously-created authority_reference covers the same statute
  - A previously-created evidence_item documents the same act section
  - A previously-created money_flow shares the same statutory_basis
- **Example:** If `AUTH-AR-ACT-504-2025` already exists and governs DHS-MS, you may reference it in DHS-OBHS artifacts instead of creating a duplicate

**NEVER:**
- Invent dollar amounts
- Fabricate statute section numbers
- Create fake audit findings
- Skip an agency entirely due to missing evidence

**ALWAYS:**
- Create the artifact with available information
- Mark uncertainty explicitly
- Continue to the next agency

---

## CROSS-REFERENCING RULES

1. **Every money_flow MUST have:**
   - At least one `authority_reference` in its `statutory_basis`
   - At least one `evidence_item` with `section` pointing to the flow_id

2. **Every authority_reference SHOULD have:**
   - At least one flow_id in its `governs[]` array
   - An `evidence_item` documenting the statute text

3. **Every evidence_item MUST have:**
   - A valid `section` pointing to an existing artifact

4. **field_validation artifacts:**
   - Create when Legislative Audit data exists
   - Reference at least one authority and one evidence in `evidence_basis`
   - **Skip if no audit data exists** — do not fabricate compliance status

---

## OUTPUT FORMAT

Return a single JSON object:

```json
{
  "batch_id": "BATCH-AGENCY-SWEEP-2026-02-05",
  "mode": "agency-sweep",
  "generated_at": "2026-02-05",
  "agencies_processed": 15,
  "total_artifacts": 0,
  "artifacts": {
    "money_flow": [],
    "authority_reference": [],
    "evidence_item": [],
    "field_validation": []
  },
  "agency_log": [
    {"agency": "AOC", "flows": 0, "authorities": 0, "evidence": 0, "validations": 0},
    {"agency": "ADH", "flows": 0, "authorities": 0, "evidence": 0, "validations": 0}
  ],
  "completion_status": "ALL_AGENCIES_PROCESSED | PARTIAL",
  "notes": "Summary of coverage and any gaps remaining"
}
```

---

## VALIDATION CHECKLIST

Before submitting, verify:

- [ ] All 15 agencies have at least one money_flow
- [ ] Every money_flow has `intermediary` field (use `"None"` if direct)
- [ ] Every money_flow has `restrictions.medicaid` and `restrictions.dhs_controlled`
- [ ] All amounts are integers (no commas, no decimals)
- [ ] All `editor_status` values are `"pending"`
- [ ] All `governs[]` arrays include flow_ids where applicable
- [ ] All `section` fields in evidence_item reference valid artifact IDs

---

## BEGIN

Start with Agency #1 (AOC). You already have data for AOC and ADH from previous runs — you may skip those and start with Agency #3 (DHS-MS) if you prefer.

Process all 15 agencies. Generate all implied artifacts. Do not stop until the queue is empty.
