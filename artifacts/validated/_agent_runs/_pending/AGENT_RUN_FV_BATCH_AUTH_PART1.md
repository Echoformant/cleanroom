# Agent Run: Field Validation Batch — Authority References (Part 1 of 4)

**Priority:** HIGH  
**Est. Time:** 60-90 minutes  
**Goal:** Create field_validation artifacts for 40 authority_reference artifacts

---

## Context

373 artifacts are missing field_validation coverage. This batch focuses on the first 40 authority_reference artifacts. Field validations confirm audit alignment, compliance status, and disclosure level.

## What is a Field Validation?

A field_validation artifact connects an authority or money_flow to real-world verification:
- Was this statute actually consulted/applied?
- Is there an audit finding related to this?
- What's the current compliance status?

---

## Target Artifacts (Batch 1: 40 Authority References)

Create field_validations for these:

1. AUTH-AR-1115-WAIVER-ARHOME
2. AUTH-AR-1915C-ARCHOICES-0195R06
3. AUTH-AR-20-46-301
4. AUTH-AR-20-64-1001
5. AUTH-AR-20-64-602-19
6. AUTH-AR-20-76-201-EXHIBIT-H
7. AUTH-AR-20-76-201
8. AUTH-AR-20-77-107
9. AUTH-AR-20-77-135
10. AUTH-AR-25-10-129
11. AUTH-AR-ACA-10-3-2901-SPECIALTY-COURT-ADVISORY-COM
12. AUTH-AR-ACA-10-3-2901
13. AUTH-AR-ACA-12-1-101
14. AUTH-AR-ACA-12-27-103
15. AUTH-AR-ACA-12-8-101
16. AUTH-AR-ACA-15-4-209
17. AUTH-AR-ACA-16-10-139-SPECIALTY-COURT-PROGRAM
18. AUTH-AR-ACA-16-10-139
19. AUTH-AR-ACA-16-98-304-COST-AND-FEES
20. AUTH-AR-ACA-16-98-304
21. AUTH-AR-ACA-16-98-305-REQUIRED-RESOURCES
22. AUTH-AR-ACA-19-1-101-CONTRACTS
23. AUTH-AR-ACA-19-4-101
24. AUTH-AR-ACA-19-5-1011-DRUG-COURT-ENHANCEMENT-SPECI
25. AUTH-AR-ACA-19-5-1033-CRIME-VICTIMS-REPARATIONS-RE
26. AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND
27. AUTH-AR-ACA-19-5-1146-ADULT-DRUG-COURT-EXPENSE-CAS
28. AUTH-AR-ACA-19-5-1147-SPECIALTY-COURT-STATE-CENTRA
29. AUTH-AR-ACA-19-5-1148-COURT-TECHNOLOGY-IMPROVEMENT
30. AUTH-AR-ACA-19-5-304-COMMUNITY-CORRECTION-REVOLVIN
31. AUTH-AR-ACA-19-5-501
32. AUTH-AR-ACA-19-5-940
33. AUTH-AR-ACA-19-5-941
34. AUTH-AR-ACA-19-8-303
35. AUTH-AR-ACA-20-46-101
36. AUTH-AR-ACA-20-47-101
37. AUTH-AR-ACA-20-76-101
38. AUTH-AR-ACA-25-1-101
39. AUTH-AR-ACA-6-1-101
40. AUTH-AR-APAC-CHAIR

---

## Schema Reference

### field_validation
```json
{
  "fv_id": "FV-AR-AUTH-20-77-107-COMPLIANCE-2026",
  "jurisdiction": "Arkansas",
  "validating_entity": "Arkansas Legislative Audit",
  "alignment_status": "captured",
  "evidence_basis": ["AUTH-AR-20-77-107", "EVID-AR-DHS-MEDICAID-AUDIT-2024"],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

### Field Definitions

| Field | Values | Description |
|-------|--------|-------------|
| `fv_id` | `FV-AR-{type}-{ref}-{year}` | Unique validation ID |
| `jurisdiction` | `Arkansas` | Always Arkansas for AR- artifacts |
| `validating_entity` | Legislature, DFA, DHS, etc. | Who validates compliance |
| `alignment_status` | `captured` / `open` / `mixed` | Current compliance state |
| `evidence_basis` | Array of artifact IDs | What this FV references |
| `disclosure_level` | `public` / `restricted` / `internal` | Availability |
| `editor_status` | `pending` / `accepted` | Review status |

---

## Instructions

1. For each authority_reference, determine:
   - What entity would validate compliance? (Legislative Audit, DFA, DHS, CMS, etc.)
   - Is compliance captured (clearly documented), open (pending/unknown), or mixed?
   - What evidence supports this? (link to audits, reports, or the authority itself)

2. Use this naming pattern:
   - `FV-AR-{short-id}-COMPLIANCE-{YEAR}` for compliance validations
   - `FV-AR-{short-id}-AUDIT-{YEAR}` for audit-based validations
   - `FV-AR-{short-id}-STATUTORY-VERIFICATION` for statute existence checks

3. For authorities with no known audit, create basic statutory verification FVs

## Output Format

```json
{
  "field_validation": [
    {
      "fv_id": "FV-AR-20-77-107-COMPLIANCE-2026",
      "jurisdiction": "Arkansas",
      "validating_entity": "Department of Human Services",
      "alignment_status": "captured",
      "evidence_basis": ["AUTH-AR-20-77-107"],
      "disclosure_level": "public",
      "editor_status": "pending"
    }
  ]
}
```

---

## Success Criteria

- 40 field_validation artifacts created
- Each references the correct authority in evidence_basis
- Appropriate validating_entity assigned
- No duplicate fv_ids
