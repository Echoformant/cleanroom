# AGENT RUN: Federal Authority Backfill (Focused Batch)

**Priority:** HIGH - Foundation for all federal fund flows
**Estimated time:** 30-45 min
**Output:** Batch JSON with ~15-25 artifacts

## Objective

Create authority_reference artifacts for the major federal statutes, regulations, and programs that Arkansas behavioral health funding flows through. These are referenced throughout Exhibit E, SAMHSA grants, and Medicaid rules but we lack the authority artifacts.

## Required Schema

```json
{
  "authority_id": "AUTH-US-...",
  "authority_type": "statute|regulation|act|court_order",
  "citation": "...",
  "administering_body": "...",
  "governs": [],
  "effects": "...",
  "editor_status": "pending"
}
```

## Federal Authorities Needed

### Block Grant Programs
1. **SAMHSA Block Grant** - 42 USC 300x (SAPT Block Grant)
2. **MHBG** - Mental Health Block Grant (42 USC 300x-1 et seq)
3. **SSBG** - Social Services Block Grant (Title XX)

### Medicaid Authorities
4. **Social Security Act Title XIX** - Medicaid enabling
5. **42 CFR 440** - Medicaid covered services
6. **42 CFR 438** - Managed Care regulations
7. **1115 Waiver Authority** - Section 1115 demonstration authority
8. **1915(b) Waiver** - Managed care waivers
9. **1915(c) Waiver** - HCBS waivers
10. **1915(i)** - State Plan HCBS option

### Opioid/SUD Programs
11. **21st Century Cures Act** - Opioid STR/SOR funding
12. **SUPPORT Act** - Comprehensive addiction treatment
13. **DATA 2000** - Buprenorphine prescribing (already have AUTH-US-DATA-2000)
14. **CARA** - Comprehensive Addiction and Recovery Act

### Recovery/Peer Support
15. **SAMHSA Recovery Definition** - 2012 working definition
16. **42 CFR 96** - Block Grant requirements
17. **Peer Support CMS guidance** - State Medicaid Director Letters

### Evidence/Prevention
18. **CDC Opioid Prescribing Guidelines** (already have AUTH-US-CDC-OPIOID-GUIDELINE-2016)
19. **NIDA Treatment Principles**
20. **SAMHSA Evidence-Based Practices Registry**

## Evidence Items Needed

For each authority, create an evidence item pointing to the source:

```json
{
  "evidence_id": "EVID-US-[source]-[topic]",
  "section": "AUTH-US-...",
  "claim_summary": "...",
  "evidence_type": "policy",
  "source": {
    "document": "...",
    "url": "https://...",
    "retrieved": "2026-02-06"
  },
  "confidence_level": "high",
  "editor_status": "pending"
}
```

## Output Format

```json
{
  "batch_id": "federal_authority_backfill_YYYYMMDD",
  "generated_at": "ISO timestamp",
  "mode": "authority_backfill",
  "total_turns": 1,
  "artifacts": {
    "authority_reference": [...],
    "evidence_item": [...]
  }
}
```

## Success Criteria

- [ ] All SAMHSA block grant authorities created
- [ ] Medicaid waiver types documented
- [ ] Opioid-specific federal programs captured
- [ ] Peer support federal guidance documented
- [ ] Source URLs point to official .gov sources
- [ ] governs[] arrays populated where Arkansas artifacts exist

## Usage

These federal authorities will be referenced by:
- Arkansas Medicaid State Plan amendments
- SAMHSA grant applications and awards
- Opioid settlement Exhibit E compliance
- Peer Support certification requirements
