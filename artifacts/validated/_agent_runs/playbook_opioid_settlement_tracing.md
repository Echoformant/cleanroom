---
title: Opioid Settlement Tracing Playbook
version: "1.0"
created: 2025-02-10
category: audit_methodology
applies_to:
  - money_flow
  - authority_reference
  - evidence_item
  - field_validation
priority: high
tags:
  - opioid_settlement
  - arorp
  - exhibit_e
  - deterministic_linkage
  - treasury_reconciliation
dependencies:
  - entity_registry
  - AUTH-AR-ARORP
  - AUTH-AR-ACT691-2025
---

# Opioid Settlement Tracing Playbook

A field-ready methodology for tracing opioid-settlement dollars from source to service with deterministic links.

## Three High-Yield Audit Hooks

### 1. Distribution Agreements (Exhibit E)

**What:** The master allocation schedule that maps defendants → state share → in-state subdivisions.

**Why:** It's the canonical "origin → allocation" key. Every later payment schedule and subaward should reconcile back to an Exhibit E line item (defendant, tranche, % share, year).

**Artifact Pattern:**
```json
{
  "authority_id": "AUTH-US-OPIOID-EXHIBIT-E-<DEFENDANT>",
  "authority_type": "settlement_agreement",
  "allocation_schedule": {
    "defendant_group": "Distributors|Janssen|Purdue|...",
    "state_code": "AR",
    "state_share_pct": 0.333,
    "subdivision_shares": [
      {"entity": "ARORP-Counties", "pct": 0.333},
      {"entity": "ARORP-Municipalities", "pct": 0.333}
    ]
  }
}
```

### 2. Recurring Payment Schedules

**What:** Year-by-year payment timetables (often by defendant group) with due dates, paid-to-date, and shortfalls/interest.

**Why:** Gives you time-bounded cash-in events. These let you validate state treasury deposits and catch "missing" receipts in a given fiscal year.

**Artifact Pattern:**
```json
{
  "evidence_id": "EVID-AR-OPIOID-PAYMENT-SCHEDULE-<DEFENDANT>-<FY>",
  "payment_schedule": {
    "defendant_group": "Distributors",
    "fiscal_year": "FY2025",
    "due_date": "2025-07-15",
    "amount_due": 12500000,
    "amount_paid": 12500000,
    "shortfall": 0,
    "interest_accrued": 0
  }
}
```

### 3. Third-Party Subgrantee MOUs

**What:** Agreements from the state program (e.g., ARORP/AG/AOC/DHS) to downstream implementers (counties, NGOs, courts, universities).

**Why:** They encode the authority chain (who can obligate/approve), scope restrictions, CFDA/authority tags, and reporting obligations—your deterministic bridge from the settlement pool to services.

**Artifact Pattern:**
```json
{
  "authority_id": "AUTH-AR-MOU-<GRANTOR>-TO-<SUBGRANTEE>-<FY>",
  "authority_type": "mou",
  "parties": {
    "grantor": "AR Attorney General - Opioid Fund",
    "grantor_program_code": "OPIOID-STATE-SHARE",
    "subgrantee": "Administrative Office of the Courts",
    "subgrantee_ein": "71-6000000"
  },
  "terms": {
    "start_date": "2024-11-01",
    "end_date": "2025-06-30",
    "obligation_amount": 1000000,
    "allowable_uses": [
      "transitional housing",
      "mental health treatment",
      "peer recovery supports",
      "transportation"
    ]
  }
}
```

---

## Minimal Capture Spec (Four Artifact Types)

### authority_reference

| Field | Pattern | Notes |
|-------|---------|-------|
| `authority_id` | `AUTH-US-OPIOID-<AGREEMENT>` or `AUTH-AR-<STATE-ACT>` | |
| `authority_type` | `settlement_agreement`, `statute`, `regulation`, `administrative`, `mou` | |
| `citation` | Settlement title/section; state act/section | |
| `administering_body` | AG / ARORP / AOC / DHS (desk-level when known) | |
| `effects.access_limiting` | Allowable uses, carve-outs, match, timelines | |
| `editor_status` | `pending` | |

### money_flow

