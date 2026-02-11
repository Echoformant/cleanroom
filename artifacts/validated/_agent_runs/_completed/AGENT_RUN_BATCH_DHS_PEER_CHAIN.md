# AGENT RUN: DHS-Medicaid-Peer Authority Chain (Focused Batch)

**Priority:** HIGHEST - Critical for NAMI capture avoidance
**Estimated time:** 45-60 min
**Output:** Batch JSON with ~20-30 artifacts

## Objective

Map the complete authority chain from Arkansas statutes through DHS organizational hierarchy to the desk level for Medicaid-funded Peer Support Services. This is the critical path for understanding how DHS controls peer workforce certification, reimbursement, and service delivery.

## Required Schema Fields

### Money Flow
```json
{
  "flow_id": "MF-AR-...",
  "source": "...",
  "intermediary": "None" or "...",
  "destination": "...",
  "amount": 0,
  "fund_type": "state",
  "fiscal_year": "FY2026",
  "restrictions": {"medicaid": true, "dhs_controlled": true},
  "statutory_basis": "Ark. Code § ...",
  "statutory_basis_refs": ["AUTH-...", "EVID-..."],
  "editor_status": "pending"
}
```

### Authority Reference
```json
{
  "authority_id": "AUTH-AR-...",
  "authority_type": "statute|regulation|administrative|mou",
  "citation": "...",
  "administering_body": "...",
  "governs": ["MF-...", "AUTH-..."],
  "effects": "...",
  "editor_status": "pending"
}
```

Use `authority_type: "administrative"` for desk-level authorities (director positions, committees, delegation chains).

## Seeds to Expand

Start with these existing artifacts and expand their authority chains:

1. **AUTH-AR-ACA-20-77-107** - DHS authority over Medicaid
2. **AUTH-AR-ACA-19-5-1144** - Accountability Court Fund
3. **MF-AR-MEDICAID-PEER-ROUTING-2026** - Peer Medicaid routing

## Research Targets

### Tier 1: Statutory Foundation
- Ark. Code § 20-77-107 (DHS Medicaid authority)
- Ark. Code § 20-46 (Mental Health Services)
- Ark. Code § 20-64 (Substance Abuse)
- DHS enabling statute

### Tier 2: Regulatory Layer
- DHS Provider Manual (Peer Support Services chapter)
- OBHS (Office of Behavioral Health Services) rules
- Peer certification requirements
- Medicaid reimbursement codes for peer services

### Tier 3: Administrative/Desk Level
Map these positions and their authorities:
- DHS Secretary (top)
- DHS Deputy Director
- Division of Medical Services Director
- OBHS Director
- OSAMH Director (Kirk Lane)
- Peer Certification Board/Committee
- Provider Enrollment Unit

For each desk-level position, create:
```json
{
  "authority_id": "AUTH-AR-DHS-[OFFICE]-[POSITION]",
  "authority_type": "administrative",
  "citation": "DHS Organizational Chart; [statute delegating authority]",
  "administering_body": "[Name of office]",
  "governs": ["MF-...", "AUTH-subordinate-..."],
  "effects": "[What decisions this position controls]",
  "editor_status": "pending"
}
```

### Tier 4: Certification/Credentialing
- Who certifies Peer Recovery Specialists in Arkansas?
- What body controls Peer training curriculum?
- What Medicaid codes apply to Peer services?
- What supervision requirements exist?

## Output Format

Return a complete batch JSON:

```json
{
  "batch_id": "dhs_medicaid_peer_chain_YYYYMMDD",
  "generated_at": "ISO timestamp",
  "mode": "focused_authority_chain",
  "total_turns": 1,
  "artifacts": {
    "money_flow": [...],
    "authority_reference": [...],
    "evidence_item": [...],
    "field_validation": [...]
  }
}
```

## Success Criteria

- [ ] Complete chain from Ark. Code → DHS Secretary → desk level
- [ ] All Peer certification authorities identified
- [ ] Medicaid billing codes for peer services documented
- [ ] Kirk Lane's position in chain clearly mapped
- [ ] All artifacts have `statutory_basis_refs` populated
- [ ] Source URLs for DHS manuals/org charts included

## Key Question to Answer

**"If NAMI wants to provide Medicaid-reimbursable Peer Support Services without going through DHS-controlled channels, what authorities must be navigated?"**
