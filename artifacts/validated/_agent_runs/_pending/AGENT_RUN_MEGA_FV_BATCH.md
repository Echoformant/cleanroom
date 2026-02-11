# Agent Run: Mega Field Validation Batch — All Categories

**Priority:** MEDIUM-HIGH  
**Est. Time:** 90-120 minutes  
**Goal:** Create 100+ field_validation artifacts in one exhaustive batch

---

## Context

This is a mega batch designed for running across multiple agent sessions. 373 artifacts need field validations. This batch provides the full context for bulk generation.

---

## The Task

Create field_validation artifacts for as many of these as possible:

### By Category

**Authority References Needing FVs (145 total)**

Key statute families:
- Ark. Code Ann. Title 19 (Appropriations/Fiscal) — ~30 artifacts
- Ark. Code Ann. Title 20 (Public Health/Welfare) — ~25 artifacts
- Ark. Code Ann. Title 25 (State Government) — ~10 artifacts
- Ark. Code Ann. Title 16 (Courts/Criminal) — ~15 artifacts
- Federal authorities (42 CFR, IRC 468B, SAMHSA) — ~15 artifacts
- Administrative/Desk-level — ~20 artifacts
- MOUs and Agreements — ~10 artifacts
- Acts of Arkansas Legislature — ~20 artifacts

**Money Flows Needing FVs (243 total)**

By agency:
- ADH (Department of Health) — ~20 artifacts
- ADC (Corrections) — ~10 artifacts
- ADE (Education) — ~15 artifacts
- DHS (Human Services) — ~40 artifacts
- AOC (Courts) — ~25 artifacts
- ARORP (Opioid) — ~30 artifacts
- QSF (Settlement Funds) — ~15 artifacts
- DAABHS/OSAMH — ~20 artifacts
- Other state agencies — ~68 artifacts

---

## Schema Reference

### Standard FV Template
```json
{
  "fv_id": "FV-AR-{artifact-short-id}-{type}-{year}",
  "jurisdiction": "Arkansas",
  "validating_entity": "{appropriate entity}",
  "alignment_status": "captured|open|mixed",
  "evidence_basis": ["{referenced artifact ID}", "{related evidence}"],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

### FV ID Patterns
| Pattern | Use Case |
|---------|----------|
| `FV-AR-ACA-{section}-STATUTORY` | Statute existence/text validation |
| `FV-AR-MF-{flow}-APPROPRIATION` | Appropriation in Act 776 |
| `FV-AR-{agency}-AUDIT-{year}` | Legislative audit finding |
| `FV-AR-{topic}-COMPLIANCE-{year}` | Program compliance check |
| `FV-AR-{position}-APPOINTMENT` | Desk-level appointment verification |

### Validating Entity Reference
| Entity | Use For |
|--------|---------|
| Arkansas Legislative Audit | State fund audits, appropriations |
| Department of Human Services | DHS programs, Medicaid |
| CMS (Centers for Medicare & Medicaid) | Federal Medicaid compliance |
| Administrative Office of the Courts | Specialty court programs |
| Attorney General / ARORP Committee | Opioid settlements |
| Governor's Office | Executive appointments |
| Arkansas Legislature | Statutory authorization |
| Department of Finance and Administration | State budget/fiscal |

---

## Batch Strategy

1. **Start with easy wins**: Appropriation FVs for money_flows (just verify Act 776 section)
2. **Then authorities**: Statutory verification FVs (statute exists and is current)
3. **Then complex**: Audit-based FVs (require actual audit research)

---

## Output Format

Return all field_validations in a single JSON batch:

```json
{
  "field_validation": [
    {...},
    {...},
    // as many as possible
  ]
}
```

---

## Full Gap List Reference

See `_agent_runs/_pending/FV_GAPS_LIST.txt` for complete list of 360 artifact IDs needing field validations.

---

## Success Criteria

- 100+ field_validation artifacts created
- No duplicate fv_ids
- Proper validating_entity per agency
- All FVs reference correct source artifact in evidence_basis
