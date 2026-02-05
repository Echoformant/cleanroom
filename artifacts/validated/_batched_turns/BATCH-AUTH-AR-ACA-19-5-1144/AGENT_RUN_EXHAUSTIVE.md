# SINGLE ARTIFACT BATCH CYCLING — GPT AGENT MODE (EXHAUSTIVE)

You are running a Single Artifact Batch Cycling operation for Operation NAMI Clearlane.

**MODE: EXHAUSTIVE** — Run until no more valid anchors can be produced.

## YOUR MISSION

Research Arkansas public-finance data and generate as many schema-valid artifacts as possible from one anchor. Continue cycling through turns until research is exhausted. This is NOT a template — execute this now.

---

## CANONICAL ARTIFACT DEFINITIONS (CRITICAL)

These definitions are BINDING. Do not deviate.

### authority_reference
**Definition:** A statute, regulation, or policy that AUTHORIZES or GOVERNS an action, program, or fund.
**Use when:** The source IS the law itself — the text that creates authority.
**Contains:** Legal citations, administering bodies, what it governs.
**Examples:** Arkansas Code sections, CFR regulations, DHS policy manuals.
**NOT for:** Budget documents, audit reports, appropriation line items.

### money_flow
**Definition:** A discrete movement of funds FROM a source TO a destination, optionally through an intermediary.
**Use when:** You can identify source → destination and an amount (or authorization to move funds).
**Contains:** Funding source, pass-through entity, receiving entity, amount, fiscal year, restrictions.
**Examples:** "Act 776 appropriates $300,000 from General Revenue to AOC for Drug Courts."
**NOT for:** The statute text itself (that's authority_reference) or the document proving it (that's evidence_item).

### evidence_item
**Definition:** A DOCUMENT or SOURCE that proves a claim about authority or money flow.
**Use when:** You have a citable document that supports another artifact's existence.
**Contains:** Document title, issuing body, URL, what claim it supports.
**Examples:** Budget documents, appropriation act PDFs, grant award letters, AOC annual reports.
**NOT for:** The law itself (authority_reference) or audit conclusions (field_validation).

### field_validation
**Definition:** A CONFIRMATION that authority and evidence align — an audit finding, compliance check, or verification.
**Use when:** An independent entity has validated, audited, or confirmed something.
**Contains:** Validating entity, alignment status, what evidence it relies on.
**Examples:** Legislative Audit findings, federal compliance reports, AOC internal audit results.
**NOT for:** The source document (evidence_item) or the law being audited (authority_reference).

### The Chain
```
authority_reference (the law) 
    → authorizes → 
money_flow (the funds moving)
    → documented by → 
evidence_item (the proof)
    → validated by → 
field_validation (the confirmation)
```

---

## ANCHOR ARTIFACT (Your Starting Point)

```json
{
  "authority_id": "AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND",
  "authority_type": "statute",
  "citation": "Arkansas Code Annotated §19-5-1144",
  "administering_body": "Arkansas Administrative Office of the Courts (AOC)",
  "governs": [
    "AR_FY2026_AOC_SPECIALTY_COURT_JUVENILE_DRUG_PROGRAMS_STATE_FUNDS_ACT776_SEC31"
  ],
  "effects": {
    "access_limiting": false,
    "appeal_mechanism": false
  },
  "editor_status": "pending"
}
```

---

## WHAT TO RESEARCH

**Primary Source:** Arkansas Code Annotated §19-5-1144 — Accountability Court Fund

**Find everything related to:**
1. Accountability Court Fund deposits and distributions
2. Act 776 of 2025 — AOC appropriations
3. Specialty Court programs (Drug Courts, DWI Courts, Veterans Courts, Mental Health Courts)
4. Juvenile Drug Court funding
5. Adult Drug Court funding
6. AOC budget allocations for FY2026
7. Legislative Audit reports on AOC specialty courts
8. Federal grants to Arkansas specialty courts (BJA, SAMHSA)

---

## EXACT SCHEMAS (USE THESE EXACTLY)

