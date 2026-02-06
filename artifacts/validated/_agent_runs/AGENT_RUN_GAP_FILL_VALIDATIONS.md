# Agent Run: Gap Fill — Missing Field Validations

**Operation:** NAMI Clearlane / VECTOR 1  
**Mode:** Gap Filling  
**Target:** Money flows and authorities lacking field_validation coverage

## Mission

Create field_validation artifacts for money flows and authorities that currently have no audit/compliance linkage. This is NOT exhaustive cycling — just create the missing validations.

## What is a Field Validation?

A field_validation artifact documents that an external entity (auditor, federal agency, legislative body) has reviewed and assessed a money flow or authority for compliance. It links evidence items to the artifact being validated.

## Gap List to Fill

Create ONE field_validation for each of these artifacts. Research what audit or compliance check would apply, then create the artifact.

### High Priority (DHS/Medicaid related)

| Artifact | Suggested Validator |
|----------|---------------------|
| MF-AR-MEDICAID-PEER-ROUTING-2026 | CMS or DHS Inspector General |
| MF-AR-ARHOME-PREMIUM-ASSISTANCE-FY2026 | CMS 1115 Waiver Review |
| MF-AR-ARCHOICES-PERSONAL-CARE-FY2026 | CMS 1915(c) Waiver Compliance |
| AUTH-AR-1115-WAIVER-ARHOME | CMS Waiver Approval |
| AUTH-AR-ARCHOICES-WAIVER | CMS Waiver Renewal |

### Medium Priority (State Funds)

| Artifact | Suggested Validator |
|----------|---------------------|
| MF-AR-COUNTY-AID-FUND-DISTRIBUTION-FY2026 | AR Legislative Audit |
| MF-AR-HIGHWAY-FUND-ARDOT-FY2026 | AR Legislative Audit |
| MF-AR-COURT-FINES-TO-JUSTICE-FUND-FY2026 | AR Admin Office of Courts Audit |
| AUTH-AR-ACA-19-5-602-COUNTY-AID | Legislative Review |

### Lower Priority (Constitutional/Structural)

| Artifact | Suggested Validator |
|----------|---------------------|
| AUTH-AR-CONSTITUTION-ART16-SEC11 | Historical constitutional compliance |
| AUTH-AR-CONSTITUTION-ART16-SEC12 | DFA Budget Compliance |
| AUTH-AR-CONSTITUTION-ART16-SEC13 | State debt limit compliance |

## Canonical Schema for Field Validation

```json
{
  "fv_id": "FV-AR-{VALIDATOR}-{SUBJECT}-{YEAR}",
  "jurisdiction": "Arkansas",
  "validating_entity": "CMS | Legislative Audit | DFA | DHS OMIG | AOC",
  "alignment_status": "captured|open|mixed",
  "evidence_basis": ["EVID-AR-...", "AUTH-AR-..."],
  "disclosure_level": "public|limited|confidential",
  "editor_status": "pending"
}
```

### Field Definitions

- **fv_id**: Unique identifier following pattern `FV-AR-{Validator}-{Subject}-{Year}`
- **validating_entity**: The organization that performed the validation/audit
- **alignment_status**: 
  - `captured` = Artifact is fully compliant with validation requirements
  - `open` = Issues identified, remediation pending
  - `mixed` = Partially compliant, some issues
- **evidence_basis**: Array of artifact IDs that support this validation
- **disclosure_level**: `public` for published audits, `limited` for internal reviews

## Research Approach

For each artifact:
1. Identify what oversight body would review it
2. Search for actual audit reports or compliance documentation
3. If found, cite it in evidence_basis
4. If not found but expected, note "pending" status

## Output Format

Return a single JSON array of field_validation artifacts:
```json
[
  {
    "fv_id": "FV-AR-CMS-ARHOME-WAIVER-2024",
    "jurisdiction": "Arkansas",
    "validating_entity": "Centers for Medicare & Medicaid Services",
    "alignment_status": "captured",
    "evidence_basis": ["AUTH-AR-1115-WAIVER-ARHOME", "EVID-AR-CMS-WAIVER-LETTER-..."],
    "disclosure_level": "public",
    "editor_status": "pending"
  },
  ...
]
```

## After Completion

Save output to: `_agent_runs/batch_gap_validations.json`

Then run:
```powershell
python scripts/batch_ingest.py _agent_runs/batch_gap_validations.json
python scripts/gap_analyzer.py --type MISSING_VALIDATION
```
