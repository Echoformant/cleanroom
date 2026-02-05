# SINGLE ARTIFACT BATCH CYCLING — GPT AGENT MODE (AUTHORITY-FLOW ROTATION)

You are running a Single Artifact Batch Cycling operation for Operation NAMI Clearlane.

**MODE: AUTHORITY-FLOW ROTATION** — Anchor alternates between authority_reference and money_flow only. Evidence and validation are always supporting slots.

## YOUR MISSION

Research Arkansas public-finance data and generate artifacts by rotating between authority_reference and money_flow as anchors. Continue until no more valid anchors can be produced. This is NOT a template — execute this now.

---

## CANONICAL ARTIFACT DEFINITIONS (CRITICAL)

These definitions are BINDING. Do not deviate.

### authority_reference (ANCHOR TYPE)
**Definition:** A statute, regulation, or policy that AUTHORIZES or GOVERNS an action, program, or fund.
**Use when:** The source IS the law itself — the text that creates authority.
**Contains:** Legal citations, administering bodies, what it governs.
**Examples:** Arkansas Code sections, CFR regulations, DHS policy manuals.
**NOT for:** Budget documents, audit reports, appropriation line items.

### money_flow (ANCHOR TYPE)
**Definition:** A discrete movement of funds FROM a source TO a destination, optionally through an intermediary.
**Use when:** You can identify source → destination and an amount (or authorization to move funds).
**Contains:** Funding source, pass-through entity, receiving entity, amount, fiscal year, restrictions.
**Examples:** "Act 776 appropriates $300,000 from General Revenue to AOC for Drug Courts."
**NOT for:** The statute text itself (that's authority_reference) or the document proving it (that's evidence_item).

### evidence_item (SUPPORTING TYPE — never an anchor)
**Definition:** A DOCUMENT or SOURCE that proves a claim about authority or money flow.
**Use when:** You have a citable document that supports another artifact's existence.
**Contains:** Document title, issuing body, URL, what claim it supports.
**Examples:** Budget documents, appropriation act PDFs, grant award letters, AOC annual reports.
**NOT for:** The law itself (authority_reference) or audit conclusions (field_validation).

### field_validation (SUPPORTING TYPE — never an anchor)
**Definition:** A CONFIRMATION that authority and evidence align — an audit finding, compliance check, or verification.
**Use when:** An independent entity has validated, audited, or confirmed something.
**Contains:** Validating entity, alignment status, what evidence it relies on.
**Examples:** Legislative Audit findings, federal compliance reports, AOC internal audit results.
**NOT for:** The source document (evidence_item) or the law being audited (authority_reference).

### The Two-Pole Chain
```
authority_reference (the law) 
    ↔ alternates with ↔ 
money_flow (the funds)
    
    both supported by:
    evidence_item (the proof)
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

### 1. money_flow Schema (ANCHOR TYPE)
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

### 2. authority_reference Schema (ANCHOR TYPE)
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

### 3. evidence_item Schema (SUPPORTING — never anchor)
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

### 4. field_validation Schema (SUPPORTING — never anchor)
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
  "batch_id": "BATCH-AUTH-AR-ACA-19-5-1144-AUTHFLOW",
  "anchor_id": "AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND",
  "mode": "authority-flow-rotation",
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
    { "turn": 1, "anchor_id": "...", "anchor_type": "authority_reference", "artifacts_generated": 0 },
    { "turn": 2, "anchor_id": "...", "anchor_type": "money_flow", "artifacts_generated": 0 }
  ],
  "research_notes": "Summary of sources consulted and why cycling stopped"
}
```

---

## TURN-BASED CYCLING INSTRUCTIONS (AUTHORITY-FLOW ROTATION)

Run as many turns as possible. Anchor alternates ONLY between authority_reference and money_flow.

### Turn Pattern (TWO-POLE ROTATION)
```
authority_reference → money_flow → authority_reference → money_flow → ...
```

Evidence_item and field_validation are ALWAYS supporting slots — they NEVER become anchors.

### Each Turn Structure

**When anchor is authority_reference:**
- Generate: money_flow(s), evidence_item(s), field_validation(s)
- Promote: ONE money_flow becomes next anchor
- Save: The authority_reference anchor + all other money_flows + all evidence_items + all field_validations

**When anchor is money_flow:**
- Generate: authority_reference(s), evidence_item(s), field_validation(s)
- Promote: ONE authority_reference becomes next anchor
- Save: The money_flow anchor + all other authority_references + all evidence_items + all field_validations

### Example Flow
```
Turn 1: 
  Anchor: AUTH-AR-ACA-19-5-1144 (authority_reference)
  Generate: 3 money_flows, 2 evidence_items, 1 field_validation
  Save: AUTH-AR-ACA-19-5-1144 + 2 money_flows + 2 evidence_items + 1 field_validation
  Promote: MF-AR-xxx (one money_flow becomes Turn 2 anchor)

Turn 2: 
  Anchor: MF-AR-xxx (money_flow)
  Generate: 2 authority_references, 3 evidence_items, 1 field_validation
  Save: MF-AR-xxx + 1 authority_reference + 3 evidence_items + 1 field_validation
  Promote: AUTH-AR-yyy (one authority_reference becomes Turn 3 anchor)

Turn 3:
  Anchor: AUTH-AR-yyy (authority_reference)
  Generate: 2 money_flows, 1 evidence_item, 2 field_validations
  Save: AUTH-AR-yyy + 1 money_flow + 1 evidence_item + 2 field_validations
  Promote: MF-AR-zzz (one money_flow becomes Turn 4 anchor)

Turn 4:
  Anchor: MF-AR-zzz (money_flow)
  Generate: 1 authority_reference, 2 evidence_items, 0 field_validations
  Save: MF-AR-zzz + 0 authority_references + 2 evidence_items + 0 field_validations
  Promote: NONE — no authority_reference generated → STOP

... cycle ends when no artifact of the required anchor type exists
```

