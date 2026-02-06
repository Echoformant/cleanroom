# Agent Run: ARORP Dossier Completion

**Operation:** NAMI Clearlane / VECTOR 1  
**Mode:** Domain-Focused Deep Dive  
**Target:** Complete Arkansas Opioid Recovery Partnership (ARORP) cluster

## Mission

ARORP controls ~$270 million in opioid settlement funds (2/3 of $406M total to Arkansas). We have foundational artifacts but need to complete the dossier with:

1. **Grant recipient flows** — Where has money actually gone?
2. **Board/governance artifacts** — Who makes decisions?
3. **Denial analysis artifacts** — What got rejected and why?
4. **Impact evidence** — What outcomes are documented?
5. **Transparency gaps** — What's missing?

## Existing ARORP Artifacts (Already Ingested)

### Authorities
- AUTH-AR-OPIOIDS-MOU-EXECUTED-JUL-2021
- AUTH-AR-QSF-ORDER-CRITTENDEN-18CV-22-355-2022-06-13
- AUTH-AR-COUNTIES-DISTRIBUTION-AGREEMENT
- AUTH-AR-CITIES-DISTRIBUTION-AGREEMENT
- AUTH-AR-ARORP-FUNDING-GUIDELINES
- AUTH-US-OPIOID-SETTLEMENT-* (8 settlement agreements)

### Money Flows
- MF-AR-OPIOID-*-SETTLEMENT-* (8 settlement inflows)
- MF-AR-QSF-TO-COUNTIES-SETTLEMENT-DISTRIBUTION-2022-2040
- MF-AR-QSF-TO-CITIES-SETTLEMENT-DISTRIBUTION-2022-2040
- MF-AR-AG-TO-CHILDRENS-HOSPITAL-OPIOID-RESEARCH-2023
- MF-AR-ARORP-TO-HOPE-MOVEMENT-2023-2024

### Evidence
- EVID-AR-ARORP-DENIAL-LOG-336M-2025
- EVID-AR-ARORP-TOTAL-AWARDED-26M-2025
- EVID-AR-WYSAC-TRANSPARENCY-SCORE-12-16-2024
- EVID-AR-AAC-AUDIT-ARORP-ADMIN-2024

## Artifacts Needed to Complete Dossier

### A. Grant Recipient Flows

ARORP has awarded $26.3M to 142 projects. We need money_flow artifacts for major recipients:

| Recipient Category | Example Flow ID |
|-------------------|-----------------|
| Recovery Beds (384 beds) | MF-AR-ARORP-TO-{PROVIDER}-RECOVERY-BEDS-{YEAR} |
| Overdose Response Teams (11) | MF-AR-ARORP-TO-JD{N}-ORT-{YEAR} |
| Peer Recovery Specialists (35) | MF-AR-ARORP-TO-{PROVIDER}-PEER-SPECIALISTS-{YEAR} |
| Naloxone Bank | MF-AR-ARORP-NALOXONE-BANK-DISTRIBUTION-{YEAR} |
| Prevention Programs (26) | MF-AR-ARORP-TO-{PROVIDER}-PREVENTION-{YEAR} |

**Research source:** ARORP Progress page, annual reports, AAC articles

### B. Governance Artifacts

Administrative authorities for ARORP decision-makers:

| Position | Artifact ID |
|----------|-------------|
| ARORP Director (Kirk Lane) | AUTH-AR-ARORP-DIRECTOR-KIRK-LANE |
| ARORP Deputy Director (Tenesha Barnes) | AUTH-AR-ARORP-DEPUTY-DIRECTOR |
| ARORP Advisory Board | AUTH-AR-ARORP-ADVISORY-BOARD |
| AAC Director (Chris Villines) | AUTH-AR-AAC-DIRECTOR |
| AML Director (Mark Hayes) | AUTH-AR-AML-DIRECTOR |
| QSF Administrator (Edgar Gentle) | AUTH-AR-QSF-ADMINISTRATOR-EDGAR-GENTLE |

**Key fields:**
```json
{
  "authority_id": "AUTH-AR-ARORP-DIRECTOR-KIRK-LANE",
  "authority_type": "administrative",
  "citation": "Counties Distribution Agreement; AAC/AML appointment",
  "administering_body": "ARORP",
  "governs": ["MF-AR-ARORP-*"],
  "effects": "Operational control of all ARORP funding decisions",
  "appointment_authority": "AAC Director + AML Director jointly",
  "editor_status": "pending"
}
```

### C. Denial Analysis Artifacts

We have aggregate denial evidence (EVID-AR-ARORP-DENIAL-LOG-336M-2025). Need breakdown:

| Denial Category | Count | Amount | Artifact ID |
|-----------------|-------|--------|-------------|
| Missing signatures | ~100 | $150M+ | EVID-AR-ARORP-DENIALS-MISSING-SIGNATURES |
| Budget issues | ~80 | $100M+ | EVID-AR-ARORP-DENIALS-BUDGET-NONCOMPLIANT |
| Supplanting | ~30 | $50M+ | EVID-AR-ARORP-DENIALS-SUPPLANTING |
| Insufficient evidence | ~37 | $36M+ | EVID-AR-ARORP-DENIALS-INSUFFICIENT-DATA |

