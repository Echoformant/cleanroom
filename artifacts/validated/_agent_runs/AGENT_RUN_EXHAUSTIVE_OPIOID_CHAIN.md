# Agent Run: Exhaustive Opioid Settlement Chain Completion

**Priority:** HIGH  
**Est. Time:** 45-60 minutes  
**Goal:** Complete opioid settlement artifact chain with field validations and missing links

---

## Context

Arkansas receives opioid settlement funds from multiple defendants. The current dossier has money_flows and some authorities but gaps exist in:
1. Field validations for all opioid-related artifacts
2. Complete defendant settlement authority references
3. ARORP transparency evidence linkages

---

## Current Opioid Artifacts Needing Work

### Money Flows (need FVs)
- MF-AR-OPIOID-ALLERGAN-SETTLEMENT-2024-2030
- MF-AR-OPIOID-CVS-SETTLEMENT-2024-2032
- MF-AR-OPIOID-DISTRIBUTOR-SETTLEMENT-2022-2038
- MF-AR-OPIOID-JANSSEN-SETTLEMENT-2022-2031
- MF-AR-OPIOID-KROGER-SETTLEMENT-2025-2034
- MF-AR-OPIOID-TEVA-SETTLEMENT-2024-2035
- MF-AR-OPIOID-WALGREENS-SETTLEMENT-2024-2037
- MF-AR-OPIOID-WALMART-SETTLEMENT-2024
- MF-AR-OPIOIDSETTLEMENT-QSF-SETTLEMENTPAYMENTS-FY2022
- MF-AR-QSF-ATTORNEYFEES-EXPENSES-FY2022
- MF-AR-QSF-DISTRIBUTION-CITIES-FY2022
- MF-AR-QSF-DISTRIBUTION-COUNTIES-FY2022
- MF-AR-QSF-DISTRIBUTION-STATE-FY2022
- MF-AR-QSF-TO-CITIES-SETTLEMENT-DISTRIBUTION
- MF-AR-QSF-TO-COUNTIES-SETTLEMENT-DISTRIBUTION

### Authorities (need FVs)
- AUTH-US-26CFR-1-468B-1-TREASREG
- AUTH-US-IRC-468B-QSF
- AUTH-AR-OPIOIDS-MOU-2021-07
- AUTH-AR-CITIES-DISTRIBUTION-AGREEMENT-2022
- AUTH-AR-COUNTIES-DISTRIBUTION-AGREEMENT-2022
- AUTH-AR-QSF-ORDER-18CV-22-355

---

## Schema Reference

### Settlement FV Pattern
```json
{
  "fv_id": "FV-AR-OPIOID-SETTLEMENT-JANSSEN-TRACKING-2026",
  "jurisdiction": "Arkansas",
  "validating_entity": "Attorney General / ARORP Committee",
  "alignment_status": "captured",
  "evidence_basis": [
    "MF-AR-OPIOID-JANSSEN-SETTLEMENT-2022-2031",
    "AUTH-AR-OPIOIDS-MOU-2021-07",
    "EVID-AR-ARORP-QUARTERLY-2024Q4"
  ],
  "disclosure_level": "public",
  "editor_status": "pending"
}
```

---

## Instructions

1. Create field_validations for ALL opioid settlement money_flows
2. Create field_validations for ALL opioid-related authorities
3. Link FVs to ARORP transparency evidence where available
4. Use "Attorney General / ARORP Committee" as validating_entity
5. Set alignment_status to "captured" (settlements are well-documented)

## Evidence Sources

- ARORP Transparency Portal: https://arorp.arkansasag.gov/
- ARORP Quarterly Reports
- Crittenden County Court Order 18CV-22-355
- Settlement Agreements on ARORP site

## Output Format

```json
{
  "field_validation": [
    {
      "fv_id": "FV-AR-OPIOID-SETTLEMENT-{defendant}-TRACKING-2026",
      ...
    }
  ]
}
```

---

## Success Criteria

- All 15+ opioid money_flows have FVs
- All opioid authorities have FVs
- FVs properly link to ARORP evidence
- Complete chain: Settlement → QSF → Distribution → Projects → Outcomes
