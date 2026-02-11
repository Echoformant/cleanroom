# PULSE DUMP — 2026-02-10

---

## Pulse 1: Opioid Settlement Tracing Playbook

---
pulse_number: 1
temporal_hash: "#021020261415"
thread_title: "Opioid Settlement Tracing with Deterministic Linkage"
version: 1.0
status: promoted
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - playbook_candidate
  - money_flow_candidate
  - validation_candidate

priority: high
impact: foundational

topics:
  - opioid_settlement
  - specialty_courts
  - aoc
  - authority_chain

related_pulses: []
fills_gaps:
  - "MISSING_VALIDATION:MF-AR-OPIOID-*"
strengthens:
  - "AUTH-AR-ARORP"
  - "AUTH-AR-ACT691-2025"

created_at: "2026-02-10T14:15:00Z"
promoted_to:
  - "_agent_runs/playbook_opioid_settlement_tracing.md"
---

### The Big Idea

Field-ready playbook for tracing opioid-settlement dollars from source to service with deterministic links.

### Three High-Yield Audit Hooks

**1. Distribution Agreements (Exhibit E)**
- Master allocation schedule: defendants → state share → in-state subdivisions
- Canonical "origin → allocation" key
- Every payment/subaward reconciles back to Exhibit E line item

**2. Recurring Payment Schedules**
- Year-by-year timetables with due dates, paid-to-date, shortfalls/interest
- Time-bounded cash-in events
- Validates treasury deposits, catches missing receipts

**3. Third-Party Subgrantee MOUs**
- Agreements from state program (ARORP/AG/AOC/DHS) to downstream implementers
- Encodes authority chain, scope restrictions, CFDA tags, reporting obligations
- Deterministic bridge from settlement pool to services

### Deterministic Linkage Keys (MANDATORY)

| Key | Composite Structure |
|-----|---------------------|
| `exhibit_e_id` | `(defendant_group, state_code, subdivision_id, allocation_pct)` |
| `payment_schedule_id` | `(defendant_group, year, due_date, amount_due)` |
| `treasury_receipt_id` | `(fund_code, journal_id, post_date, amount)` |
| `mou_id` | `(grantor_prog_code, subgrantee_ein, start_end, oblig_amt)` |
| `program_object_code` | State object/fund code for ledger validation |

### Operational Workflow

1. **Anchor**: Create `authority_reference` for settlement; attach Exhibit E as `evidence_item`
2. **Inbounds**: For each due year/defendant, instantiate `money_flow` (receipt); validate with treasury
3. **Outbounds**: For each subaward/MOU, instantiate `money_flow` (obligation); bind to lineage
4. **Reconcile**: Yearly: `Σ receipts` ≟ `Σ obligations + expenditures + ending balance`

### QA Flags

- Missing lineage (no `exhibit_e_id` or `payment_schedule_id`)
- Timing mismatch (deposit >30 days after due date)
- Scope drift (MOU purpose not in allowables)
- Orphan MOUs (no matching treasury disbursement)
- Residuals (large balance without encumbrance notes)

**Promotion Note:** Full playbook created at `_agent_runs/playbook_opioid_settlement_tracing.md` with complete schema specs, starter stubs, and CSV template.

---

## Pulse 2: ACT 691 Authority Chain Discovery

---
pulse_number: 2
temporal_hash: "#021020261430"
thread_title: "ACT 691 Controls Everything We Didn't Map"
version: 1.0
status: promoted
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - authority_candidate
  - money_flow_candidate
  - entity_candidate
  - gap_fill_candidate

priority: critical
impact: foundational

topics:
  - specialty_courts
  - aoc
  - opioid_settlement
  - appropriations
  - authority_chain

related_pulses:
  - "#021020261415"
fills_gaps:
  - "INCOMPLETE_CHAIN:AUTH-AR-SPECIALTY-COURT-*"
  - "MISSING_VALIDATION:MF-AR-SPECIALTY-COURT-*"
strengthens: []

created_at: "2026-02-10T14:30:00Z"
promoted_to:
  - "authority_reference/AUTH-AR-ACT691-2025.json"
  - "authority_reference/AUTH-AR-SCPAC.json"
  - "authority_reference/AUTH-AR-ARORP.json"
  - "money_flow/MF-AR-SPECIALTY-COURT-USER-FEE.json"
  - "money_flow/MF-AR-SPECIALTY-COURT-FUND-DISTRIBUTION.json"
  - "money_flow/MF-AR-OPIOID-SETTLEMENT-AG-SPECIALTY-COURTS.json"
  - "money_flow/MF-AR-LOCAL-DRUG-COURT-FEE-COUNTY.json"
  - "entity_registry/ENTITY-AR-SCPAC.json"
  - "entity_registry/ENTITY-AR-ARORP.json"
  - "entity_registry/ENTITY-AR-AOC.json"
  - "entity_registry/ENTITY-AR-AG-OPIOID-FUND.json"
---

### The Big Idea

ACT 691 (2025) is a major gatekeeper for specialty court funding that we had ZERO coverage on. One act controls:

- **Approval authority** for ALL specialty courts (Supreme Court + SCPAC)
- **Fee collection** ($250/participant → State Treasury)
- **AOC distribution formula** (reviewed by SCPAC, approved by Legislative Council)
- **Opioid settlement routing** ($1M+ through AG → AOC → specialty courts)
- **Local quorum court control** over local drug court funds
- **DCC/DHS treatment slots** (subject to appropriation)

### Who Decides What Gets Funded

| Step | Decision-Maker | Mechanism |
|------|----------------|-----------|
| 1. Approval | Supreme Court + SCPAC | Administrative plan (Orders 14 & 18) |
| 2. Appropriation | General Assembly | Acts with position authorization |
| 3. Distribution | AOC | Formula (SCPAC review, Legislative Council approval) |
| 4. Local funds | County Quorum Courts | Local fee fund appropriation |
| 5. Opioid $ (state) | Attorney General | Grant approval from state share |
| 6. Opioid $ (local) | ARORP | Proposal process with county/mayor signature |

