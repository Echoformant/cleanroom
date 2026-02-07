# AGENT RUN: ARORP Recipient 990 Prep (Focused Batch)

**Priority:** HIGH - Connects settlement → nonprofit → outcomes
**Estimated time:** 30-45 min (research phase)
**Output:** List of EINs and org names for 990 extraction

## Objective

Identify all nonprofit recipients of ARORP funding that would have IRS Form 990 filings. Create a manifest for 990 extraction targeting these specific organizations.

## Known ARORP Recipients (from ingested batch)

| Organization | Amount | Project |
|--------------|--------|---------|
| John 3:16 Ministries | $2,357,912 | Women's Housing Expansion |
| CADCA | $385,745 + $284,600 | Training + CAN Project |
| Changes Behavioral Health, LLC | $381,139 | Washington County Recovery Center |
| Hot Springs School District | $237,794 | Prevention Recovery Program |
| Arkansas Pharmacists Association | $78,585 | Under 100 |
| Bridging the Gaps | $25,000 | COPE |
| C.H.A.N.G.E. | $25,000 | COPE |
| Union Rescue Mission | $3,552 | Naloxone HERO |

## Research Task

For each nonprofit recipient:

1. **Find EIN** - Look up on ProPublica Nonprofit Explorer or IRS database
2. **Verify 990 availability** - Check most recent filing year
3. **Note related entities** - Parent orgs, DBA names, fiscal sponsors

## Output: 990 Target Manifest

Create a JSON manifest:

```json
{
  "manifest_id": "990_ARORP_RECIPIENTS",
  "generated_at": "ISO timestamp",
  "purpose": "Extract 990 data for ARORP grant recipients",
  "targets": [
    {
      "organization": "John 3:16 Ministries",
      "ein": "XX-XXXXXXX",
      "arorp_amount": 2357912,
      "arorp_project": "ARORP-FY2023-WOMENS-HOUSING",
      "latest_990_year": "2023",
      "990_source_url": "https://projects.propublica.org/nonprofits/organizations/...",
      "notes": ""
    }
  ],
  "extraction_fields": [
    "total_revenue",
    "total_expenses",
    "program_expenses",
    "executive_compensation",
    "grants_received",
    "grants_paid",
    "board_members",
    "mission_statement"
  ]
}
```

## Additional Recipients to Research

Check ARORP project pages for additional recipients not in our batch:
- https://www.arorp.org/projects/
- Look for faith-based recovery homes
- Community coalitions
- Healthcare providers
- Law enforcement (for Sentinel TruNarc)

## Link to Existing Artifacts

For each 990 target, note which money_flow artifacts reference them:
- `MF-AR-ARORP-TO-JOHN316-WOMENS-HOUSING-FY2023`
- `MF-AR-ARORP-TO-CADCA-TRAINING-FY2023`
- etc.

## Success Criteria

- [ ] EINs identified for all nonprofit ARORP recipients
- [ ] 990 filing years confirmed
- [ ] Manifest ready for 990 extraction script
- [ ] Related organizations noted (for network mapping)

## Next Step

After this manifest is created, run 990 extraction formulas against these specific organizations to get:
- Revenue/expense trends
- Grant income (look for ARORP amounts)
- Board composition (potential overlap with state officials)
- Executive compensation
