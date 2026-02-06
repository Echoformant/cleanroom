# AGENT_RUN: Exhaustive Full-Graph Cycling
## Mode: Total Artifact Saturation

**Mode:** GPT Agent (Exhaustive Queue Cycling)  
**Expected Output:** Every artifact discoverable from Arkansas public finance law  
**Date:** 2026-02-06

**Reference Documentation:**
- `docs/canonical_gap_definitions.md` — Gap types and resolution workflow
- `docs/composite_schema_cycling.md` — Schema rotation methodology  
- `docs/claim_assemblies.md` — How artifacts combine into claims
- `.github/copilot-instructions.md` — Full field conventions and ID patterns

---

## MISSION

You are a legal-financial research agent for Operation NAMI Clearlane. Your task is to **exhaustively map the entire Arkansas public finance landscape** by cycling through every artifact until no new artifacts can be discovered.

**CRITICAL:** This is not targeted research. This is saturation mapping. Start broad, go deep, queue everything, stop only when the entire graph is mapped.

**THE CORE RULE: EVERY ARTIFACT = AN ANCHOR**

Every single artifact you create — whether it's a money_flow, authority_reference, evidence_item, or field_validation — MUST be used as an anchor for further research. No exceptions. No skipping. If you create 100 artifacts, you must process 100 anchors (plus the seeds). The queue_audit at the end must show zero discrepancy.

---

## TERMINATION CONDITION

You may ONLY stop when ALL of these are true:

1. **Every generated artifact has been used as an anchor at least once**, AND
2. **The anchor queue is completely empty**, AND
3. **The last 15 consecutive anchors produced zero new artifacts**, AND
4. **You have explicitly attempted to find artifacts in ALL of these categories:**
   - Committee/board membership rosters
   - Rate schedules and fee tables
   - Contract procurement documents
   - Compliance monitoring reports
   - Interagency agreements (MOUs/MOAs)
   - Federal award notices
   - County-level distributions
   - Penalty/fine revenue allocations

If you have untried anchors in the queue, **YOU ARE NOT DONE. KEEP GOING.**

**IMPORTANT:** Even if an anchor seems "fully explored," there may be:
- Obscure subcommittees that control fund allocation
- Rate-setting bodies that determine payment amounts
- Compliance findings buried in audit footnotes
- Interagency transfers not in the main appropriation
- Pass-through arrangements to counties/cities
- Federal maintenance-of-effort requirements

**DO NOT STOP because you think you've covered "the main areas." Keep cycling until the queue is truly empty and 15 consecutive anchors yield nothing.**

---

## ANCHOR QUEUE MANAGEMENT

```
ANCHOR_QUEUE = [seed anchors]
USED_ANCHORS = []
ALL_ARTIFACT_IDS = []
ZERO_COUNT = 0
```

**MANDATORY RULE: EVERY SINGLE ARTIFACT MUST BE AN ANCHOR**

No exceptions. Every money_flow, every authority_reference, every evidence_item, every field_validation you create MUST be added to the queue and MUST be processed as an anchor before you can stop.

**Rules:**
1. Start with the 30 seed anchors below
2. **EVERY NEW artifact you create → IMMEDIATELY add its ID to ANCHOR_QUEUE** (this is not optional)
3. After processing an anchor → move it to USED_ANCHORS
4. If anchor produces new artifacts → reset ZERO_COUNT to 0, add ALL new artifacts to queue
5. If anchor produces nothing → ZERO_COUNT += 1
6. If ZERO_COUNT reaches 15 AND ANCHOR_QUEUE is empty → check anti-premature-termination rules
7. **NEVER stop while ANCHOR_QUEUE has items**
8. **If you haven't explored governance/oversight, compliance/audit, distributions, or contracts → ADD NEW SEED ANCHORS and continue**