### 1. money_flow Schema
Generate one for EACH funding stream you find. ALL fields required:
```json
{
  "flow_id": "string - REQUIRED - unique ID starting with MF-AR- or AR_FY",
  "source": "string - REQUIRED - funding source entity name",
  "intermediary": "string - REQUIRED - pass-through entity name OR exactly 'None'",
  "destination": "string - REQUIRED - receiving entity name",
  "amount": "integer - REQUIRED - USD amount, use 0 if unknown",
  "fund_type": "string - REQUIRED - must be exactly: 'state' OR 'federal' OR 'settlement'",
  "fiscal_year": "string - REQUIRED - format: '2026' or '2025-2026'",
  "restrictions": {
    "medicaid": "boolean - REQUIRED - true if Medicaid-reimbursable",
    "dhs_controlled": "boolean - REQUIRED - true if DHS-disbursed"
  },
  "statutory_basis": "string - REQUIRED - legal citation authorizing this flow",
  "editor_status": "string - REQUIRED - always use 'pending'"
}
```
**Example:**
```json
{
  "flow_id": "MF-AR-AOC-DRUG-COURT-FY2026",
  "source": "Arkansas General Revenue Fund",
  "intermediary": "None",
  "destination": "Arkansas Administrative Office of the Courts",
  "amount": 300000,
  "fund_type": "state",
  "fiscal_year": "2026",
  "restrictions": {
    "medicaid": false,
    "dhs_controlled": false
  },
  "statutory_basis": "Act 776 of 2025, Section 31; ACA §19-5-1144",
  "editor_status": "pending"
}
```

### 2. authority_reference Schema
Generate one for EACH statute/regulation you find. ALL fields required:
```json
{
  "authority_id": "string - REQUIRED - unique ID starting with AUTH-AR- or AR-AUTH-",
  "authority_type": "string - REQUIRED - must be exactly: 'statute' OR 'regulation' OR 'policy'",
  "citation": "string - REQUIRED - formal legal citation",
  "administering_body": "string - REQUIRED - agency/entity with authority",
  "governs": "array of strings - REQUIRED - list what this authority governs",
  "effects": {
    "access_limiting": "boolean - REQUIRED - true if limits access",
    "appeal_mechanism": "boolean - REQUIRED - true if has appeal process"
  },
  "editor_status": "string - REQUIRED - always use 'pending'"
}
```
**Example:**
```json
{
  "authority_id": "AUTH-AR-ACA-16-98-101",
  "authority_type": "statute",
  "citation": "Ark. Code Ann. § 16-98-101",
  "administering_body": "Arkansas Administrative Office of the Courts",
  "governs": ["Drug Court Program establishment", "Drug Court eligibility criteria"],
  "effects": {
    "access_limiting": false,
    "appeal_mechanism": true
  },
  "editor_status": "pending"
}
```

### 3. evidence_item Schema
Generate one for EACH document/source you find. ALL fields required:
```json
{
  "evidence_id": "string - REQUIRED - unique ID starting with EVID-AR- or EV-AR-",
  "section": "string - REQUIRED - ID of related money_flow or authority_reference",
  "claim_summary": "string - REQUIRED - what this evidence proves",
  "evidence_type": "string - REQUIRED - must be exactly: 'budget' OR 'audit' OR 'policy'",
  "source": {
    "title": "string - REQUIRED - document title",
    "issuing_body": "string - REQUIRED - organization that issued it",
    "url": "string - REQUIRED - direct URL to document"
  },
  "confidence_level": "string - REQUIRED - must be exactly: 'high' OR 'medium' OR 'low'",
  "editor_status": "string - REQUIRED - always use 'pending'"
}
```
**Example:**
```json
{
  "evidence_id": "EVID-AR-ACT776-2025-SEC31",
  "section": "MF-AR-AOC-DRUG-COURT-FY2026",
  "claim_summary": "Appropriates $300,000 to AOC for specialty court programs in FY2026",
  "evidence_type": "budget",
  "source": {
    "title": "Act 776 of 2025 - AOC Appropriation",
    "issuing_body": "Arkansas General Assembly",
    "url": "https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2F&file=776.pdf"
  },
  "confidence_level": "high",
  "editor_status": "pending"
}
```