### Key Entities Discovered

- **SCPAC** (Specialty Court Program Advisory Committee) — evaluates programs, reviews formulas, refers findings to Supreme Court
- **ARORP** (Arkansas Opioid Recovery Partnership) — manages 2/3 of opioid settlement (county + municipal shares)
- **AG Opioid Fund** — manages 1/3 of opioid settlement (state share)
- **AOC** — central administrator for specialty court funding

### Fee Flow

```
Participants → $250 fee → Circuit/District Courts → State Treasury (Specialty Court Program Fund) → AOC (formula distribution) → Approved Drug Courts
```

### Opioid Settlement Split

```
National Settlement
├── 1/3 → State (AG manages) → can grant to specialty courts via AOC
└── 2/3 → ARORP
    ├── 1/3 → Counties (proposal process)
    └── 1/3 → Municipalities (proposal process)
```

### What This Unlocks

- Complete approval chain for specialty courts
- Three separate funding streams mapped (fees, appropriations, opioid settlement)
- Entity registry bootstrap (SCPAC, ARORP, AOC, AG Opioid Fund)
- Foundation for mapping all 45 drug courts by judicial district

**Promotion Note:** Created 3 authority artifacts, 4 money flow artifacts, 4 entity registry entries, 2 evidence items.

---

## Pulse 3: Entity Registry Schema Proposal

---
pulse_number: 3
temporal_hash: "#021020261445"
thread_title: "Key Registry for Arkansas Orgs/Positions"
version: 1.0
status: promoted
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - entity_candidate

priority: high
impact: foundational

topics:
  - entity_registry
  - dhs
  - aoc
  - authority_chain

related_pulses:
  - "#021020261430"
fills_gaps:
  - "ORPHAN_REFERENCE:*"
strengthens: []

created_at: "2026-02-10T14:45:00Z"
promoted_to:
  - "entity_registry/README.md"
---

### The Big Idea

Need a canonical registry of organizations, offices, positions, and programs that appear in Arkansas public finance artifacts. Provides "who is who" for the org hierarchy.

### Entity Types

| Type | Description | Examples |
|------|-------------|----------|
| `agency` | State-level department | DHS, AOC, DFA |
| `division` | Major subdivision | DAABHS, DMS |
| `office` | Office within division | OSAMH |
| `position` | Named role | Drug Director, OSAMH Director |
| `committee` | Advisory/governance body | SCPAC, Legislative Council |
| `partnership` | Multi-entity collaborative | ARORP |
| `provider` | Service delivery org | CMHCs |
| `court` | Judicial entity | Drug Court (by district) |
| `program` | Funded program | Veterans Treatment Court |

### Schema

```json
{
  "entity_id": "ENTITY-AR-DHS-OSAMH",
  "entity_type": "office",
  "name": "Office of Substance Abuse and Mental Health",
  "abbreviation": "OSAMH",
  "parent": "ENTITY-AR-DHS-DAABHS",
  "children": ["ENTITY-AR-DHS-OSAMH-DIRECTOR"],
  "authorities": ["AUTH-AR-ACA-20-46-*"],
  "controls": ["MF-AR-OSAMH-*"],
  "fiscal_agent": true,
  "medicaid_provider": false,
  "editor_status": "pending"
}
```

### ID Patterns

| Pattern | Meaning |
|---------|---------|
| `ENTITY-AR-DHS` | Arkansas DHS (top-level) |
| `ENTITY-AR-DHS-DAABHS` | Division under DHS |
| `ENTITY-AR-DHS-OSAMH-DIRECTOR` | Position within office |
| `ENTITY-AR-AOC-DRUG-COURT-DIST01` | Specific court program |
| `ENTITY-AR-CMHC-OZARK` | Community Mental Health Center |

### Priority Entities to Populate

1. DHS hierarchy (DAABHS → OSAMH → positions)
2. AOC + SCPAC
3. ARORP + AG opioid administration
4. 45 Drug Courts (by judicial district)
5. CMHCs
6. Key federal sources (SAMHSA, DOJ BJA, HRSA)

**Promotion Note:** Created `entity_registry/` folder with README.md schema documentation and 4 initial entity entries.

---

## Pulse 4: Data Completeness Gaps

---
pulse_number: 4
temporal_hash: "#021020261500"
thread_title: "937 Artifacts But Most Are Hollow"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - gap_fill_candidate

priority: critical
impact: tactical

topics:
  - appropriations
  - samhsa
  - peer_support
  - medicaid

related_pulses: []
fills_gaps: []
strengthens: []

created_at: "2026-02-10T15:00:00Z"
promoted_to: []
---

### The Big Idea

937 artifacts sounds impressive but actual data quality is poor:

### Coverage Analysis

| Metric | Current | Problem |
|--------|---------|---------|
| Money flows with $ amount | 114 of 216 | Half have no dollar amounts |
| FY2026 tagged | 1 | Almost nothing current |
| SAMHSA mentions | 13 | Massively underrepresented |
| Peer support mentions | 11 | Barely exists |
| Field validations | 197 | But 372 artifacts have NO validation |

### Gap Summary

| Gap Type | Count |
|----------|-------|
| INCOMPLETE_CHAIN | 53 |
| MISSING_VALIDATION | 372 |
| Total gaps | 425 |

### Priority Data Sources Needed

1. **FY2026 appropriation acts** — section-by-section with dollar amounts
2. **Federal grant awards** — SAMHSA TI grants, State Opioid Response
3. **Peer certification authority** — Medicaid reimbursement chain
4. **DHS org chart PDFs** — establish full hierarchy
5. **AOC drug court directory** — list all 50+ programs
6. **County financial reports** — Quorum Court minutes (public)

### What Makes Data "Real"

- Has dollar amount (not 0)
- Has fiscal year (current or specific)
- Has statutory_basis_refs (linked to authority)
- Has field_validation (independently verified)
- Has evidence_item support

