# AGENT RUN: RHTP Four Proposals Completion (Focused Batch)

**Priority:** MEDIUM - Legislative proposals for FY2026
**Estimated time:** 30-45 min
**Output:** Batch JSON with ~20-30 artifacts

## Objective

Complete documentation for the four RHTP (Regional Hub Treatment Program) proposals being considered by Arkansas Senate. These represent potential new funding pathways.

## The Four Proposals

### 1. HEART (Arkansas HEART Program)
- Hub-based treatment expansion
- Regional distribution model

### 2. PACT (Program for Addiction Care and Treatment)
- Peer-led recovery support
- Community-based model

### 3. RISE AR
- Recovery integration services
- Statewide coverage focus

### 4. THRIVE Arkansas
- Treatment and housing integration
- Wraparound services

## Existing Artifacts

We have basic money_flow entries for these. Need to expand with:
- Authority references (enabling legislation if passed)
- Evidence items (Senate summaries, fiscal impact statements)
- Field validations (legislative record)

## Research Targets

### Legislative Sources
- Arkansas Senate Health Committee records
- BLR (Bureau of Legislative Research) fiscal impact
- Bill text if filed
- Sponsor statements

### Program Design
- Who administers each proposal?
- What is the funding mechanism?
- How do peer services fit?
- What is the relationship to existing programs?

### Comparison Points
- How do these differ from DHS-controlled pathways?
- Do they create new authority chains?
- What is the Medicaid relationship?

## Output Format

```json
{
  "batch_id": "rhtp_proposals_YYYYMMDD",
  "generated_at": "ISO timestamp",
  "mode": "legislative_proposal",
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

- [ ] All four proposals documented with consistent detail
- [ ] Administering bodies identified
- [ ] Funding mechanisms specified
- [ ] Peer service components highlighted
- [ ] Legislative status current
