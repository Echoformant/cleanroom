# AGENT_RUN: Exhaustive 4-Artifact Cycling (V2 — Fixed)
## Mode: Total Artifact Saturation

**Mode:** GPT Agent (Exhaustive Queue Cycling)  
**Expected Output:** Hundreds of artifacts covering Arkansas public finance  
**Date:** 2026-02-06

---

## CRITICAL FIXES FROM V1

**V1 FAILED BECAUSE:**
1. Evidence and validation items were queued as anchors — they produce nothing
2. Only 1 of 30 seeds was used
3. Only 42 artifacts generated instead of 200+

**V2 RULES:**
- **ONLY authority_reference and money_flow go in the queue** — these are research seeds
- **evidence_item and field_validation are OUTPUT ONLY** — never anchor on them
- **USE ALL 30 SEEDS** — do not skip any
- **Generate all 4 types per anchor** — but only queue 2 types

---

## THE CORE CONCEPT

```
RESEARCH ANCHORS:     authority_reference, money_flow
DOCUMENTATION OUTPUT: evidence_item, field_validation

For each anchor:
  1. Research it deeply
  2. Create ALL 4 artifact types (auth, flow, evidence, validation)
  3. Queue ONLY the new authority_reference and money_flow artifacts
  4. DO NOT queue evidence_item or field_validation — they are dead ends
```

---

## QUEUE MANAGEMENT

```
ANCHOR_QUEUE = [all 30 seeds]
USED_ANCHORS = []
ZERO_COUNT = 0
```

**Rules:**
1. Start with ALL 30 seed anchors in queue
2. Pop one anchor, research it
3. Generate artifacts of all 4 types
4. **Queue ONLY new authority_reference and money_flow** — NOT evidence or validation
5. After processing → move anchor to USED_ANCHORS
6. If anchor produces new auth/flow → ZERO_COUNT = 0
7. If anchor produces ONLY evidence/validation (no new auth/flow) → ZERO_COUNT += 1
8. Stop when ZERO_COUNT = 15 AND queue is empty

**NEVER queue evidence_item or field_validation as anchors.**

---

## THE 30 SEED ANCHORS

Process ALL of these. Do not skip any. Do not start with something else.