### D. Impact Evidence

Document outcomes from ARORP annual reports:

| Metric | Value | Artifact ID |
|--------|-------|-------------|
| People obtaining employment | 873 | EVID-AR-ARORP-IMPACT-EMPLOYMENT-2024 |
| People obtaining insurance | 1,041 | EVID-AR-ARORP-IMPACT-INSURANCE-2024 |
| Naloxone kits to community | 11,049 | EVID-AR-ARORP-IMPACT-NALOXONE-COMMUNITY-2024 |
| Naloxone kits to responders | 6,181 | EVID-AR-ARORP-IMPACT-NALOXONE-RESPONDERS-2024 |
| People trained on naloxone | 10,298 | EVID-AR-ARORP-IMPACT-NALOXONE-TRAINING-2024 |

### E. Transparency Gap Evidence

Document what's missing per WYSAC evaluation:

| Missing Item | Artifact ID |
|--------------|-------------|
| No board meeting agendas | EVID-AR-ARORP-TRANSPARENCY-GAP-AGENDAS |
| No voting records | EVID-AR-ARORP-TRANSPARENCY-GAP-VOTES |
| No scoring sheets | EVID-AR-ARORP-TRANSPARENCY-GAP-SCORING |
| No conflict-of-interest disclosures | EVID-AR-ARORP-TRANSPARENCY-GAP-COI |

### F. Field Validations

| Subject | Validator | Artifact ID |
|---------|-----------|-------------|
| ARORP Overall | WYSAC Evaluation | FV-AR-WYSAC-ARORP-TRANSPARENCY-2024 |
| AAC Administration | Legislative Audit | FV-AR-LEGAUDIT-AAC-ARORP-ADMIN-2024 |
| Settlement Fund Compliance | QSF Court Order | FV-AR-CRITTENDEN-QSF-COMPLIANCE-2024 |

## Canonical Schemas

### Money Flow
```json
{
  "flow_id": "MF-AR-ARORP-TO-{RECIPIENT}-{TYPE}-{YEAR}",
  "source": "Arkansas Opioid Recovery Partnership",
  "intermediary": "None",
  "destination": "{Recipient organization}",
  "amount": 0,
  "fund_type": "state",
  "fiscal_year": "FY{YEAR}",
  "restrictions": {
    "medicaid": false,
    "dhs_controlled": false,
    "opioid_abatement": true
  },
  "statutory_basis": "Arkansas Opioids MOU; Counties/Cities Distribution Agreements",
  "statutory_basis_refs": ["AUTH-AR-OPIOIDS-MOU-EXECUTED-JUL-2021", "AUTH-AR-COUNTIES-DISTRIBUTION-AGREEMENT"],
  "editor_status": "pending"
}
```

### Authority (Administrative)
```json
{
  "authority_id": "AUTH-AR-ARORP-{POSITION}",
  "authority_type": "administrative",
  "citation": "{Appointment document}",
  "administering_body": "ARORP / AAC / AML",
  "governs": ["MF-AR-ARORP-*"],
  "effects": "{What this position controls}",
  "appointment_authority": "{Who appoints}",
  "editor_status": "pending"
}
```

### Evidence (Impact)
```json
{
  "evidence_id": "EVID-AR-ARORP-IMPACT-{METRIC}-{YEAR}",
  "section": "MF-AR-ARORP-{RELATED-FLOW}",
  "claim_summary": "{Metric value and context}",
  "evidence_type": "audit",
  "source": {
    "document": "ARORP Annual Evaluation Report {YEAR}",
    "url": "https://arorp.gov/reports/",
    "retrieved": "2026-02-06"
  },
  "confidence_level": "high",
  "editor_status": "pending"
}
```

## Output Format

Return a single JSON array with all new artifacts:

```json
[
  { "authority_id": "AUTH-AR-ARORP-DIRECTOR-KIRK-LANE", ... },
  { "flow_id": "MF-AR-ARORP-TO-JD5-ORT-2024", ... },
  { "evidence_id": "EVID-AR-ARORP-IMPACT-EMPLOYMENT-2024", ... },
  { "fv_id": "FV-AR-WYSAC-ARORP-TRANSPARENCY-2024", ... },
  ...
]
```

## After Completion

Save output to: `_agent_runs/batch_arorp_dossier.json`

Then run:
```powershell
python scripts/batch_ingest.py _agent_runs/batch_arorp_dossier.json
python scripts/linkage_analyzer.py --artifact MF-AR-ARORP
```

## Dossier Visualization Goal

After completion, we produce:
1. **Timeline** — MOU → QSF → Director → Funding Rounds → Present
2. **Governance Map** — AAC/AML → Director → Board → Decisions
3. **Sankey** — Settlements → QSF → ARORP → Recipients
4. **Denial Analysis** — Pie/bar chart of rejection reasons
5. **Impact Dashboard** — Key metrics from outcome evidence