**Promotion Note:** Not yet promoted. Needs data collection before artifacts can be created.

---

## Pulse 5: Navigator Enhancements

---
pulse_number: 5
temporal_hash: "#021020261330"
thread_title: "Navigator HTML Features"
version: 1.0
status: promoted
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - toolbox_candidate

priority: medium
impact: tactical

topics:
  - visualization

related_pulses: []
fills_gaps: []
strengthens: []

created_at: "2026-02-10T13:30:00Z"
promoted_to:
  - "_data/navigator.html"
---

### Features Implemented

1. **Agency/Entity Filter** — dynamically populated from classifications, filters by DHS/AOC/SAMHSA/etc.

2. **Path Finder** — "show me how X connects to Y"
   - BFS shortest path algorithm
   - Highlights path with enlarged nodes and green edges
   - Step-by-step path list display

3. **Question Interface** — free-text with quick buttons
   - "What authorities govern drug courts?"
   - "Where does SAMHSA money go?"
   - "Show Medicaid money flows"
   - "What does DHS control?"

### Potential Future Features

- FY timeline slider
- Dollar amount range filter
- Export to CSV/JSON
- Keyboard shortcuts
- URL state saving (shareable links)
- Sankey diagram (separate page)

**Promotion Note:** All three features implemented in `_data/navigator.html`.

---

## Pulse 6: Arkansas Transparency Portal as Anchor Data Source

---
pulse_number: 6
temporal_hash: "#021020261915"
thread_title: "Tracing AOC Grants & Aid through FY2026"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - evidence_candidate
  - money_flow_candidate
  - data_source_candidate
  - validation_candidate

priority: high
impact: foundational

topics:
  - transparency_portal
  - aoc
  - grants_aid
  - expenditures
  - county_payments
  - act_303

related_pulses:
  - "#021020261430"
  - "#021020261415"
fills_gaps:
  - "MISSING_VALIDATION:MF-AR-AOC-*"
strengthens:
  - "MF-AR-SPECIALTY-COURT-FUND-DISTRIBUTION"
creates_authority:
  - "AUTH-AR-ACT303"

sources:
  - url: "https://transparency.arkansas.gov/"
    title: "Transparency.Arkansas.gov – Homepage"
  - url: "https://www.ark.org/dfa/transparency/payments.php"
    title: "Payments to Cities & Counties"
  - url: "https://www.ark.org/dfa/transparency_2025/expenditures.php"
    title: "Expenditures by Classification"
  - url: "https://transparency.arkansas.gov/about.html"
    title: "About this Site - Act 303 basis"

created_at: "2026-02-10T19:15:00Z"
promoted_to: []
---

### The Big Idea

Transparency.Arkansas.gov is a daily-updated, downloadable, field-level expenditure database authorized by Act 303. It gives you deterministic join keys to validate money flows from state agencies (including AOC) down to vendor-level transactions — and a separate slice specifically for payments to cities and counties.

### Why This Matters Now

This directly attacks Pulse 4's biggest gap — money flows with no dollar amounts. The portal has actual FY2026 transaction-level data with amounts, vendors, classifications, and dates. This is the evidence layer that makes hollow artifacts real.

### Data Assets Available

| Dataset | Granularity | Update Frequency |
|---------|-------------|-----------------|
| Expenditures | Agency → Vendor → Transaction | Daily |
| Payments to Cities & Counties | Agency → Local Gov → Amount | Daily |
| Revenue | Source → Agency → Amount | Daily |

### Join Keys for Cross-Referencing

| Field | Use |
|-------|-----|
| `fiscal_year` | Temporal alignment |
| `agency` | Source entity match |
| `vendor_name` | Destination entity match (needs normalization) |
| `classification` | GRANTS/AID filter |
| `warrant_id / transaction_id` | Deterministic receipt match |
| `fund_code` | Program-level tracing |
| `object_code` | Expenditure type classification |
| `amount` | Dollar validation |

### Deterministic Validation Path

```
Clearlane money_flow artifact (e.g., MF-AR-AOC-DRUG-COURT-DIST01-FY2026)
  → match agency (AOC) + classification (GRANTS/AID) + vendor (county/court program)
  → pull warrant_id + amount + date from portal export
  → create evidence_item with transaction-level proof
  → field_validation: PASS (amount reconciles, warrant exists)
```

### County Cross-Reference Potential

Portal exports can be joined to county check registers using:
- `fiscal_year` + `warrant_id` + `vendor_name` normalization
- This bridges state-level disbursement to county-level receipt — closing the loop

### Authority Basis

- **Act 303** — mandates the portal's existence and defines what gets published
- Expenditures defined as warrants, direct deposits, electronic transfers
- This is itself an `authority_reference` candidate (see `creates_authority` above)

### Immediate Actions

1. Download FY2026 AOC expenditures filtered by GRANTS/AID classification
2. Normalize vendor names against entity registry
3. Match to existing money_flow artifacts — fill dollar amounts
4. Create evidence_items from transaction records
5. Run field_validation against matched pairs

### What This Unlocks

- Real dollar amounts for AOC money flows (kills the hollow artifact problem)
- Transaction-level evidence for opioid settlement disbursements
- County-level receipt validation
- Daily-updated data means artifacts can stay current

**Promotion Note:** Not yet promoted. Needs FY2026 AOC export downloaded and normalized before artifacts can be hardened.

---

## Pulse 7: FIS Data Spine — Canonical Identity Architecture

---
pulse_number: 7
temporal_hash: "#021020261930"
thread_title: "Building the Data Spine for AR Nonprofits + Court-Aligned Programs"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - entity_candidate
  - key_registry_candidate
  - fis_foundation

priority: critical
impact: foundational

topics:
  - key_registry
  - data_spine
  - ein
  - uei
  - aln
  - fain
  - npi
  - eo_bmf
  - usaspending
  - transparency_portal
  - census_cbp

related_pulses:
  - "#021020261915"
  - "#021020261445"
  - "#021020261430"
fills_gaps:
  - "ORPHAN_REFERENCE:*"
