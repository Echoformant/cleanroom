# Agent Run: Field Validation Batch — Money Flows (Part 1 of 3)

**Priority:** HIGH  
**Est. Time:** 60-90 minutes  
**Goal:** Create field_validation artifacts for 50 money_flow artifacts

---

## Context

243 money_flow artifacts need field_validation coverage. This batch focuses on the first 50. Money flow validations verify:
- Is the appropriation documented in legislation?
- Are there audit findings about this fund?
- Is spending aligned with statutory restrictions?

---

## Target Money Flows (Batch 1: 50)

1. MF-ACCOUNTABILITY-COURT-FUND-2025-2026
2. MF-Accountability-Court-Fund-to-Administrative-Office
3. MF-Adult-Drug-Court-Cash-Fund-to-Administrative-Office
4. MF-AR-ACF-DEPOSIT-2025
5. MF-AR-ADC-EDUCATIONAL-WORK-PROGRAMS-FY2026
6. MF-AR-ADC-OPERATIONS-FY2026
7. MF-AR-ADC-PRISON-FARM-FY2026
8. MF-AR-ADE-PUBLIC-SCHOOL-FUND-FY2026
9. MF-AR-ADE-TEACHER-SALARY-SUPPORT-FY2026
10. MF-AR-ADE-TEXTBOOK-PURCHASE-FY2026
11. MF-AR-ADH-BREAST-CARE-FY2026
12. MF-AR-ADH-EMS-FY2026
13. MF-AR-ADH-GRANTS-AID-FY2026
14. MF-AR-ADH-HEALTH-BUILDING-GRANTS-FY2026
15. MF-AR-ADH-INFECTIOUS-DISEASE-CONTROL-FY2026
16. MF-AR-ADH-INFECTIOUS-DISEASES-TESTING-FY2026
17. MF-AR-ADH-INTERPRETERS-DEAF-FY2026
18. MF-AR-ADH-KIDNEY-DISEASE-FY2026
19. MF-AR-ADH-NUCLEAR-PLANNING-FY2026
20. MF-AR-ADH-OPERATIONS-FY2026
21. MF-AR-ADH-SHARED-SERVICES-PAYING-FY2026
22. MF-AR-ADH-TOBACCO-PREVENTION-FY2026
23. MF-AR-ADH-TRAUMA-SYSTEM-FY2026
24. MF-AR-ADH-WIC-FY2026
25. MF-AR-ADLL-APPRENTICESHIP-PROGRAM-FY2026
26. MF-AR-ADLL-LABOR-STANDARDS-ENFORCEMENT-FY2026
27. MF-AR-ADLL-LICENSING-BOARD-OPERATIONS-FY2026
28. MF-AR-ADPHT-HERITAGE-GRANTS-FY2026
29. MF-AR-ADPHT-STATE-PARKS-OPERATIONS-FY2026
30. MF-AR-ADPHT-TOURISM-MARKETING-FY2026
31. MF-AR-AEDC-BUSINESS-INNOVATION-PROGRAM-FY2026
32. MF-AR-AEDC-ECONOMIC-DEVELOPMENT-GRANTS-FY2026
33. MF-AR-AEDC-MINORITY-AND-WOMEN-BUSINESS-SUPPORT-FY2026
34. MF-AR-AG-TO-CHILDRENS-HOSPITAL-OPIOID-RESEARCH-2024
35. MF-AR-AID-CONSUMER-EDUCATION-PROGRAM-FY2026
36. MF-AR-AID-INSURANCE-FRAUD-INVESTIGATION-FY2026
37. MF-AR-AID-INSURANCE-REGULATION-OPERATIONS-FY2026
38. MF-AR-AOC-ACCOUNTABILITY-COURT-FUND-FY2026
39. MF-AR-AOC-ACF-FY2026
40. MF-AR-AOC-ADULT-DRUG-COURT-PROGRAM-FY2026
41. MF-AR-ARORP-142-PROJECTS-26M-2024H1
42. MF-AR-ARORP-APPROVED-28M-THROUGH-2024Q4
43. MF-AR-ARORP-DENIED-293M-THROUGH-2024Q4
44. MF-AR-ARORP-NALOXONE-TOTAL-2M-2022-2026
45. MF-AR-ARORP-TO-AR-PHARMACISTS-UNDER100-FY2024
46. MF-AR-ARORP-TO-BRIDGING-GAPS-COPE-FY2024
47. MF-AR-ARORP-TO-CADCA-CAN-FY2025
48. MF-AR-ARORP-TO-CADCA-TRAINING-FY2023
49. MF-AR-ARORP-TO-CHANGE-COPE-FY2025
50. MF-AR-ARORP-TO-CHANGES-BEHAVIORAL-HEALTH-FY2024

---

## Schema Reference

### field_validation for money_flow
```json
{
  "fv_id": "FV-AR-MF-ADH-OPERATIONS-FY2026-APPROPRIATION",
  "jurisdiction": "Arkansas",
  "validating_entity": "Arkansas Legislative Audit",
  "alignment_status": "captured",
  "evidence_basis": ["MF-AR-ADH-OPERATIONS-FY2026", "AUTH-AR-ACT776-2025-ADH"],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

### Alignment Status Guide

| Status | When to Use |
|--------|-------------|
| `captured` | Appropriation is in Act 776/appropriation bill, spending documented |
| `open` | Appropriation exists but no audit coverage yet |
| `mixed` | Partial documentation, some gaps in trail |

### Validating Entity by Agency

| Money Flow Source | Validating Entity |
|-------------------|-------------------|
| ADH (Health Dept) | Arkansas Department of Health / Legislative Audit |
| ADC (Corrections) | Arkansas Department of Correction / Legislative Audit |
| ADE (Education) | Arkansas Department of Education / Legislative Audit |
| AOC (Courts) | Administrative Office of the Courts / Supreme Court |
| ARORP (Opioid) | ARORP Transparency / Attorney General / Legislative Audit |
| DHS | Department of Human Services / CMS (if Medicaid) |

---

## Instructions

1. For each money_flow, create a field_validation that:
   - References the money_flow in `evidence_basis`
   - Adds any related authority in `evidence_basis` if known
   - Uses appropriate validating_entity based on agency
   - Sets `alignment_status` based on documentation level

2. Use this naming pattern:
   - `FV-AR-MF-{short-id}-APPROPRIATION` for state appropriations
   - `FV-AR-MF-{short-id}-AUDIT-{YEAR}` if audit exists
   - `FV-AR-MF-{short-id}-GRANT-TRACKING` for grant flows

## Output Format

```json
{
  "field_validation": [...]
}
```

---

## Success Criteria

- 50 field_validation artifacts created
- Each references correct money_flow in evidence_basis
- Appropriate validating entities assigned
- ARORP flows reference ARORP transparency documentation