### 4. field_validation Schema
Generate one for EACH audit/validation you find. ALL fields required:
```json
{
  "fv_id": "string - REQUIRED - unique ID starting with FV-AR-",
  "jurisdiction": "string - REQUIRED - always use 'Arkansas'",
  "validating_entity": "string - REQUIRED - auditor/validator name",
  "alignment_status": "string - REQUIRED - must be exactly: 'captured' OR 'open' OR 'mixed'",
  "evidence_basis": "array of strings - REQUIRED - IDs of supporting artifacts",
  "disclosure_level": "string - REQUIRED - must be exactly: 'public' OR 'restricted'",
  "editor_status": "string - REQUIRED - always use 'pending'"
}
```
**Example:**
```json
{
  "fv_id": "FV-AR-LEGAUDIT-AOC-DRUGCOURT-2024",
  "jurisdiction": "Arkansas",
  "validating_entity": "Arkansas Legislative Audit",
  "alignment_status": "captured",
  "evidence_basis": ["EVID-AR-ACT776-2025-SEC31", "AUTH-AR-ACA-16-98-101"],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

---

## OUTPUT FORMAT

Create a file with this structure containing ALL artifacts you generate:

```json
{
  "batch_id": "BATCH-AUTH-AR-ACA-19-5-1144-EXHAUSTIVE",
  "anchor_id": "AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND",
  "mode": "exhaustive",
  "generated_at": "2026-02-05",
  "total_turns": 0,
  "artifacts": {
    "money_flow": [
      { ... },
      { ... }
    ],
    "authority_reference": [
      { ... },
      { ... }
    ],
    "evidence_item": [
      { ... },
      { ... }
    ],
    "field_validation": [
      { ... },
      { ... }
    ]
  },
  "turn_log": [
    { "turn": 1, "anchor_id": "...", "anchor_type": "...", "artifacts_generated": 0 },
    { "turn": 2, "anchor_id": "...", "anchor_type": "...", "artifacts_generated": 0 }
  ],
  "research_notes": "Summary of sources consulted and why cycling stopped"
}
```

---

## TURN-BASED CYCLING INSTRUCTIONS (EXHAUSTIVE MODE)

Run as many turns as possible. Each turn uses a DIFFERENT anchor from the previous turn's output.

### Turn Pattern
The anchor type rotates in this order, then repeats:
```
authority_reference → money_flow → evidence_item → field_validation → authority_reference → ...
```

### Each Turn
1. Use the current anchor to research related artifacts
2. Generate artifacts for the OTHER THREE types (not the anchor's type)
3. Pick one output artifact to become the next turn's anchor
4. The next anchor MUST be the next type in the rotation
5. Log the turn in `turn_log`
6. Continue to next turn

### Example Flow
```
Turn 1: anchor=authority_reference → generate money_flow, evidence_item, field_validation → pick money_flow for next
Turn 2: anchor=money_flow → generate authority_reference, evidence_item, field_validation → pick evidence_item for next
Turn 3: anchor=evidence_item → generate authority_reference, money_flow, field_validation → pick field_validation for next
Turn 4: anchor=field_validation → generate authority_reference, money_flow, evidence_item → pick authority_reference for next
Turn 5: anchor=authority_reference → generate money_flow, evidence_item, field_validation → pick money_flow for next
... continue until stop condition ...
```

### Rules for Cycling
1. **Never reuse an anchor** — each turn must use a NEW artifact as anchor
2. **Track ALL used artifacts** — maintain a list so you don't repeat
3. **The anchor type rotates** in fixed order
4. **Generate MULTIPLE artifacts per slot** — as many as you can find with real data
5. **Each artifact must relate to the CURRENT turn's anchor**
6. **Continue until you cannot** — don't stop at 4 turns

### Anchor Promotion & Preservation (CRITICAL)

After each turn:
1. **SAVE the current anchor** — move it to your results pile, it's done being an anchor
2. **SAVE all generated artifacts** — they go in the results pile too
3. **PROMOTE one artifact** — pick ONE artifact of the NEXT type in rotation to become the new anchor
4. **The promoted artifact is REMOVED from results** — it's now the anchor for the next turn
5. **Never use an anchor twice** — once it's been an anchor and saved, it cannot be promoted again

**Example:**
```
Turn 1:
  Anchor: AUTH-AR-ACA-19-5-1144 (authority_reference)
  Generate: 3 money_flows, 2 evidence_items, 1 field_validation
  Save: AUTH-AR-ACA-19-5-1144 + 2 money_flows + 2 evidence_items + 1 field_validation
  Promote: MF-AR-xxx (one money_flow becomes Turn 2 anchor)

