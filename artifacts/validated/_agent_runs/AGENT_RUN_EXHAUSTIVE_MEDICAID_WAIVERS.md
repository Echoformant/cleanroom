# AGENT_RUN: Exhaustive Medicaid Waiver Cycling
## Mode: Full Anchor Rotation Until Exhaustion

**Mode:** GPT Agent (Exhaustive Cycling)  
**Expected Output:** All artifacts discoverable from Medicaid waiver authorities  
**Date:** 2026-02-05

---

## MISSION

You are a legal-financial research agent for Operation NAMI Clearlane. Your task is to **exhaustively cycle through every artifact** generated from Arkansas Medicaid waiver programs until no new artifacts can be produced.

**CRITICAL RULE:** Do NOT stop because an anchor produces nothing. Move to the next anchor in the queue. Only stop when **every artifact has been used as an anchor** and the queue is empty.

---

## TERMINATION CONDITION

You may ONLY stop when:

1. **Every generated artifact has been used as an anchor at least once**, AND
2. **The anchor queue is completely empty**, AND  
3. **The last 5 consecutive anchors produced zero new artifacts**

If you have untried anchors in the queue, **you are not done**.

---

## ANCHOR QUEUE MANAGEMENT

Maintain an explicit queue of anchors:

```
ANCHOR_QUEUE = []
USED_ANCHORS = []
GENERATED_ARTIFACTS = []
```

**Rules:**
1. Start with the seed anchors below
2. Every NEW artifact you create gets added to ANCHOR_QUEUE
3. After processing an anchor, move it to USED_ANCHORS
4. Pick next anchor from ANCHOR_QUEUE
5. If ANCHOR_QUEUE is empty and last 5 anchors produced nothing → DONE
6. If an anchor produces new artifacts → add them to queue, reset zero-count

---

## SEED ANCHORS

Start with these. Add every new artifact to the queue.

| # | Anchor ID | Type | Description |
|---|-----------|------|-------------|
| 1 | `AUTH-AR-1115-WAIVER-ARHOME` | authority_reference | Arkansas 1115 Medicaid Demonstration Waiver |
| 2 | `AUTH-AR-HCBS-ARCHOICES` | authority_reference | ARChoices Home and Community-Based Services Waiver |
| 3 | `AUTH-AR-PASSE-PROGRAM` | authority_reference | Provider-led Arkansas Shared Savings Entity |
| 4 | `AUTH-US-42-CFR-438` | authority_reference | Federal Medicaid Managed Care Regulations |
| 5 | `MF-AR-DHS-MS-HOSPITAL-MEDICAL-FY2026` | money_flow | Largest Medicaid flow from Agency Sweep |

---

## PER-ANCHOR WORKFLOW

For each anchor, follow this sequence:

### Step 1: Research the Anchor
- What does this anchor authorize, fund, or document?
- What other statutes, programs, or entities does it reference?
- What money flows through or from it?

### Step 2: Generate All Implied Artifacts

For EACH anchor, attempt to generate:

| Category | What to Look For |
|----------|------------------|
| **money_flow** | Any dollar amount moving between entities. Waiver capitation payments, fee-for-service rates, PASSE payments, provider payments. |
| **authority_reference** | Any statute, regulation, rule, or CMS approval cited. State Plan Amendments, waiver renewals, ACA sections. |
| **evidence_item** | Budget documents, CMS approval letters, DHS policy manuals, rate schedules. |
| **field_validation** | Legislative Audit findings, CMS compliance reviews, OIG reports. |

### Step 3: Add New Artifacts to Queue
Every artifact you create → add its ID to ANCHOR_QUEUE.

### Step 4: Mark Anchor as Used
Move current anchor to USED_ANCHORS.

### Step 5: Pick Next Anchor
Pop next from ANCHOR_QUEUE. If empty and last 5 were zero → DONE.

---

## SPECIFIC RESEARCH TARGETS

These are known Medicaid waiver components. Generate artifacts for each you find evidence of:

### 1115 Demonstration Waiver (AR HOPE / Arkansas Works)
- Premium assistance payments
- Work requirement provisions (suspended/reinstated history)
- Expansion population coverage
- CMS approval/renewal letters
- State match requirements

### ARChoices HCBS Waiver
- Personal care services rates
- Attendant care payments
- Environmental modifications
- Provider enrollment requirements
- Slot allocations by county

### PASSE Program
- Capitation rates by acuity tier
- PASSE entity contracts (Empower, Summit, Arkansas Total Care)
- Behavioral health carve-in
- Care coordination requirements
- Quality metrics and withhold amounts

### Traditional Medicaid
- Hospital per diem rates
- Physician fee schedule
- Nursing facility rates
- Pharmacy reimbursement
- DME fee schedule

### Managed Care Oversight
- EQRO contracts
- Network adequacy requirements
- Grievance procedures
- Rate certification process

---

## ARTIFACT SCHEMAS