| Field | Pattern | Notes |
|-------|---------|-------|
| `flow_id` | `MF-AR-OPIOID-<DEFENDANT>-<FY>-<TRANCHE>` (receipts) | |
| `flow_id` | `MF-AR-OPIOID-<PROGRAM>-TO-<SUBGRANTEE>-<FY>` (outflows) | |
| `source` | Treasury fund / program account | |
| `destination` | Implementer (county, court program, NGO) | |
| `linkage_keys` | `exhibit_e_id`, `payment_schedule_id`, `mou_id` | **Critical for tracing** |
| `constraints` | Allowables from authority_reference | |
| `editor_status` | `pending` | |

### evidence_item

| Field | Pattern | Notes |
|-------|---------|-------|
| `evidence_id` | `EVID-AR-OPIOID-EXE-<DEF>-<YEAR>` (Exhibit E row) | |
| `proves` | List of authority_reference and money_flow IDs | |
| `location` | URL/file path; page/section | |
| `editor_status` | `pending` | |

### field_validation

| Field | Pattern | Notes |
|-------|---------|-------|
| `target_id` | The money_flow or authority_reference being validated | |
| `checks` | Array of check types (see below) | |
| `result` | `pass`, `fail`, `partial` + notes | |
| `editor_status` | `pending` | |

**Check Types:**
- `reconciles_to_exhibit_e`
- `matches_payment_schedule`
- `mou_scope_ok`
- `treasury_deposit_hit`
- `subaward_register_hit`

---

## Deterministic Linkage Keys (MANDATORY)

These keys enable traceable reconciliation across artifacts:

| Key | Composite Structure | Use |
|-----|---------------------|-----|
| `exhibit_e_id` | `(defendant_group, state_code, subdivision_id, allocation_pct)` | Tie to master allocation |
| `payment_schedule_id` | `(defendant_group, year, due_date, amount_due)` | Tie to payment timeline |
| `treasury_receipt_id` | `(fund_code, journal_id, post_date, amount)` | Validate actual deposits |
| `mou_id` | `(grantor_prog_code, subgrantee_ein, start_end, oblig_amt)` | Tie to subaward |
| `program_object_code` | State object/fund code | Ledger validation |

---

## Fast Operational Workflow (Repeatable Desk-Touch)

### Step 1: Anchor
Create `authority_reference` for the settlement agreement; attach Exhibit E as `evidence_item`.

```
AUTH-US-OPIOID-<SETTLEMENT>
  ├── EVID-AR-OPIOID-EXE-<DEFENDANT>-EXHIBIT-E
  └── links to downstream flows
```

### Step 2: Inbounds
For each due year/defendant, instantiate `money_flow` (receipt) using `payment_schedule_id`; validate with treasury receipts (`field_validation`).

```
MF-AR-OPIOID-<DEFENDANT>-FY2025-RECEIPT
  ├── linkage_keys.payment_schedule_id = "DISTRIBUTORS-2025-0715-12500000"
  └── FV-AR-OPIOID-<DEFENDANT>-FY2025-TREASURY-RECONCILE
```

### Step 3: Outbounds
For each subaward/MOU, instantiate `money_flow` (obligation → disbursement) and bind to the same `exhibit_e_id` lineage; validate scope & allowables.

```
MF-AR-OPIOID-AG-TO-AOC-SPECIALTY-COURTS-FY2025
  ├── linkage_keys.exhibit_e_id = parent allocation
  ├── linkage_keys.mou_id = "AG-OPIOID-AOC-2024NOV-1000000"
  └── FV-AR-OPIOID-AG-AOC-SCOPE-VALIDATION
```

### Step 4: Reconcile
Yearly balance check:

```
Σ receipts (by defendant) ≟ Σ obligations + expenditures + ending balance
```

---

## QA Flags for Dashboards

| Flag | Condition | Severity |
|------|-----------|----------|
| **Missing lineage** | Any `money_flow` without `exhibit_e_id` or `payment_schedule_id` | HIGH |
| **Timing mismatch** | Deposit posted >30 days after scheduled due date | MEDIUM |
| **Scope drift** | MOU purpose not in `effects.access_limiting` | HIGH |
| **Orphan MOUs** | Subgrantee agreements with no matching treasury disbursement | HIGH |
| **Residuals** | Large year-end fund balance without encumbrance notes | MEDIUM |