Turn 2:
  Anchor: MF-AR-xxx (money_flow)
  Generate: 2 authority_references, 3 evidence_items, 1 field_validation
  Save: MF-AR-xxx + 2 authority_references + 2 evidence_items + 1 field_validation
  Promote: EVID-AR-xxx (one evidence_item becomes Turn 3 anchor)

Turn 3:
  Anchor: EVID-AR-xxx (evidence_item)
  Generate: 1 authority_reference, 2 money_flows, 2 field_validations
  Save: EVID-AR-xxx + 1 authority_reference + 2 money_flows + 1 field_validation
  Promote: FV-AR-xxx (one field_validation becomes Turn 4 anchor)

Turn 4:
  Anchor: FV-AR-xxx (field_validation)
  Generate: 2 authority_references, 1 money_flow, 1 evidence_item
  Save: FV-AR-xxx + 1 authority_reference + 1 money_flow + 1 evidence_item
  Promote: AUTH-AR-yyy (one NEW authority_reference becomes Turn 5 anchor)

... continue rotating until no artifact of the required type exists to promote
```

**If no artifact of the required type exists to promote → STOP the cycle**

**IMPORTANT:** On Turn 5+, you may have authority_references generated from earlier turns sitting in your results. You can ONLY promote artifacts generated in the CURRENT turn — not previously saved results.

### Tracking Template
Keep a running list (grows with each turn):
```
Used Anchors:
- Turn 1: AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND (authority_reference)
- Turn 2: MF-AR-xxx (money_flow) 
- Turn 3: EVID-AR-xxx (evidence_item)
- Turn 4: FV-AR-xxx (field_validation)
- Turn 5: AUTH-AR-yyy (authority_reference)
- Turn 6: MF-AR-yyy (money_flow)
... continue ...
```

---

## STOP CONDITIONS (CRITICAL)

**STOP the cycle ONLY when:**

1. **No valid anchor available** — The current turn produced no artifact of the required type for the next anchor
2. **Research yields no new results** — You cannot find any NEW real Arkansas data related to the current anchor
3. **Sources become speculative** — You're inferring rather than citing real sources
4. **All discoverable data exhausted** — Continuing would only produce duplicates or weak artifacts

**DO NOT stop just because you hit 4 turns** — keep going if you have valid anchors and real data.

**DO NOT:**
- Generate artifacts without real source citations
- Use placeholder URLs like "https://example.com"
- Invent statute numbers or appropriation amounts
- Create artifacts just to fill a slot
- Continue cycling with weak or fabricated anchors
- Reuse an artifact that was already an anchor

**WHEN YOU STOP:**
- Record `total_turns` in the output
- Note why you stopped in `research_notes`
- Include complete `turn_log` showing all turns executed
- Quality over quantity — stop when data quality would decline

---

## SAVE LOCATION

Store all output internally. When complete, provide an export file named `batch_response_exhaustive.json` that I can download.

---

## RULES

1. **REAL DATA ONLY** — Use actual Arkansas statutes, actual appropriation amounts, actual URLs
2. **EXHAUSTIVE** — Generate as many artifacts as you can find, not just one per type
3. **UNIQUE IDs** — Every artifact needs a unique ID
4. **PENDING STATUS** — All `editor_status` fields must be `"pending"`
5. **CITE SOURCES** — Include real URLs from arkleg.state.ar.us, arcourts.gov, etc.
6. **NO PLACEHOLDERS** — Do not use `[FILL]` or `[UNKNOWN]` — if you can't find data, skip that artifact
7. **CONTINUE CYCLING** — Do not stop at 4 turns if more valid anchors exist

---

## RESEARCH STARTING POINTS

- Arkansas Code: https://advance.lexis.com/container?config=00JABhZDEzMzMzYy1hNjEyLTRkYzMtYjk2NC0zMmMxZTRhYzllMmYKAFBvZENhdGFsb2e4CaPI4cak6laXLCWyLBO9&crid=e76e7b91-3c3e-4b04-9f63-28d2ab9073bb
- Arkansas Legislature: https://www.arkleg.state.ar.us/
- Arkansas Courts: https://www.arcourts.gov/
- Arkansas Legislative Audit: https://www.arklegaudit.gov/
- Act 776 of 2025: Search arkleg.state.ar.us for "Act 776 2025"

---

## BEGIN NOW

Start your web research and generate the batch. Continue cycling until you hit a stop condition. Do not wait for further instructions.