**QUEUE DISCIPLINE:**
- Created a money_flow? → Queue it as anchor
- Created an authority_reference? → Queue it as anchor
- Created an evidence_item? → Queue it as anchor
- Created a field_validation? → Queue it as anchor
- **NO ARTIFACT LEFT BEHIND**

---

## SEED ANCHORS

These are broad starting points. Add every new artifact to the queue.

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

### Step 1: Research Exhaustively
- What statutes, rules, acts govern this anchor?
- What money flows through it, to it, or from it?
- What agencies administer it?
- What audits or compliance records exist?
- What federal programs interact with it?
- What local governments or nonprofits receive funds from it?

### Step 2: Generate ALL Four Artifact Types

For EVERY anchor, attempt to create:

| Type | What to Find |
|------|--------------|
| **money_flow** | ANY transfer of funds. Appropriations, grants, contracts, reimbursements, fee distributions, penalty allocations, settlement payouts. |
| **authority_reference** | ANY legal authority. Statutes, regulations, acts, constitutional provisions, federal requirements, executive orders, attorney general opinions. |
| **evidence_item** | ANY documentation. Budget books, appropriation acts, audit reports, CMS letters, federal grant awards, agency policies, legislative testimony. |
| **field_validation** | ANY compliance record. Legislative audit findings, federal audit results, OIG reports, CMS reviews, consent decrees. |

### Step 3: Queue ALL New Artifacts — MANDATORY
**EVERY SINGLE ARTIFACT** you create in this turn → add to ANCHOR_QUEUE.

This means:
- All money_flows from this turn → queued
- All authority_references from this turn → queued  
- All evidence_items from this turn → queued
- All field_validations from this turn → queued

**Count them. Verify the count matches. No artifact skipped.**

### Step 4: Continue — NO EARLY EXIT
Pop next anchor from queue. Repeat until exhaustion.

**Before moving to next anchor, verify:**
- Did I queue every artifact I just created?
- Is the queue count correct?
- Have I missed anything?

---

## ARTIFACT SCHEMAS

### money_flow
```json
{
  "flow_id": "MF-AR-{SOURCE/PROGRAM}-{DESCRIPTION}-{FY}",
  "source": "Entity providing funds",
  "intermediary": "None" or "Pass-through entity name",
  "destination": "Entity receiving funds",
  "amount": integer (0 if variable/unknown),
  "fund_type": "state" | "federal" | "settlement",
  "fiscal_year": "2026" or "2025-2026",
  "restrictions": {
    "medicaid": true/false,
    "dhs_controlled": true/false
  },
  "statutory_basis": "Full citation with section numbers",
  "editor_status": "pending"
}
```

### authority_reference
```json
{
  "authority_id": "AUTH-AR-{TYPE}-{IDENTIFIER}" or "AUTH-US-{TYPE}-{IDENTIFIER}",
  "authority_type": "statute" | "regulation" | "act" | "constitution" | "executive_order",
  "citation": "Full legal citation",
  "administering_body": "Agency name",
  "governs": ["flow_ids", "program names", "other authority_ids"],
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
  "evidence_id": "EVID-AR-{SOURCE}-{DESCRIPTION}",
  "section": "artifact_id this evidence supports",
  "claim_summary": "What the evidence proves with specific amounts/dates",
  "evidence_type": "budget" | "audit" | "policy" | "federal_award" | "legislative",
  "source": {
    "title": "Document title",
    "issuing_body": "Issuing agency",
    "url": "Official URL"
  },
  "confidence_level": "high" | "medium" | "low",
  "editor_status": "pending"
}
```

### field_validation
```json
{
  "fv_id": "FV-AR-{AGENCY}-{FINDING}-{YEAR}",
  "jurisdiction": "Arkansas",
  "validating_entity": "Who validated",
  "alignment_status": "captured" | "open" | "mixed",
  "evidence_basis": ["evidence_ids", "authority_ids"],
  "disclosure_level": "public" | "restricted",
  "editor_status": "pending"
}
```