strengthens:
  - "ENTITY-AR-*"
creates_artifact:
  - "key_registry.yaml"

created_at: "2026-02-10T19:30:00Z"
promoted_to: []
---

### The Big Idea

The Funding Intelligence System needs a single identity spine that connects seven federal/state/local identifier systems into one joinable structure — without drifting into DHS lanes. EIN is the canonical key. Everything else joins to it.

### The Seven Anchor ID Systems

| ID | Source | Refresh | Role |
|----|--------|---------|------|
| EIN | IRS TEOS/990 | Monthly | Canonical org key |
| EO BMF | IRS | Monthly | Active status, NTEE, address |
| UEI | SAM.gov / USAspending | Varies | Federal award identity |
| FAIN | USAspending | Varies | Specific award instance |
| ALN | SAM.gov | Stable | Program definition (formerly CFDA) |
| State Payee | Transparency.Arkansas.gov | Daily | Vendor-level spend |
| NPI | NPPES/CMS | Monthly | Health provider identity |

### Join Map

```
EIN (canonical)
├── 1:1 → EO_BMF (name, address, NTEE, status)
├── fuzzy → UEI (name+address normalization, persist match score)
│   └── exact → FAIN → ALN (federal award chain)
├── fuzzy → State Payee (normalize AR payee strings)
├── conditional → NPI (clinical partners only)
└── geographic → County FIPS → Census CBP (NAICS 62/813)
```

### Critical Design Decisions

1. **EIN is king.** Everything resolves to EIN first. No EIN, no spine entry.
2. **Fuzzy joins get scored.** EIN↔UEI and EIN↔State Payee are fuzzy by nature. Persist `match_score`, `match_method`, and keep an unresolved bucket. Never force a match.
3. **ALN is the narrative bridge.** It connects "program intent" (what Congress funded) to "award instance" (who got the money). This is the semantic layer between authority and money.
4. **NPI is conditional.** Only needed for clinical/behavioral health provider joins. Don't over-collect.
5. **Census CBP is context, not identity.** NAICS 62 (health/social assistance) and 813 (nonprofits) by county gives you capacity baseline. Doesn't join to individual orgs.

### Three Signal Patterns

| Pattern | What It Reveals | Data Sources |
|---------|-----------------|--------------|
| Sprawl | Small orgs filing 990-N with only 8 fields | EO BMF + State Payee fill the gaps |
| Converge | Award-bearing orgs with recurring federal flows | UEI/ALN/FAIN clustering |
| Harden | Stable anchors with year-over-year consistency | Same ALN/agency + daily AR payments |

### Unresolved Match Bucket (MANDATORY)

State payee names will NOT cleanly match EIN/UEI records. Rules:

- Keep every unresolved match in a separate table
- Document what was tried (name normalization, address, fuzzy score)
- Never discard — unresolved matches are data, not failures
- Review periodically as new identifiers surface

### Relationship to Existing Infrastructure

- **Key Registry** → this IS the key registry's full design. Current `key_registry.yaml` is the seed.
- **Moonlight 990 data** → provides the EIN-keyed historical layer. 10 years of spine-ready data.
- **Transparency Portal (Pulse 6)** → provides the state payee side of the fuzzy join.
- **Entity Registry (Pulse 3)** → provides the org hierarchy that sits on TOP of the spine.

### What This Is NOT

- Not a CRM
- Not a grant eligibility tool
- Not a live funding tracker
- It's an identity resolution layer that makes everything else joinable

**Promotion Note:** Not yet promoted. Key registry seed exists. Full spine requires EIN→UEI matching infrastructure and state payee normalization rules. This is FIS foundation — survives beyond Clearlane.

---

## Pulse 8: Medicaid Trigger Glossary — DHS Capture Prevention Language Guide

---
pulse_number: 8
temporal_hash: "#021020261945"
thread_title: "Quick Reference: Medicaid Trigger Terms"
version: 1.0
status: promoted
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - operational_guide
  - dhs_capture_prevention
  - grant_writing_tool
  - clearlane_core

priority: critical
impact: immediate

topics:
  - medicaid
  - dhs_capture
  - language_safety
  - grant_writing
  - mou_drafting
  - peer_support
  - education_framing

related_pulses:
  - "#021020261430"
  - "#021020261415"
fills_gaps:
  - "MISSING_VALIDATION:clearlane_language_safety"
strengthens:
  - "AUTH-AR-MEDICAID-*"
  - "MF-AR-DHS-*"

created_at: "2026-02-10T19:45:00Z"
promoted_to:
  - "docs/medicaid_trigger_glossary_v1.yaml"
---

### The Big Idea

Certain words and phrases in grant narratives, MOUs, websites, and program descriptions silently reroute NAMI into DHS/Medicaid jurisdiction. This glossary is a find-and-replace defense system. Red terms trigger capture. Green terms keep you in the education-only clearlane.

### Why This Is Arguably the Most Important Pulse

Every other pulse builds infrastructure. This one keeps the infrastructure safe. It doesn't matter how good your authority chain mapping is if someone writes "peer support" in a grant narrative and DHS captures the program. This is the operational layer that touches every document NAMI produces.

### The Three Lanes

| Lane | Rule | Example |
|------|------|---------|
| RED | Prohibit in all public docs | "peer support" → implies Medicaid-regulated role |
| AMBER | Rewrite with explicit non-clinical qualifier | "referral" → "court-to-education referral" |
| GREEN | Safe for court/education framing | "psychoeducation workshop", "skills practice" |

### Core Substitutions (the cheat sheet)

| Kill This | Use This |
|-----------|----------|
| peer support / peer specialist / PRSS / CRS | trained community facilitator (non-clinical) |
| recovery support services / RSS | non-clinical education workshop / skills session |
| care coordination / case management | participant coordination (admin, non-clinical) |
| treatment plan | learning plan / session plan |
| clinical assessment / diagnosis | readiness survey (non-diagnostic) |
| referral to treatment | information handoff to community education |
| billing provider / rendering provider / NPI | program operator (non-billing) |
| medical necessity / prior authorization | omit or "court-aligned eligibility (education program)" |
| Medicaid-eligible / CPT / HCPCS / MCO | omit or "publicly-funded (non-health-care)" |