### Rules for Cycling
1. **Anchor alternates:** authority_reference → money_flow → authority_reference → money_flow → ...
2. **evidence_item and field_validation are NEVER anchors** — always supporting slots
3. **Never reuse an anchor** — each turn must use a NEW artifact as anchor
4. **Track ALL used artifacts** — maintain a list so you don't repeat
5. **Generate MULTIPLE artifacts per slot** — as many as you can find with real data
6. **Each artifact must relate to the CURRENT turn's anchor**
7. **Continue until you cannot** — don't stop after any fixed number of turns

### Anchor Promotion & Preservation (CRITICAL)

After each turn:
1. **SAVE the current anchor** — move it to your results pile, it's done being an anchor
2. **SAVE all evidence_items and field_validations** — they always go to results (never promoted)
3. **SAVE all but one of the next anchor type** — the extras go to results
4. **PROMOTE one artifact** of the NEXT anchor type (alternating authority↔money_flow)
5. **The promoted artifact is REMOVED from results** — it's now the anchor for the next turn
6. **Never use an anchor twice** — once saved, it cannot be promoted again

**If no artifact of the required anchor type exists to promote → STOP the cycle**

**IMPORTANT:** You can ONLY promote artifacts generated in the CURRENT turn — not previously saved results.

### Tracking Template
Keep a running list (grows with each turn):
```
Used Anchors:
- Turn 1: AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND (authority_reference)
- Turn 2: MF-AR-xxx (money_flow) 
- Turn 3: AUTH-AR-yyy (authority_reference)
- Turn 4: MF-AR-zzz (money_flow)
- Turn 5: AUTH-AR-aaa (authority_reference)
... continue until no more anchors available ...
```

---

## STOP CONDITIONS (CRITICAL)

**STOP the cycle ONLY when:**

1. **No valid anchor available** — The current turn produced no money_flow (if authority was anchor) or no authority_reference (if money_flow was anchor)
2. **Research yields no new results** — You cannot find any NEW real Arkansas data related to the current anchor
3. **Sources become speculative** — You're inferring rather than citing real sources
4. **All discoverable authority↔flow relationships exhausted** — Continuing would only produce duplicates or weak artifacts

**DO NOT stop just because you hit any fixed number of turns** — keep going if you have valid anchors and real data.

**DO NOT:**
- Generate artifacts without real source citations
- Use placeholder URLs like "https://example.com"
- Invent statute numbers or appropriation amounts
- Create artifacts just to fill a slot
- Continue cycling with weak or fabricated anchors
- Reuse an artifact that was already an anchor
- Promote evidence_item or field_validation to anchor (they are NEVER anchors)

**WHEN YOU STOP:**
- Record `total_turns` in the output
- Note why you stopped in `research_notes`
- Include complete `turn_log` showing all turns executed
- Quality over quantity — stop when data quality would decline

---

## SAVE LOCATION

Store all output internally. When complete, provide an export file named `batch_response_authflow.json` that I can download.

---

## RULES

1. **REAL DATA ONLY** — Use actual Arkansas statutes, actual appropriation amounts, actual URLs
2. **EXHAUSTIVE** — Generate as many artifacts as you can find, not just one per type
3. **UNIQUE IDs** — Every artifact needs a unique ID
4. **PENDING STATUS** — All `editor_status` fields must be `"pending"`
5. **CITE SOURCES** — Include real URLs from arkleg.state.ar.us, arcourts.gov, etc.
6. **NO PLACEHOLDERS** — Do not use `[FILL]` or `[UNKNOWN]` — if you can't find data, skip that artifact
7. **TWO-POLE ROTATION** — Only authority_reference and money_flow can be anchors
8. **CONTINUE CYCLING** — Do not stop at any fixed number of turns if more valid anchors exist

---

## RESEARCH STARTING POINTS

- Arkansas Code: https://advance.lexis.com/container?config=00JABhZDEzMzMzYy1hNjEyLTRkYzMtYjk2NC0zMmMxZTRhYzllMmYKAFBvZENhdGFsb2e4CaPI4cak6laXLCWyLBO9&crid=e76e7b91-3c3e-4b04-9f63-28d2ab9073bb
- Arkansas Legislature: https://www.arkleg.state.ar.us/
- Arkansas Courts: https://www.arcourts.gov/
- Arkansas Legislative Audit: https://www.arklegaudit.gov/
- Act 776 of 2025: Search arkleg.state.ar.us for "Act 776 2025"

---

## BEGIN NOW

Start your web research and generate the batch. Alternate anchors between authority_reference and money_flow until you hit a stop condition. Do not wait for further instructions.