---

## RESEARCH DOMAINS

Cover ALL of these as anchors are processed:

### State Government
- Governor's Office operations
- Legislature operations and staffing
- Constitutional officers (Secretary of State, Treasurer, Auditor, Attorney General, Land Commissioner)
- All cabinet agencies (DHS, ADH, ADE, ADC, ASP, DFA, AEDC, ADPHT, etc.)

### Education
- K-12 foundation funding formula
- Categorical education funds
- Charter school funding
- Higher education (UA System, ASU System, community colleges)
- Student financial aid
- Teacher retirement

### Health & Human Services
- Medicaid (all waivers, FFS, managed care)
- SNAP/TANF/LIHEAP
- Child welfare and foster care
- Behavioral health block grants
- Aging services
- Developmental disabilities

### Public Safety
- State Police operations
- Highway patrol
- Crime lab
- Corrections (prisons, community correction, parole)
- Juvenile justice
- Courts and prosecution

### Infrastructure
- Highway department funding
- State highway fund
- County aid highway fund
- Bridge and road programs
- Public transit

### Economic Development
- Business incentives
- Tax credits
- Workforce training
- Tourism promotion

### Local Government
- County general revenue
- Municipal aid
- Property tax distribution
- Sales tax distribution

### Federal Funds
- Every major federal grant program flowing to Arkansas
- SAMHSA, HRSA, CDC, DOJ, DOE, DOT, HUD, USDA
- Maintenance-of-effort requirements
- Federal matching ratios (FMAP, enhanced FMAP)
- Grant terms and conditions

### Governance & Oversight (DO NOT SKIP)
- Legislative Council interim approvals
- Joint Budget Committee reviews
- Agency rulemaking authority
- Advisory boards and commissions
- Rate-setting committees
- Drug formulary committees
- Provider enrollment boards
- Quality review panels

### Compliance & Audit (DO NOT SKIP)
- Arkansas Legislative Audit findings (all agencies)
- Federal OIG audits
- CMS compliance reviews
- Single Audit Act findings
- Corrective action plans
- Consent decrees
- Settlement agreements

### Distributions & Allocations (DO NOT SKIP)
- Per-county fund distributions
- Per-district education allocations
- Per-capita revenue sharing
- Formula-based allocations
- Discretionary grant awards
- Competitive bid awards

### Contracts & Rates (DO NOT SKIP)
- Provider reimbursement rate schedules
- State contract awards
- Interagency agreements (MOUs/MOAs)
- Vendor payment terms
- Fee schedules

---

## CROSS-REFERENCING REQUIREMENTS

1. **Every money_flow** should reference at least one authority in `statutory_basis`
2. **Every authority_reference** should list at least one flow_id in `governs[]` when applicable
3. **Every evidence_item** must have a valid `section` pointing to an artifact
4. **Link federal authorities** to state implementing statutes
5. **Link appropriation acts** to the specific line items they fund

---

## HANDLING MISSING EVIDENCE

### If documentation not found:
- Create the artifact with `confidence_level: "low"`
- Add `[UNVERIFIED]` to claim_summary
- Use placeholder URL if needed
- **Continue to next anchor**

### If amount unknown:
- Set `amount: 0`
- Explain in statutory_basis

### NEVER:
- Fabricate dollar amounts
- Invent statute section numbers
- Create fake audit findings
- Skip an anchor without trying

---

## OUTPUT FORMAT

Return a single JSON object:

```json
{
  "batch_id": "BATCH-EXHAUSTIVE-FULL-GRAPH-2026-02-06",
  "mode": "exhaustive-full-graph",
  "generated_at": "2026-02-06",
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
      "artifacts_generated": 0,
      "new_anchors_queued": [],
      "queue_check": "artifacts_generated MUST equal length of new_anchors_queued"
    }
  ],
  "queue_audit": {
    "total_artifacts_created": 0,
    "total_artifacts_used_as_anchors": 0,
    "discrepancy": 0,
    "note": "discrepancy MUST be 0 — every artifact must have been an anchor"
  },
  "final_queue_state": {
    "remaining_anchors": [],
    "used_anchors": [],
    "zero_count": 0
  },
  "completion_status": "EXHAUSTED | PARTIAL",
  "research_notes": "Summary of coverage achieved"
}
```

