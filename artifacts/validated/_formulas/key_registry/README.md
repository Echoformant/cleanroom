# Key Registry (Composite Join Surface)

**Purpose:** One authoritative table that maps every funding/program record to canonical keys so SAM.gov, USAspending, and Arkansas DFA/agency exports join cleanly without hand-fixes.

## Why This Matters

- Different sources name the same thing differently
- A composite key prevents drift and duplicate entities
- Once in place, every new dataset "plugs in" with zero manual reconciliation
- Becomes your universal `JOIN ... USING (...)` surface across money flows, authority refs, and field validations

## Schema (v1)

| Column | Type | Description |
|--------|------|-------------|
| `entity_name` | string | Normalized legal name |
| `uei` | string | Unique Entity Identifier (SAM.gov) |
| `ein` | string | Employer Identification Number |
| `assistance_listing` | array | CFDA/AL numbers (e.g., 93.958) |
| `state_fund_code` | array | Arkansas internal codes from DFA/agency ledgers |
| `duns_legacy` | string | Legacy DUNS (nullable, for older files) |
| `aka_names` | array | Common name variants |
| `status` | enum | `active` \| `retired` |
| `source_of_truth` | string | Who last validated (editor + evidence) |
| `valid_from` | date | Temporal bound start |
| `valid_to` | date | Temporal bound end (null = current) |

## Join Logic

| Source | Join Key |
|--------|----------|
| SAM.gov | `uei` |
| USAspending | `uei` or `assistance_listing` (+ year) |
| Arkansas DFA/agency | `state_fund_code` (+ fiscal year) |
| Legacy files | `duns_legacy` or `ein` (fallback) |

## Normalization Rules

1. **UPPERCASE** for codes (UEI, AL/CFDA, fund codes)
2. **Title Case** for entity names
3. Strip punctuation/Inc./LLC from `entity_name`
4. AL/CFDA must be `NN.NNN` string form
5. `state_fund_code` must be exact code from Arkansas ledgers (no friendly labels)

## Files

- `key_registry.yaml` — Authoritative records with lineage
- `key_registry.csv` — Flat export for quick joins
- `key_registry.sql` — SQLite/Postgres table definition

## Usage

```sql
-- Join USAspending to state fund codes
SELECT u.*, k.state_fund_code
FROM usaspending u
JOIN key_registry k ON u.uei = k.uei
WHERE k.status = 'active';

-- Find all programs under a specific assistance listing
SELECT * FROM key_registry
WHERE '93.958' = ANY(assistance_listing);
```

## VECTOR 1 Clearlane Integration

The Key Registry enables deterministic Snapshot generation:

1. **Resolve identity once** against registry
2. **Normalize all feeds** through the same resolver
3. **Generate Snapshot Matrix** with confidence signals
4. **Flag gaps explicitly** when joins fail

Unresolved ≠ error. Unresolved = explicit GAP artifact.

## Snapshot Matrix Columns

| Column | Meaning |
|--------|---------|
| `SURFACE_ID` | Canonical ID from registry |
| `SURFACE_NAME` | Entity name |
| `AUTHORITY_SIGNAL` | Statute/admin order tied to fund/desk |
| `MONEY_SIGNAL` | Resolved fund code or obligation exists |
| `IMPLEMENTATION_SIGNAL` | Agency program execution evidence |
| `OVERSIGHT_SIGNAL` | Reporting, audit, or committee touch |
| `EVIDENCE_FOUND` | yes/partial/no |
| `GAP_FLAG` | Any join failed or evidence missing |
| `NOTES` | Context for gaps |

No synthesis. No interpretation. Facts only.