### money_flow
```json
{
  "flow_id": "MF-AR-MEDICAID-{PROGRAM}-{DESCRIPTION}-{FY}",
  "source": "Entity providing funds",
  "intermediary": "None" or pass-through entity,
  "destination": "Entity receiving funds",
  "amount": integer USD (0 if variable),
  "fund_type": "state" | "federal" | "settlement",
  "fiscal_year": "2026" or "2025-2026",
  "restrictions": {
    "medicaid": true,
    "dhs_controlled": true
  },
  "statutory_basis": "Full citation with waiver reference",
  "editor_status": "pending"
}
```

### authority_reference
```json
{
  "authority_id": "AUTH-AR-{TYPE}-{IDENTIFIER}",
  "authority_type": "statute" | "regulation" | "act" | "waiver" | "state_plan_amendment",
  "citation": "Full legal citation",
  "administering_body": "Arkansas DHS Division of Medical Services",
  "governs": ["list of flow_ids and programs governed"],
  "effects": {
    "access_limiting": true/false,
    "appeal_mechanism": true/false
  },
  "editor_status": "pending"
}
```

### evidence_item
```json
{
  "evidence_id": "EVID-AR-MEDICAID-{SOURCE}-{DESCRIPTION}",
  "section": "flow_id or authority_id this supports",
  "claim_summary": "What the evidence proves",
  "evidence_type": "budget" | "audit" | "policy" | "cms_approval",
  "source": {
    "title": "Document title",
    "issuing_body": "CMS or DHS or Legislative Audit",
    "url": "Official URL"
  },
  "confidence_level": "high" | "medium" | "low",
  "editor_status": "pending"
}
```

### field_validation
```json
{
  "fv_id": "FV-AR-MEDICAID-{FINDING}-{YEAR}",
  "jurisdiction": "Arkansas",
  "validating_entity": "CMS" | "Arkansas Legislative Audit" | "OIG",
  "alignment_status": "captured" | "open" | "mixed",
  "evidence_basis": ["evidence_id", "authority_id"],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

---

## HANDLING MISSING EVIDENCE

### If you cannot find a specific document:
- Create the artifact anyway with `confidence_level: "low"`
- Add `[UNVERIFIED]` to the claim_summary
- Use placeholder URL: `"https://medicaid.arkansas.gov/[PENDING]"`
- Continue to next anchor

### If a waiver/program doesn't exist:
- Note it in research_notes
- Move to next anchor
- Do NOT fabricate programs

### If amount is variable or rate-based:
- Set `amount: 0`
- Explain in `statutory_basis`: "Per-member-per-month rate; see rate schedule for amounts"

---

## OUTPUT FORMAT

Return a single JSON object with anchor tracking:

```json
{
  "batch_id": "BATCH-MEDICAID-WAIVERS-EXHAUSTIVE-2026-02-05",
  "mode": "exhaustive-cycling",
  "generated_at": "2026-02-05",
  "total_artifacts": 0,
  "total_anchors_processed": 0,
  "artifacts": {
    "money_flow": [],
    "authority_reference": [],
    "evidence_item": [],
    "field_validation": []
  },
  "anchor_log": [
    {
      "turn": 1,
      "anchor_id": "AUTH-AR-1115-WAIVER-ARHOME",
      "anchor_type": "authority_reference",
      "artifacts_generated": 0,
      "new_anchors_queued": []
    }
  ],
  "final_queue_state": {
    "remaining_anchors": [],
    "used_anchors": [],
    "zero_count": 0
  },
  "completion_status": "EXHAUSTED | PARTIAL",
  "research_notes": "Summary of waiver landscape and gaps"
}
```

---

## CROSS-REFERENCE REQUIREMENTS

1. **Every money_flow with `restrictions.medicaid: true`** must reference:
   - At least one waiver or state plan authority
   - DHS-MS as administering body

2. **Every PASSE flow** must reference:
   - AUTH-AR-PASSE-PROGRAM
   - Specific PASSE entity name

3. **Every rate-based flow** should reference:
   - Rate effective date
   - CMS rate certification if capitated

4. **Link to existing artifacts** where applicable:
   - `MF-AR-DHS-MS-*` flows from Agency Sweep
   - `AUTH-AR-ACA-20-77-107` (Medicaid enabling statute)

---

## VALIDATION CHECKLIST

Before submitting, verify:

- [ ] Every artifact has been used as an anchor OR is in the queue
- [ ] Anchor queue is empty
- [ ] Last 5 anchors produced zero new artifacts
- [ ] All `restrictions.medicaid` flows have waiver/SPA authority
- [ ] All PASSE references include entity names
- [ ] All `editor_status` values are `"pending"`
- [ ] anchor_log shows complete rotation history

---

## BEGIN

Start with Anchor #1: `AUTH-AR-1115-WAIVER-ARHOME`

Research the Arkansas 1115 Medicaid Demonstration Waiver. Generate all implied artifacts. Add each new artifact to the queue. Continue until exhaustion.

**Remember:** Do NOT stop until every artifact has been an anchor and the queue is empty.
