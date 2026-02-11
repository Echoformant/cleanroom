# AGENT RUN: Specialty Courts Authority Chain (Focused Batch)

**Priority:** MEDIUM-HIGH - Alternative to DHS control path
**Estimated time:** 30-45 min
**Output:** Batch JSON with ~15-20 artifacts

## Objective

Map the complete authority chain for Arkansas specialty/accountability courts (Drug Courts, Mental Health Courts, Veterans Courts, DWI Courts). These represent a **non-DHS pathway** for behavioral health services and funding - critical for NAMI navigation.

## Why This Matters

Specialty courts operate under AOC (Administrative Office of the Courts), not DHS. They:
- Receive direct appropriations (Act 776-2025 Section 25: $300,000)
- Have their own certification/standards
- Can fund peer support outside Medicaid channels
- Represent alternative service delivery model

## Seeds to Expand

Existing artifacts:
- `AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND`
- `EVID-AR-ACT776-2025-S25-SpecialtyCourtProgram-300000-FY2026`
- `MF-AR-AOC-SPECIALTYCOURT-FY2026`

## Research Targets

### Tier 1: Statutory Foundation
- Ark. Code § 16-98 (Drug Court programs)
- Ark. Code § 16-99 (Veterans Treatment Court)
- Ark. Code § 19-5-1144 (Accountability Court Fund)
- Administrative Order 21 (Supreme Court)

### Tier 2: Administrative Structure
Map these entities:
- Arkansas Supreme Court (oversight)
- Administrative Office of the Courts (implementation)
- Drug Court Coordinator position
- Individual court judges with specialty dockets

### Tier 3: Funding Flows
- State appropriation → AOC → Individual courts
- SAMHSA Drug Court grants (federal)
- BJA (Bureau of Justice Assistance) grants
- Participant fees (if any)

### Tier 4: Service Delivery
- What treatment providers can specialty courts use?
- Are peer support services allowable?
- What certification is required?
- How does this differ from DHS pathway?

## Output Format

```json
{
  "batch_id": "specialty_courts_chain_YYYYMMDD",
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

## Key Questions to Answer

1. **Can specialty courts fund peer support services directly?**
2. **What certification is required for peer workers in court settings?**
3. **Does this bypass DHS Medicaid requirements?**
4. **What is the funding capacity ($300K appropriation + grants)?**

## Success Criteria

- [ ] Complete AOC organizational chain mapped
- [ ] All specialty court types documented
- [ ] Federal grant authorities included
- [ ] Service delivery pathways identified
- [ ] Comparison point to DHS pathway created