### The Banner (paste at top of every RFP/MOU)

> "NAMI services described herein are education-only, non-clinical, and not billed to Medicaid. No diagnosis, treatment, or Medicaid billing."

### Five Declarations for Every Public Document

1. **Scope:** "NAMI provides education-only, non-clinical services."
2. **Lane:** "Justice-referred participants are served inside existing education infrastructure."
3. **Roles:** "Facilitators are non-clinical instructors; no Medicaid-recognized credentials required or implied."
4. **Data:** "We track process/learning metrics — no PHI/claims data."
5. **Partners:** "If a partner bills Medicaid, NAMI's role remains non-billing education; no incident-to/under-supervision relationships."

### What This Enables for Tricia

This is something she can use TODAY. No graph viewer needed. No Power BI. No LLM. Print it out and tape it to the wall. Every time she writes a grant, an MOU, or a program description, she runs it through this list.

This might be the single most useful thing you hand her before you leave.

**Promotion Note:** YAML config created. Candidate for standalone printable one-pager, custom GPT system prompt, and STRATA lint rule.

---

## Pulse 9: FOIA Strategy — DHS Delegation of Authority Records

---
pulse_number: 9
temporal_hash: "#021020262000"
thread_title: "FOIAing DHS Delegation Records"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - evidence_candidate
  - authority_candidate
  - control_surface_candidate
  - intelligence_collection

priority: high
impact: foundational

topics:
  - foia
  - dhs
  - osamh
  - dms_medicaid
  - delegation_of_authority
  - control_surface
  - signature_authority

related_pulses:
  - "#021020261430"
  - "#021020261445"
  - "#021020261945"
fills_gaps:
  - "INCOMPLETE_CHAIN:AUTH-AR-DHS-OSAMH-*"
  - "INCOMPLETE_CHAIN:AUTH-AR-DHS-DMS-*"
strengthens:
  - "ENTITY-AR-DHS-OSAMH"
  - "ENTITY-AR-DHS-DMS"

created_at: "2026-02-10T20:00:00Z"
promoted_to: []
---

### The Big Idea

Statutes tell you what the law says. Delegation memos tell you which desk controls the switch. Without these, Clearlane maps authority to agencies but can't resolve to the actual human or office that approves, blocks, or routes. This FOIA targets the gap between statutory authority and operational control inside DHS — specifically OSAMH and DMS/Medicaid.

### Why This Is Critical for Clearlane

The entire point of Clearlane is avoiding DHS capture. But you can't avoid what you can't see. Right now the authority chain stops at the agency level. Delegation memos reveal:

- Which desk sets standards for behavioral health programs
- Which desk approves or rejects provider/court program participation
- Which desk signs off on grant acceptance
- Which desk controls evaluation and compliance reporting
- Where cross-agency MOUs hand off decision rights

These are the invisible choke points.

### What Gets Requested

| Record Type | What It Reveals |
|-------------|-----------------|
| Delegation orders/memos | Who the agency head gave power to |
| Internal management directives | Rulemaking, policy issuance, program approvals |
| Signature authority matrices | Who can sign what — the actual control map |
| Routing sheets | How decisions flow through the bureaucracy |
| Cross-agency MOUs | Where OSAMH/DMS receives or gives away power |
| Superseded versions | When and how control shifted over time |

### Dual-Target Strategy

Send to THREE offices simultaneously:

1. **DHS central legal** — parent department records custodian
2. **OSAMH program office** — behavioral health specific
3. **DMS/Medicaid** — Medicaid operations specific

CC all three on each request. Eliminates "not in our custody" deflection.

### Intake Schema for Returns

Each returned memo gets structured as:

- `delegated_power` — what authority was given
- `effective_date` — when it took effect
- `supersedes` — what it replaced
- `signatory` — who signed it
- `program_scope` — what programs it covers
- `control_edges` — who gains/loses decision rights

### Temporal Intelligence

Requesting superseded versions (last 5-10 years) is the real play. It shows:

- Control shifts over time
- Whether current delegation matches what statutes imply
- Whether authority was quietly moved before or after policy changes
- Pattern of centralization vs decentralization

**Promotion Note:** Not yet promoted. FOIA template is ready to send. Intake schema needs to be formalized before returns arrive. This is a collection action — value depends on what comes back.

---

## Pulse 10: Court Orders as Federal Funding Levers

---
pulse_number: 10
temporal_hash: "#021020262015"
thread_title: "When Court Orders Unlock Funding"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - authority_candidate
  - money_flow_candidate
  - funding_strategy
  - clearlane_core
  - time_sensitive

priority: critical
impact: immediate

topics:
  - specialty_courts
  - aoc
  - supreme_court
  - samhsa
  - bja_doj
  - 988
  - nofo
  - court_authority
  - federal_funding

related_pulses:
  - "#021020261430"
  - "#021020261415"
  - "#021020261945"
  - "#021020262000"
fills_gaps:
  - "INCOMPLETE_CHAIN:AUTH-AR-SPECIALTY-COURT-TO-FEDERAL"
strengthens:
  - "AUTH-AR-ACT691-2025"
  - "MF-AR-SPECIALTY-COURT-*"
creates_authority:
  - "AUTH-AR-ACA-16-100-204"
  - "AUTH-AR-ACA-16-10-139"

sources:
  - url: "https://law.justia.com/codes/arkansas/2023/title-16/subtitle-2/chapter-100/"
    title: "Ark. Code § 16-100-201 to -207 (Specialty Courts)"
  - url: "https://www.arcourts.gov/courts/specialty-courts"
    title: "Arkansas Judiciary - Specialty Courts"
  - url: "https://www.samhsa.gov/grants/grant-announcements/ti-26-002"
    title: "SAMHSA 988 Administrator NOFO (FY2026)"
  - url: "https://bja.ojp.gov/funding"
    title: "BJA Current Opportunities"

