# Cleanroom: NAMI Clearlane / VECTOR 1 Dossier System

## Overview

This is a **schema-bound artifact repository** for Operation NAMI Clearlane, a law-anchored operating framework for NAMI Arkansas. It catalogs legal authorities, funding flows, evidence, and field validations related to Arkansas public finance—especially behavioral health, DHS, Medicaid, and court systems.

## Architecture

### Four Artifact Schemas (Strictly Enforced)
All artifacts must conform to one of four JSON schemas in [schemas/](schemas/):

| Schema | ID Field | Purpose |
|--------|----------|---------|
| `authority_reference` | `authority_id` | Statutes, regulations, policies, administering bodies |
| `money_flow` | `flow_id` | Funding sources, intermediaries, destinations, amounts |
| `evidence_item` | `evidence_id` | Budgets, grants, audit reports, official documents |
| `field_validation` | `fv_id` | Real-world alignment status (open/mixed/captured) |

### Directory Structure
- **`artifacts/validated/`** — Schema-validated, accepted artifacts (the canonical Dossier)
- **`artifacts/invalidated/`** — Files failing validation, awaiting fixes
- **`proposals/{schema_type}/`** — Staged artifacts pending pipeline validation
- **`schemas/`** — JSON Schema definitions (source of truth)
- **`docs/llm_op_instructions/`** — LLM behavioral contracts and briefings

### Artifact Lifecycle
```
raw/ → proposals/{type}/ → [pipeline validates] → artifacts/validated/ or artifacts/invalidated/
```

## Critical Conventions

### Artifact Creation Rules
1. **Output YAML by default**, JSON only when explicitly requested
2. **Set `editor_status: "pending"`** for new artifacts
3. **Never add fields not in schema** — `additionalProperties: false` is enforced
4. **Use exact enum values** from schemas (e.g., `fund_type`: `state`|`federal`|`settlement`)
5. **Include all required fields** — see schema definitions

### File Naming Patterns
- Validated artifacts have dual representation:
  - Pretty file at root: `MF-AR-MEDICAID-PEER-ROUTING-2026.json`
  - Minified in folder: `MF-AR-MEDICAID-PEER-ROUTING-2026.yaml/0.json`
- Suffixes like `--002` indicate derivative variants — never renumber
- Act-focused IDs: `AR_FY2026_...` trace Arkansas appropriation acts

### money_flow Specifics
- `amount`: Integer USD (no commas, decimals, or strings)
- `fiscal_year`: String pattern `YYYY` or `YYYY-YYYY`
- `intermediary`: Use `"None"` rather than omitting
- `statutory_basis`: Ends with citation using `【docId†Lstart-Lend】` format
- `fund_type`: `state` when appropriated by Arkansas (even with federal reimbursement)

### authority_reference Specifics
- `administering_body`: Single string (not array)
- `governs`: Array of strings describing what the authority governs
- `effects`: Object with `access_limiting` and `appeal_mechanism` booleans

## Behavioral Contract for AI Agents

From [vector1_clearlane_instruction.yaml](vector1_clearlane_instruction.yaml):

**DO:**
- Produce only schema-valid artifacts
- Capture all discrete claims from source material as separate artifacts
- Use exact entity names as statutes describe them

**DON'T:**
- Infer governance meaning, intent, or bias
- Speculate about DHS, Medicaid, or any agency
- Add commentary, explanation, or prose around artifacts
- Wrap JSON/YAML in Markdown fences (unless explicitly asked)

## Validation

No build system. Validate artifacts using:
- VS Code JSON diagnostics
- PowerShell: `Get-Content path | jq . > $null` (if jq installed)
- Pipeline validation occurs on commit to `proposals/`

## Key Files

- [vector1_clearlane_instruction.yaml](vector1_clearlane_instruction.yaml) — Full operating instructions and schemas
- [docs/llm_op_instructions/LLM_BRIEFING_OPERATION_NAMI_CLEARLANE_VECTOR1.md](docs/llm_op_instructions/LLM_BRIEFING_OPERATION_NAMI_CLEARLANE_VECTOR1.md) — Briefing for model context
- [docs/workflow-upgrade-plan.md](docs/workflow-upgrade-plan.md) — Pipeline fix documentation