| # | Anchor ID | Type | Area |
|---|-----------|------|------|
| 1 | AUTH-AR-CONSTITUTION-ARTICLE-16 | authority | State finance constitutional provisions |
| 2 | AUTH-AR-ACA-19-1-101 | authority | State Treasury and fiscal management |
| 3 | AUTH-AR-ACA-19-4-101 | authority | Appropriations and budget process |
| 4 | AUTH-AR-ACA-19-5-101 | authority | Special revenue funds |
| 5 | AUTH-AR-ACA-25-1-101 | authority | State agencies general provisions |
| 6 | AUTH-AR-ACA-6-1-101 | authority | Education funding |
| 7 | AUTH-AR-ACA-20-76-101 | authority | Medicaid general provisions |
| 8 | AUTH-AR-ACA-20-46-101 | authority | Child welfare services |
| 9 | AUTH-AR-ACA-20-47-101 | authority | Behavioral health services |
| 10 | AUTH-AR-ACA-12-1-101 | authority | Law enforcement funding |
| 11 | AUTH-AR-ACT-1-2025 | authority | General Appropriation Act 2025 |
| 12 | MF-AR-GENERAL-REVENUE-DISTRIBUTION-FY2026 | money_flow | Master state revenue distribution |
| 13 | MF-AR-HIGHWAY-FUND-DISTRIBUTION-FY2026 | money_flow | Highway/transportation funding |
| 14 | MF-AR-EDUCATION-FOUNDATION-FUNDING-FY2026 | money_flow | K-12 education funding formula |
| 15 | MF-AR-HIGHER-ED-APPROPRIATION-FY2026 | money_flow | University system funding |
| 16 | MF-AR-CORRECTIONS-OPERATIONS-FY2026 | money_flow | Prison system funding |
| 17 | MF-AR-STATE-EMPLOYEE-BENEFITS-FY2026 | money_flow | Employee benefits/retirement |
| 18 | MF-AR-FEDERAL-FUNDS-MASTER-FY2026 | money_flow | All federal grants to Arkansas |
| 19 | AUTH-AR-ACA-21-1-101 | authority | County government funding |
| 20 | AUTH-AR-ACA-14-1-101 | authority | Municipal government funding |
| 21 | AUTH-AR-ACA-10-3-101 | authority | Legislative Council and interim committees |
| 22 | AUTH-AR-ACA-19-11-101 | authority | State procurement and contracts |
| 23 | AUTH-AR-ACA-10-4-401 | authority | Legislative Audit authority |
| 24 | AUTH-AR-TOBACCO-SETTLEMENT-TRUST | authority | Tobacco Master Settlement Fund |
| 25 | AUTH-AR-ACA-23-61-101 | authority | Insurance regulation and premium taxes |
| 26 | MF-AR-COUNTY-AID-FUND-DISTRIBUTION-FY2026 | money_flow | County aid distributions |
| 27 | MF-AR-PROPERTY-TAX-RELIEF-FUND-FY2026 | money_flow | Property tax relief payments |
| 28 | AUTH-AR-ACA-26-1-101 | authority | Tax administration |
| 29 | AUTH-AR-SINGLE-AUDIT-COMPLIANCE | authority | Federal single audit requirements |
| 30 | MF-AR-LOTTERY-SCHOLARSHIP-FUND-FY2026 | money_flow | Lottery proceeds to scholarships |

---

## PER-ANCHOR WORKFLOW

For EACH anchor:

### Step 1: Research
- What statutes/rules govern this?
- What money flows through/to/from it?
- What agencies administer it?
- What audits exist?
- What federal programs interact?

### Step 2: Generate ALL FOUR artifact types

| Type | Action |
|------|--------|
| **authority_reference** | Create any new statutes, regulations, acts discovered. **QUEUE THESE.** |
| **money_flow** | Create any fund transfers, appropriations, grants. **QUEUE THESE.** |
| **evidence_item** | Create documentation records. **DO NOT QUEUE.** |
| **field_validation** | Create audit/compliance records. **DO NOT QUEUE.** |

### Step 3: Queue correctly
- New authority_reference → ADD TO QUEUE
- New money_flow → ADD TO QUEUE
- New evidence_item → DO NOT ADD (documentation only)
- New field_validation → DO NOT ADD (compliance record only)

### Step 4: Continue
Pop next anchor. Repeat.

---

## ARTIFACT SCHEMAS

### authority_reference (QUEUE THIS)
```json
{
  "authority_id": "AUTH-AR-{TYPE}-{IDENTIFIER}",
  "authority_type": "statute" | "regulation" | "act" | "constitution",
  "citation": "Full legal citation",
  "administering_body": "Agency name",
  "governs": ["flow_ids or programs"],
  "effects": {
    "access_limiting": true/false,
    "appeal_mechanism": true/false
  },
  "editor_status": "pending"
}
```

### money_flow (QUEUE THIS)
```json
{
  "flow_id": "MF-AR-{PROGRAM}-{DESCRIPTION}-{FY}",
  "source": "Entity providing funds",
  "intermediary": "None" or "Pass-through entity",
  "destination": "Entity receiving funds",
  "amount": integer (0 if unknown),
  "fund_type": "state" | "federal" | "settlement",
  "fiscal_year": "2026",
  "restrictions": {
    "medicaid": true/false,
    "dhs_controlled": true/false
  },
  "statutory_basis": "Full citation",
  "editor_status": "pending"
}
```

