# Agent Run: DHS DAABHS Authority Chain Completion

**Priority:** HIGH  
**Est. Time:** 45-60 minutes  
**Goal:** Complete DHS/DAABHS/OSAMH authority chain with desk-level positions

---

## Context

DHS Division of Aging, Adult and Behavioral Health Services (DAABHS) contains the Office of State Alcohol and Substance Abuse Services (OSAMH). The desk-level authority chain is partially mapped but needs completion.

---

## Current Structure (Already Mapped)

```
AUTH-AR-DHS-SECRETARY (Janet Mann)
  └── AUTH-AR-DMS-DIRECTOR (Elizabeth Pitman, Medicaid side)
  └── AUTH-AR-DAABHS-DIRECTOR (?)
      └── AUTH-AR-OSAMH-DIRECTOR (Paula Stone)
          └── AUTH-AR-OSAMH-DRUG-DIRECTOR-LANE (Kirk Lane)
          └── AUTH-AR-OSAMH-DRUG-DIRECTOR-FISHER (Thomas Fisher)
```

---

## Gaps to Fill

### Missing Desk-Level Authorities (need research)
1. DAABHS Director position authority
2. OSAMH Deputy Director if exists
3. APAC (Adult Psychiatric Advisory Committee) membership
4. Peer Advisory Committee membership
5. DHS Deputy for Operations position

### Missing Field Validations
All desk-level authorities need FVs:
- AUTH-AR-DHS-SECRETARY
- AUTH-AR-DMS-DIRECTOR
- AUTH-AR-OSAMH-DIRECTOR
- AUTH-AR-OSAMH-DRUG-DIRECTOR-LANE
- AUTH-AR-OSAMH-DRUG-DIRECTOR-FISHER
- AUTH-AR-DHS-DEPUTY-OPS
- AUTH-AR-DAABHS-DIRECTOR
- AUTH-AR-APAC-CHAIR
- AUTH-AR-OSAMH-APAC

### Supporting Evidence Needed
- DHS org charts
- OSAMH staff directory
- APAC meeting minutes or bylaws
- Medicaid Provider Manual peer section

---

## Schema Reference

### Desk-Level Authority
```json
{
  "authority_id": "AUTH-AR-DAABHS-DIRECTOR",
  "authority_type": "administrative",
  "citation": "DHS DAABHS Division Director Position",
  "administering_body": "Department of Human Services",
  "governs": ["AUTH-AR-OSAMH-DIRECTOR", "MF-AR-DAABHS-OPERATIONS"],
  "effects": "Oversees DAABHS including OSAMH, aging services, and community mental health",
  "editor_status": "pending"
}
```

### FV for Desk-Level
```json
{
  "fv_id": "FV-AR-DHS-SECRETARY-APPOINTMENT-2024",
  "jurisdiction": "Arkansas",
  "validating_entity": "Governor's Office",
  "alignment_status": "captured",
  "evidence_basis": ["AUTH-AR-DHS-SECRETARY", "EVID-AR-DHS-ORG-CHART-2024"],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

---

## Research Sources

- DHS website: https://humanservices.arkansas.gov/
- OSAMH page: divisions/aging-services/osamh/
- DHS leadership page
- Arkansas Governor announcements for appointments
- LinkedIn for position verification

---

## Output Format

```json
{
  "authority_reference": [
    {"authority_id": "AUTH-AR-DAABHS-DIRECTOR", ...}
  ],
  "field_validation": [
    {"fv_id": "FV-AR-DHS-SECRETARY-APPOINTMENT-2024", ...}
  ],
  "evidence_item": [
    {"evidence_id": "EVID-AR-DHS-ORG-CHART-2024", ...}
  ]
}
```

---

## Success Criteria

- Complete DAABHS org chart in authorities
- All DHS desk-level positions have FVs
- Linkages between positions are correct (governs field)
- APAC/Advisory committees mapped
