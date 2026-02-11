# AGENT RUN: Kirk Lane Complete Profile (Focused Batch)

**Priority:** HIGH - Key control figure
**Estimated time:** 45-60 min
**Output:** Batch JSON with ~15-25 artifacts

## Objective

Build complete profile of Kirk Lane's positions, authorities, and control points across multiple Arkansas behavioral health structures. He sits at the intersection of:
- DHS OSAMH (state bureaucracy)
- ARORP (opioid settlement)
- Potentially other boards/commissions

## Known Positions

### 1. DHS OSAMH Director
- Office of Substance Abuse and Mental Health
- Within Division of Behavioral Health Services
- Medicaid policy influence

### 2. ARORP Leadership
- Role in settlement fund distribution
- Project approval authority
- Policy direction

## Research Targets

### Position Documentation
For each position, create:
```json
{
  "authority_id": "AUTH-AR-DHS-OSAMH-DIRECTOR",
  "authority_type": "administrative",
  "citation": "DHS Organizational Structure; [appointment source]",
  "administering_body": "Arkansas Department of Human Services",
  "governs": [...],
  "effects": "Controls OSAMH policy, staffing, and budget allocation",
  "editor_status": "pending"
}
```

### Authority Chain Questions
1. Who does Kirk Lane report to?
2. What budget does he control?
3. What programs does OSAMH administer?
4. What approval authority does he have over:
   - Peer certification?
   - Provider enrollment?
   - Grant distribution?
   - ARORP projects?

### Network Mapping
- What committees/boards is he on?
- What organizations receive OSAMH funding?
- What organizations receive ARORP funding he controls?
- Any nonprofit board positions?

### Document Sources
- DHS org charts
- ARORP governance documents
- Board meeting minutes
- Arkansas government appointment records
- LinkedIn/professional profiles
- News articles about OSAMH initiatives

## Evidence Items Needed

For each position/authority:
```json
{
  "evidence_id": "EVID-AR-DHS-LANE-OSAMH-APPOINTMENT",
  "section": "AUTH-AR-DHS-OSAMH-DIRECTOR",
  "claim_summary": "Kirk Lane appointment as OSAMH Director",
  "evidence_type": "policy",
  "source": {...},
  "confidence_level": "high",
  "editor_status": "pending"
}
```

## Output Format

```json
{
  "batch_id": "kirk_lane_profile_YYYYMMDD",
  "generated_at": "ISO timestamp",
  "mode": "individual_profile",
  "total_turns": 1,
  "artifacts": {
    "authority_reference": [...],
    "evidence_item": [...],
    "field_validation": [...]
  }
}
```

## Success Criteria

- [ ] All known positions documented
- [ ] Reporting chain mapped (who he reports to)
- [ ] Control points identified (what he controls)
- [ ] Budget authority quantified where possible
- [ ] ARORP role clearly documented
- [ ] Linked to existing MF/AUTH artifacts

## Key Question

**"What funding decisions require Kirk Lane's approval, and what alternative pathways exist?"**