### evidence_item (DO NOT QUEUE — output only)
```json
{
  "evidence_id": "EVID-AR-{SOURCE}-{DESCRIPTION}",
  "section": "artifact_id this supports",
  "claim_summary": "What the evidence proves",
  "evidence_type": "budget" | "audit" | "policy" | "federal_award",
  "source": {
    "title": "Document title",
    "issuing_body": "Agency",
    "url": "URL"
  },
  "confidence_level": "high" | "medium" | "low",
  "editor_status": "pending"
}
```

### field_validation (DO NOT QUEUE — output only)
```json
{
  "fv_id": "FV-AR-{AGENCY}-{FINDING}-{YEAR}",
  "jurisdiction": "Arkansas",
  "validating_entity": "Who validated",
  "alignment_status": "captured" | "open" | "mixed",
  "evidence_basis": ["evidence_ids", "authority_ids"],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

---

## RESEARCH DOMAINS TO COVER

Must explore all of these before stopping:

1. **Constitutional Finance** — Article 16 provisions
2. **Treasury Operations** — State Treasurer, fiscal management
3. **Appropriations** — Budget process, revenue stabilization
4. **Education** — K-12 foundation funding, higher ed, teacher retirement
5. **Health/Human Services** — Medicaid (all waivers), TANF, child welfare, behavioral health
6. **Public Safety** — State Police, corrections, courts
7. **Infrastructure** — Highway fund, county aid highway, transportation
8. **Federal Grants** — All major federal programs (SAMHSA, DOJ, DOE, HUD, USDA, etc.)
9. **Local Government** — County/municipal revenue sharing
10. **Governance** — Legislative Council, boards, rate-setting committees
11. **Audit/Compliance** — Legislative Audit findings, federal single audit
12. **Tobacco Settlement** — Master Settlement Fund distributions
13. **Insurance/Tax** — Premium taxes, tax administration
14. **Lottery** — Scholarship fund

---

## TERMINATION CONDITION

Stop ONLY when ALL of these are true:
1. **Queue is empty** — no unprocessed anchors remain
2. **ZERO_COUNT = 15** — last 15 anchors produced no new auth/flow
3. **All 30 seeds processed** — checked off
4. **All 14 domains explored** — checked off

---

## OUTPUT FORMAT

```json
{
  "batch_id": "BATCH-EXHAUSTIVE-V2-2026-02-XX",
  "mode": "exhaustive-v2",
  "generated_at": "2026-02-XX",
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
      "anchor_id": "AUTH-AR-CONSTITUTION-ARTICLE-16",
      "anchor_type": "authority_reference",
      "new_auth_created": 0,
      "new_flow_created": 0,
      "new_evidence_created": 0,
      "new_validation_created": 0,
      "queued_anchors": []
    }
  ],
  "seeds_processed": {
    "1": true,
    "2": false,
    "...": "..."
  },
  "domains_covered": {
    "constitutional_finance": true,
    "treasury": false,
    "...": "..."
  },
  "final_queue_state": {
    "remaining": [],
    "used": [],
    "zero_count": 0
  },
  "completion_status": "EXHAUSTED",
  "research_notes": "Summary"
}
```

---

## VALIDATION CHECKLIST

Before submitting:
- [ ] All 30 seeds processed
- [ ] Queue empty
- [ ] ZERO_COUNT = 15
- [ ] All 14 domains attempted
- [ ] No evidence_item or field_validation in anchor_log as anchors
- [ ] All `editor_status` = "pending"
- [ ] All money_flow have `intermediary` field (use "None" if direct)
- [ ] All money_flow have `restrictions` object

---

## BEGIN

Start with Seed #1: `AUTH-AR-CONSTITUTION-ARTICLE-16`

Work through all 30 seeds. Queue new auth/flow. Generate all 4 types. Stop when exhausted.

**REMEMBER:**
- Queue: authority_reference, money_flow
- Output only: evidence_item, field_validation
- Use ALL 30 seeds
- Target: 200+ artifacts