created_at: "2026-02-10T20:15:00Z"
promoted_to: []
---

### The Big Idea

State supreme court administrative orders + AOC program rules don't just govern specialty courts — they unlock federal money. When you cross-reference judicial approvals with active SAMHSA/DOJ grant IDs, you expose a path where judicial authority gates federal dollars WITHOUT DHS mediation. This is a clearlane.

### Why This Is Explosive

Most people think funding flows: Federal agency → State agency (DHS) → Program. But there's a parallel path: Federal agency → Court-authorized program (via AOC) → Direct service. The court's administrative authority is the key that opens the federal lock, and DHS never touches it.

### The Authority Spine

| Layer | Authority | What It Does |
|-------|-----------|--------------|
| Statute | §16-100-201 to -207 | Creates mental health specialty courts |
| Statute | §16-100-204 | Administration — AOC runs it |
| Statute | §16-10-139 | Statewide evaluation/approval centralized |
| Administrative | Order No. 14 lineage | Court administrative plans |
| Administrative | ACT 691 (2025) | SCPAC approval + fee + distribution |
| Federal | SAMHSA NOFOs | 988 administrator, crisis linkage |
| Federal | BJA opportunities | Justice-and-mental-health programs |

### The Funding Lever Mechanism

```
Supreme Court admin order (authority)
  → AOC approval (gate)
    → Specialty court operates (program)
      → Court letter of support + AOC data/eval hooks (credibility)
        → SAMHSA/BJA NOFO application (money)
          → Federal dollars flow to court-authorized program
            → DHS never in the chain
```

### Active Opportunities NOW

| Opportunity | Deadline | Relevance |
|-------------|----------|-----------|
| SAMHSA 988 Administrator NOFO (FY2026) | **Feb 27, 2026** | Court-anchored crisis linkage scores as governance strength |
| BJA Justice-Mental Health programs | Rolling | Court approvals + MOUs + AOC eval = readiness signals |

### ⚠️ TIME SENSITIVITY

**Feb 27 is 17 days away.** If NAMI can anchor to court authority and frame as education-only inside court referrals, this is a live funding opportunity.

### The NAMI Play (education-only, clearlane-safe)

1. **Anchor to AOC specialty court authority** — cite §16-100-204 and §16-10-139 plus local admin plan
2. **Frame curriculum as education/services to justice-referred participants** — NOT treatment (Pulse 8 glossary applies here)
3. **Cross-walk to live NOFOs** with court letters of support + data-sharing language mirroring AOC reporting requirements
4. **Withstand policy swings** — court-authorized standards + AOC reporting hooks survive federal grant turbulence

### What This Means for the Handoff

This is not infrastructure. This is actionable intelligence with a deadline. If Tricia can use anything you leave her, it might be a one-page court-safe insert that:

1. Cites the statutes
2. Frames NAMI as education-only inside court referrals
3. Plugs directly into the Feb 27 SAMHSA/BJA timeline

That one-pager could be worth more than the entire graph viewer.

**Promotion Note:** Not yet promoted. Needs one-page court-safe insert drafted. SAMHSA 988 NOFO deadline Feb 27, 2026. This pulse has a clock on it.

---

## Pulse 11: Jurisdictional Language Discipline — Extended Capture Prevention

---
pulse_number: 11
temporal_hash: "#021020262030"
thread_title: "The Semantics of Capture in Policy Language"
version: 1.0
status: promoted
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - operational_guide
  - dhs_capture_prevention
  - grant_writing_tool
  - clearlane_core

priority: critical
impact: immediate

topics:
  - jurisdictional_language
  - dhs_capture
  - credentialing
  - licensure
  - audit_hooks
  - autonomy_preservation
  - court_alignment

related_pulses:
  - "#021020261945"
fills_gaps:
  - "MISSING_VALIDATION:jurisdictional_language_discipline"
strengthens:
  - "docs/medicaid_trigger_glossary_v1.yaml"

created_at: "2026-02-10T20:30:00Z"
promoted_to:
  - "docs/jurisdictional_language_playbook_v1.md"
---

### The Big Idea

Pulse 8 covered Medicaid-specific trigger terms. This pulse goes wider. ANY word that implies a regulated activity — clinical, credentialing, billing, covered services, outcomes reporting — can silently drag NAMI into a regulatory lane and hand jurisdiction to an agency you didn't invite. Language IS jurisdiction.

### What's New Beyond Pulse 8

| Pulse 8 Covered | This Pulse Adds |
|-----------------|-----------------|
| Medicaid-specific terms (CPT, MCO, NPI) | Credentialing/licensure triggers |
| Peer support substitutions | Audit hook creation through careless language |
| DHS/Medicaid capture | ANY agency capture (boards, DHS, behavioral health) |
| Term-level find/replace | Full framing discipline (mission, role, interface, data, quality) |
| Grant narrative defense | Website, slides, MOUs, court docs, ALL public artifacts |

### The Six Jurisdictional Trigger Categories

| Category | Trigger Words | What They Invoke | Safe Swaps |
|----------|---------------|------------------|------------|
| Clinical scope | clinical, therapy, treatment, provider, patient, diagnosis, plan of care | Health licensure + billing frameworks | education, skills workshops, participants, curriculum, learning objectives |
| Covered services | case management, care coordination, assessment, screening | Medicaid/DHS service definitions | navigation overview, self-navigation toolkit, orientation questionnaire (non-diagnostic) |
| Credentialing | certified, credentialed, licensed (for staff) | Boards, DHS, Medicaid credentialing authorities | qualified by training, program-approved training, competency-verified |
| Audit hooks | program evaluation, outcomes reporting (to courts/agencies) | Funding conditions, compliance obligations | attendance metrics, anonymous feedback summaries, aggregate education completions |
| Behavioral health scope | recovery services, SUD, treatment court services | DHS/behavioral health regulatory scope | justice-referred education modules, court-aligned learning support |
| Peer roles | peer support, peer specialist, certified peer | DHS/Medicaid certification and manuals | trained community mentors, lived-experience educators, community facilitators |