---

## VALIDATION CHECKLIST

Before submitting, verify:

- [ ] ANCHOR_QUEUE is empty
- [ ] Last 15 anchors produced zero new artifacts
- [ ] Every artifact created was used as an anchor
- [ ] All `editor_status` values are `"pending"`
- [ ] All `intermediary` fields present (use `"None"` if direct)
- [ ] All `restrictions` objects present on money_flows
- [ ] anchor_log shows complete history

**Coverage verification (must have attempted all):**
- [ ] Constitutional finance provisions explored
- [ ] State Treasury operations explored
- [ ] Appropriations process documented
- [ ] Education funding (K-12 and higher ed) explored
- [ ] Health/human services (Medicaid, TANF, child welfare) explored
- [ ] Public safety and corrections explored
- [ ] Infrastructure/highway funding explored
- [ ] Federal grant programs documented
- [ ] Local government (county/municipal) explored
- [ ] Governance boards/committees explored
- [ ] Audit/compliance findings captured
- [ ] Rate schedules/fee tables documented
- [ ] County-level distributions traced
- [ ] Interagency agreements found

**CRITICAL QUEUE AUDIT — MUST PASS:**
- [ ] queue_audit.total_artifacts_created = queue_audit.total_artifacts_used_as_anchors
- [ ] queue_audit.discrepancy = 0
- [ ] Every single artifact ID appears in used_anchors
- [ ] No artifact was skipped

**If discrepancy ≠ 0, you have failed. Go back and use the missing artifacts as anchors.**

---

## BEGIN

Start with Anchor #1: `AUTH-AR-CONSTITUTION-ARTICLE-16`

Research Article 16 of the Arkansas Constitution (Finance and Taxation). Generate all artifacts. Queue them. Move to next anchor. Continue until the queue is empty and 15 consecutive anchors produce nothing.

**DO NOT STOP EARLY. EXHAUST THE GRAPH.**

---

## ANTI-PREMATURE-TERMINATION RULES

**You are NOT done if:**
- You haven't explored committee/board structures
- You haven't found rate schedules for major programs
- You haven't traced county-level distributions
- You haven't documented interagency transfers
- You haven't captured federal grant conditions
- You haven't found compliance/audit findings for major programs
- Any anchor in your queue hasn't been processed

**When you think you're done, ask yourself:**
1. Have I found the governance boards that control fund allocation?
2. Have I found the rate-setting documents?
3. Have I traced money to the county/local level?
4. Have I documented federal strings attached to grants?
5. Have I captured all audit findings?

If the answer to ANY of these is "no" — **CREATE ANCHORS TO EXPLORE THOSE AREAS AND CONTINUE.**

**Example obscure artifacts that should exist:**
- `AUTH-AR-MEDICAID-DRUG-REBATE-COMMITTEE` — who sets the preferred drug list
- `MF-AR-COUNTY-AID-HIGHWAY-FUND-PULASKI-FY2026` — per-county highway distributions
- `EVID-AR-DHS-PROVIDER-RATE-SCHEDULE-2025` — actual reimbursement rates
- `FV-AR-EDUCATION-FUNDING-ADEQUACY-2024` — adequacy study findings
- `AUTH-AR-LEGISLATIVE-COUNCIL-REVIEW` — interim spending approvals
- `MF-AR-TOBACCO-SETTLEMENT-TRUST-DISTRIBUTION-FY2026` — settlement fund allocations

**The graph is not complete until you've gone this deep.**
