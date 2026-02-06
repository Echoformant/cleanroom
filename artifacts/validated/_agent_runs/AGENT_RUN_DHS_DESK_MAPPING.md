# Agent Run: DHS Desk-Level Authority Mapping

**Operation:** NAMI Clearlane / VECTOR 1  
**Mode:** Structural Gap Filling  
**Target:** Map desk-level authority chains within Arkansas DHS

## Mission

Arkansas Department of Human Services (DHS) controls most Medicaid and behavioral health funding. We have statutes but lack the internal authority chain mapping:

**Statute** → **Agency** → **Division** → **Office** → **Committee** → **Desk Position**

Create `authority_type: "administrative"` artifacts for internal DHS positions, committees, and delegation chains.

## Why This Matters

Authority is "triggered" at different levels:
- Medicaid enrollment triggers Division of Medical Services authority
- Peer certification triggers OSAMH authority
- Billing code submission triggers DUR Board authority
- Grant application triggers program-level authority

Without mapping these triggers, we can't trace who actually controls funding decisions.

## DHS Organizational Structure to Map

### Top Level
- **DHS Secretary** — Ultimate authority over all divisions
- **DHS Chief of Staff** — Operational control

### Division of Medical Services (Medicaid)
- **Director of Medicaid** — Controls Medicaid policy
- **Deputy Director for Programs** — Oversees waiver programs
- **PASSE Program Director** — Managed care authority
- **ARHome Program Director** — 1115 waiver authority
- **ARChoices Program Manager** — 1915(c) HCBS waiver

### Office of Alcohol and Drug Abuse Prevention (OSAMH)
- **OSAMH Director** — Behavioral health policy authority
- **Peer Support Program Coordinator** — Peer certification authority
- **SUD Treatment Authority** — Substance use program authority
- **Prevention Services Manager** — Prevention grant authority

### Oversight Committees
- **Drug Utilization Review (DUR) Board** — Prescription drug policy
- **Peer Support Advisory Committee** — If exists, peer program recommendations
- **Medicaid Provider Rate Committee** — Reimbursement rates

## Artifacts to Create

### Authority References (administrative type)

For each desk position and committee, create:

```json
{
  "authority_id": "AUTH-AR-DHS-{DIVISION}-{POSITION}",
  "authority_type": "administrative",
  "citation": "DHS Policy Manual Section X.X; DHS Org Chart",
  "administering_body": "Arkansas Department of Human Services",
  "governs": ["MF-AR-...", "AUTH-AR-..."],
  "effects": "Controls [what this position/committee decides]",
  "delegation_source": "AUTH-AR-DHS-SECRETARY or parent position",
  "editor_status": "pending"
}
```

**Special fields for administrative authorities:**
- `delegation_source`: The authority this position's power comes from
- `appointment_authority`: Who appoints this position/committee
- `decision_scope`: What types of decisions this position can make

### Specific Artifacts Needed

| Artifact ID | Position/Committee | Delegation From |
|-------------|-------------------|-----------------|
| AUTH-AR-DHS-SECRETARY | DHS Secretary | Governor appointment |
| AUTH-AR-DHS-DMS-DIRECTOR | Director of Medicaid | DHS Secretary |
| AUTH-AR-DHS-OSAMH-DIRECTOR | OSAMH Director | DHS Secretary |
| AUTH-AR-DHS-OSAMH-PEER-COORDINATOR | Peer Support Coordinator | OSAMH Director |
| AUTH-AR-DHS-DUR-BOARD-CHAIR | DUR Board Chair | DMS Director |
| AUTH-AR-DHS-PASSE-DIRECTOR | PASSE Program Director | DMS Director |
| AUTH-AR-DHS-ARHOME-DIRECTOR | ARHome Program Director | DMS Director |
| AUTH-AR-DHS-ARCHOICES-MANAGER | ARChoices Program Manager | DMS Director |

### Money Flows (if discoverable)

For each administrative authority, identify money flows it controls:

```json
{
  "flow_id": "MF-AR-DHS-{PROGRAM}-{TYPE}-FY2026",
  "source": "DHS Division of Medical Services",
  "intermediary": "OSAMH",
  "destination": "Peer Support Program",
  "amount": 0,
  "fund_type": "state",
  "fiscal_year": "FY2026",
  "restrictions": {
    "medicaid": true,
    "dhs_controlled": true
  },
  "statutory_basis": "Ark. Code § 20-77-107; DHS OSAMH authority",
  "statutory_basis_refs": ["AUTH-AR-ACA-20-77-107", "AUTH-AR-DHS-OSAMH-DIRECTOR"],
  "editor_status": "pending"
}
```

## Research Sources

1. **DHS Organizational Chart** — ark.org/dhs/about/organization
2. **DHS Policy Manuals** — OBHS Provider Manual, Medicaid Provider Manuals
3. **Administrative Rules** — ARHSC, DMS Rules in Arkansas Register
4. **CMS State Plan** — Arkansas Medicaid State Plan documents
5. **Job Postings** — DHS job descriptions describe supervisory authority
6. **Board Meeting Minutes** — DUR Board, PASSE committee meetings

## Output Format

Return a JSON array of authority_reference and money_flow artifacts:

```json
[
  {
    "authority_id": "AUTH-AR-DHS-SECRETARY",
    "authority_type": "administrative",
    "citation": "Ark. Code § 25-10-101; Governor Appointment",
    "administering_body": "Arkansas Department of Human Services",
    "governs": ["AUTH-AR-DHS-DMS-DIRECTOR", "AUTH-AR-DHS-OSAMH-DIRECTOR"],
    "effects": "Ultimate authority over all DHS divisions and programs",
    "delegation_source": "Governor of Arkansas",
    "editor_status": "pending"
  },
  ...
]
```

## After Completion

Save output to: `_agent_runs/batch_dhs_desk_mapping.json`

Then run:
```powershell
python scripts/batch_ingest.py _agent_runs/batch_dhs_desk_mapping.json
python scripts/linkage_analyzer.py --summary
```

## Authority Chain Visualization Goal

After ingestion, we should be able to trace:
```
Governor
  ↓ appoints
DHS Secretary (AUTH-AR-DHS-SECRETARY)
  ↓ delegates to
Director of Medicaid (AUTH-AR-DHS-DMS-DIRECTOR)
  ↓ delegates to
OSAMH Director (AUTH-AR-DHS-OSAMH-DIRECTOR)
  ↓ delegates to
Peer Support Coordinator (AUTH-AR-DHS-OSAMH-PEER-COORDINATOR)
  ↓ controls
MF-AR-MEDICAID-PEER-ROUTING-2026
```