### Five Framing Disciplines

1. **Mission:** "Educational only. No clinical. No treatment."
2. **Role:** "Education vendor serving justice-referred participants inside existing education infrastructure."
3. **Interface:** "Court-aligned scheduling + completion attestation" — not care plans or treatment compliance
4. **Data:** "Roster + completion attestations (non-PHI)" — not clinical outcomes or treatment progress
5. **Quality:** "Curriculum standards + instructor competencies" — not licensure or scope of practice

### 10-Point Pre-Release Checklist

Before ANY document goes out — grant, MOU, website, slide, email:

1. Purpose line declares educational/non-clinical
2. Roles say instructors/facilitators, not clinicians/peers (certified)
3. Activities say classes/modules/workshops, not therapy/treatment/case management
4. Data says attendance/completion, no diagnoses or treatment notes
5. Outcomes say learning objectives met, not clinical outcomes
6. Partners say court-approved placements, avoid DHS-dependent terms
7. Funding text says education vendor, no Medicaid codes
8. Compliance cites court/administrative order, not provider manuals
9. Staff quals say program-approved training, not licensed/certified
10. Final pass: replace every risky word before release

### Micro-Templates (Copy-Paste Ready)

**Scope:** "This proposal delivers court-aligned educational modules for justice-referred participants. Services are instructional only and exclude clinical treatment, diagnosis, case management, and care coordination."

**Staffing:** "Sessions are led by trained facilitators with program-approved competencies; no licensure or clinical credential is implicated."

**Data:** "We provide rosters and completion attestations; no PHI or clinical outcomes are collected or reported."

**Interface:** "Courts select from a standardized curriculum menu; we schedule, deliver, and attest completions."

### Relationship to Pulse 8

Pulse 8 is the find-and-replace list. This pulse is the operating philosophy. Together they form a complete language defense system:

- Pulse 8 = "change this word to that word"
- Pulse 11 = "here's WHY you're changing it and here's how to think about every word you write"

**Promotion Note:** Playbook created. Candidate for: printable one-pager (checklist + templates), laminated desk reference, custom GPT system prompt layer, automated document scrubber.

---

## Pulse 12: DOJ/BJA Funding Intelligence — Query Path and Linkage Playbook

---
pulse_number: 12
temporal_hash: "#021020262045"
thread_title: "Building the Longitudinal Funding Intelligence Stack"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - money_flow_candidate
  - fis_foundation
  - data_source_candidate
  - funding_strategy
  - key_registry_candidate

priority: high
impact: foundational

topics:
  - doj
  - bja
  - usaspending
  - ein_uei_matching
  - aln
  - sam_gov
  - eo_bmf
  - county_fips
  - convergence_sprawl
  - justice_education

related_pulses:
  - "#021020261930"
  - "#021020261915"
  - "#021020262015"
  - "#021020261945"
fills_gaps:
  - "INCOMPLETE_CHAIN:federal_doj_bja_to_ar"
strengthens:
  - "MF-AR-SPECIALTY-COURT-*"
  - "AUTH-AR-ACT691-2025"

sources:
  - url: "https://www.usaspending.gov/search"
    title: "USAspending Advanced Search"
  - url: "https://sam.gov/content/assistance-listings"
    title: "SAM.gov Assistance Listings"
  - url: "https://bja.ojp.gov/funding"
    title: "BJA Funding Opportunities"

created_at: "2026-02-10T20:45:00Z"
promoted_to: []
---

### The Big Idea

A repeatable query path that traces DOJ/BJA federal dollars from USAspending down to Arkansas county-level recipients, back-resolves them to IRS filers (990 data via Moonlight), and cross-checks against state expenditure data. This is the FIS query engine for justice-aligned federal funding.

### Why This Matters Now

- Pulse 10 identified live SAMHSA/BJA opportunities with deadlines
- Pulse 7 designed the data spine but hasn't been exercised
- This pulse is the first EXECUTABLE WORKFLOW against that spine
- It proves the spine works by running real queries against real data

### The Five-Step Query Path

```
Step 1: USAspending Advanced Search
  Filter: Agency=DOJ, Sub-agency=BJA, Place=Arkansas (by county FIPS)
  Export: recipients + UEIs + award amounts + ALNs
  
Step 2: Recipient Identity Resolution
  UEI → USAspending Recipient Profiles (trend lines, related awards)
  
Step 3: Back-Resolve to IRS Filers
  Fuzzy match: recipient legal name + address → EO BMF (EIN)
  EIN → Moonlight 990 corpus (governance, programs, financials)
  
Step 4: Program Intent Layer
  Award ALN → SAM.gov Assistance Listing (program definition, eligibility)
  Watch for new cycles on same ALN
  
Step 5: State Co-Funding Cross-Check
  Arkansas Transparency Portal: match vendor/agency/county/timeframe
  Identifies dual-funded entities and state-level co-investment
```

### Data Sources and Join Keys

| Source | Join Key | What You Get |
|--------|----------|--------------|
| USAspending | UEI, FAIN, ALN | Federal awards, amounts, recipients |
| IRS EO BMF | EIN | Canonical org identity, NTEE, status |
| IRS 990 (Moonlight) | EIN | Governance, programs, financials (10 yr) |
| SAM.gov Assistance Listings | ALN | Program definitions, eligibility |
| AR Transparency Portal | Agency, vendor, amount, date | State expenditure detail |
| Census FIPS | State+County FIPS | Geographic overlay |

### The EIN↔UEI Problem

No official crosswalk exists. This is the hardest join in the entire system.

| Approach | Method | Confidence |
|----------|--------|------------|
| Name+address normalization | String matching against EO BMF | Medium — requires fuzzy scoring |
| USAspending Recipient Profiles | Manual validation per UEI | High but slow |
| Persist match scores | Store match_method + match_score | Required — never force a match |
| Unresolved bucket | Keep all failed matches | Mandatory — they're data not failures |