---

## Starter Stubs

### Receipt Flow Stub

```json
{
  "flow_id": "MF-AR-OPIOID-DISTRIBUTORS-FY2025-Q2",
  "source": "Opioid Distributor Settlement Payments",
  "intermediary": "Arkansas State Treasury",
  "destination": "Arkansas Opioid Qualified Settlement Fund",
  "amount": 0,
  "fund_type": "state",
  "fiscal_year": "FY2025",
  "linkage_keys": {
    "exhibit_e_id": "",
    "payment_schedule_id": "",
    "treasury_receipt_id": ""
  },
  "statutory_basis": "National Opioid Settlement Agreement",
  "statutory_basis_refs": ["AUTH-US-OPIOID-DISTRIBUTOR-SETTLEMENT"],
  "editor_status": "pending"
}
```

### Subaward Flow Stub

```json
{
  "flow_id": "MF-AR-OPIOID-<PROGRAM>-TO-<SUBGRANTEE>-FY2025",
  "source": "Arkansas Opioid Qualified Settlement Fund",
  "intermediary": "<AG|ARORP|AOC>",
  "destination": "<Subgrantee Name>",
  "amount": 0,
  "fund_type": "state",
  "fiscal_year": "FY2025",
  "linkage_keys": {
    "exhibit_e_id": "",
    "mou_id": "",
    "program_object_code": ""
  },
  "constraints": {
    "allowable_uses": [],
    "source_authority": "AUTH-AR-MOU-..."
  },
  "statutory_basis_refs": [],
  "editor_status": "pending"
}
```

### Validation Stub

```json
{
  "fv_id": "FV-AR-OPIOID-<FLOW_ID>-RECONCILE",
  "target_id": "MF-AR-OPIOID-...",
  "jurisdiction": "Arkansas",
  "validating_entity": "Cleanroom Audit",
  "checks": [
    {"type": "reconciles_to_exhibit_e", "result": "pending"},
    {"type": "matches_payment_schedule", "result": "pending"},
    {"type": "treasury_deposit_hit", "result": "pending"}
  ],
  "alignment_status": "open",
  "evidence_basis": [],
  "disclosure_level": "internal",
  "editor_status": "pending"
}
```

---

## Linkage Key CSV Template

Save to `_data/opioid_linkage_keys.csv`:

```csv
key_type,defendant_group,state_code,subdivision,year,due_date,amount,fund_code,journal_id,subgrantee_ein,notes
exhibit_e,Distributors,AR,State,,,0.333,,,,"State share"
exhibit_e,Distributors,AR,ARORP-Counties,,,0.333,,,,"County share via ARORP"
exhibit_e,Distributors,AR,ARORP-Municipalities,,,0.333,,,,"Municipal share via ARORP"
payment_schedule,Distributors,AR,,2025,2025-07-15,12500000,,,,"FY2025 Q2 payment"
treasury_receipt,,AR,,,2025-07-18,12500000,OPIOID-QSF,J2025-0718-001,,"Deposit confirmed"
mou,AG-OPIOID,AR,,2024,,1000000,,,71-6000000,"AOC specialty courts grant"
```

---

## Implementation Priority

1. **Create AUTH-US-OPIOID-DISTRIBUTOR-SETTLEMENT** (master settlement authority)
2. **Attach Exhibit E evidence** for Arkansas allocation
3. **Map existing MF-AR-OPIOID-* flows** to linkage keys
4. **Create field_validations** for each flow
5. **Build dashboard flag queries** for missing lineage

---

## Related Artifacts

- [AUTH-AR-ARORP](../authority_reference/AUTH-AR-ARORP.json)
- [AUTH-AR-ACT691-2025](../authority_reference/AUTH-AR-ACT691-2025.json)
- [ENTITY-AR-ARORP](../entity_registry/ENTITY-AR-ARORP.json)
- [ENTITY-AR-AG-OPIOID-FUND](../entity_registry/ENTITY-AR-AG-OPIOID-FUND.json)
- [MF-AR-OPIOID-SETTLEMENT-AG-SPECIALTY-COURTS](../money_flow/MF-AR-OPIOID-SETTLEMENT-AG-SPECIALTY-COURTS.json)