### Convergence vs Sprawl Signals

| Signal | Definition | What It Means |
|--------|------------|---------------|
| Convergence | Same UEI/EIN across multiple DOJ awards, same county cluster, multiple FYs | Established operator, recurring federal relationship |
| Sprawl | Many small sub-awards across many entities, weak repeat patterns | Fragmented landscape, potential instability |

### Minimal Field Map (Per Record)

```yaml
identity:    org_name, address, EIN, UEI
federal:     award_id, agency, sub_agency, ALN, action_date, amount, place_fips
geographic:  county_name, state_fips, county_fips
irs:         990_tax_year, return_type, schedules_present
state:       state_agency, contract_id, vendor_name, fy, amount
matching:    match_method, match_score, match_status (resolved/unresolved)
```

**Promotion Note:** Not yet promoted. Needs USAspending export run for AR+BJA. EIN↔UEI matching infrastructure required (Pulse 7 dependency). This is FIS operational — survives beyond Clearlane.

---

## Pulse 13: HHS/SAMHSA $2B Grant Cancellation and Reversal — Federal Volatility Event

---
pulse_number: 13
temporal_hash: "#021020262100"
thread_title: "HHS Reverses $2B Grant Cancellations"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - environmental_signal
  - risk_event
  - funding_volatility
  - clearlane_core

priority: critical
impact: strategic

topics:
  - samhsa
  - hhs
  - grant_cancellations
  - federal_volatility
  - naloxone
  - peer_recovery
  - community_mental_health
  - policy_instability

related_pulses:
  - "#021020262015"
  - "#021020262045"
  - "#021020261945"
  - "#021020261415"
fills_gaps:
  - "MISSING_VALIDATION:federal_funding_stability"
strengthens:
  - "AUTH-US-SAMHSA-*"
  - "MF-AR-SAMHSA-*"

sources:
  - url: "https://www.statnews.com/"
    title: "STAT - HHS Grant Cancellation Coverage"
  - url: "https://www.washingtonpost.com/"
    title: "Washington Post - Grant Restoration Coverage"
  - url: "https://rollcall.com/"
    title: "Roll Call - Congressional Response"

created_at: "2026-02-10T21:00:00Z"
promoted_to: []
---

### The Big Idea

On January 14, 2026, SAMHSA terminated ~2,800 grants worth ~$2B in a single day with no advance notice. Reversed within 24 hours under political pressure. Restoration still incomplete and fluid. This is not a one-time event — it's a signal about the operating environment for anyone dependent on federal behavioral health funding.

### Timeline

| Date | Event |
|------|-------|
| Jan 14, 2026 | SAMHSA sends termination letters to ~2,800 grantees |
| Jan 14, 2026 | Justification: awards "no longer align with agency priorities" |
| Jan 14-15, 2026 | Nonprofits warn of closures, layoffs, service gaps |
| Jan 15, 2026 | Bipartisan backlash from lawmakers and advocacy groups |
| ~Jan 15, 2026 | HHS reverses, announces grants restored |
| Ongoing | Many grantees still haven't received restoration notices |

### What Got Hit

- Overdose prevention programs
- Naloxone distribution
- Peer recovery support (RED term — but these are the programs that were cancelled)
- Community mental health care
- ~$1.9-2B in discretionary SAMHSA funding
- Frontline safety-net services nationwide

### Why This Matters for NAMI/Clearlane

**This is exactly why Clearlane exists.**

An organization that built its operations on SAMHSA grant funding woke up on January 14th with zero dollars and no explanation. 24 hours later the money was "back" but nobody had official confirmation. That's not a funding stream — that's a trap.

### Three Strategic Implications

**1. Federal discretionary funding is structurally unstable.**
This wasn't a budget cut through Congress. This was an administrative decision reversed by political pressure. It can happen again at any time, for any stated reason, with no advance notice.

**2. "No longer align with agency priorities" is an unkillable justification.**
It requires no evidence, no process, no appeal window. Any SAMHSA grant can be terminated with this language. Programs built entirely on SAMHSA money have no structural defense.

**3. Court-anchored authority is the hedge.**
Pulse 10 argued that court administrative orders unlock federal funding without DHS mediation. This pulse adds: court authority also SURVIVES federal volatility. A program authorized by a state supreme court order doesn't disappear when SAMHSA changes its mind.

### Clearlane Design Implications

| Principle | Application |
|-----------|-------------|
| Never build on a single federal stream | Diversify: court fees (ACT 691) + opioid settlement + state appropriation + federal |
| Authority must outlive funding | Anchor to court/statutory authority, not grant terms |
| Track restoration status | Any SAMHSA-linked money_flow artifact needs a volatility flag |
| Language matters more than ever | Pulse 8/11 — if SAMHSA is reviewing grant "alignment with priorities," every word in every narrative is a potential kill switch |

### New Artifact Implications

- All SAMHSA-linked money_flow artifacts should carry: `federal_volatility_risk: HIGH`
- All SAMHSA-linked authority_reference artifacts should note: administrative termination possible without notice
- field_validation for any SAMHSA-dependent program should test: "What survives if this grant disappears tomorrow?"

### The Convergence/Sprawl Read

Organizations that CONVERGE on multiple funding streams (federal + state + court fees + settlement) survive this event. Organizations in SPRAWL on a single SAMHSA grant do not. This is the first real-world stress test of the Convergence vs Sprawl signal from Pulse 12.

### What This Means for the Handoff

This is context Tricia needs to understand even without the graph viewer. The world NAMI is operating in changed on January 14th. Any funding strategy that depends on a single federal agency is now visibly fragile. The clearlane isn't just about avoiding DHS capture — it's about building on authority that can't be cancelled by email.

**Promotion Note:** Not yet promoted. Needs volatility flags added to existing SAMHSA money_flow artifacts. Candidate for standalone briefing document for Tricia. This is environmental intelligence — changes the operating assumptions for everything.
