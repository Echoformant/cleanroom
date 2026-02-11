# Entity Registry Schema

The entity registry catalogs organizations, offices, positions, and programs that appear in Arkansas public finance artifacts. It provides a canonical reference for "who is who" in the organizational hierarchy.

## Entity Types

| Type | Description | Examples |
|------|-------------|----------|
| `agency` | State-level department or independent agency | DHS, AOC, DFA |
| `division` | Major subdivision of an agency | DAABHS, DMS |
| `office` | Office within a division/agency | OSAMH |
| `position` | Named role (may or may not be person-specific) | Drug Director, OSAMH Director |
| `committee` | Advisory or governance body | SCPAC, Legislative Council |
| `partnership` | Multi-entity collaborative | ARORP |
| `provider` | Service delivery organization | CMHCs, treatment providers |
| `court` | Judicial entity | Drug Court (by district) |
| `program` | Funded program (may be multi-site) | Veterans Treatment Court |

## Schema

```json
{
  "entity_id": "ENTITY-AR-DHS-OSAMH",
  "entity_type": "office",
  "name": "Office of Substance Abuse and Mental Health",
  "abbreviation": "OSAMH",
  "parent": "ENTITY-AR-DHS-DAABHS",
  "children": ["ENTITY-AR-DHS-OSAMH-DIRECTOR"],
  "authorities": ["AUTH-AR-ACA-20-46-*"],
  "controls": ["MF-AR-OSAMH-*"],
  "fiscal_agent": true,
  "medicaid_provider": false,
  "contact": {
    "address": "",
    "phone": "",
    "website": ""
  },
  "notes": "",
  "editor_status": "pending"
}
```

## ID Patterns

| Pattern | Meaning |
|---------|---------|
| `ENTITY-AR-DHS` | Arkansas DHS (top-level) |
| `ENTITY-AR-DHS-DAABHS` | Division under DHS |
| `ENTITY-AR-DHS-OSAMH-DIRECTOR` | Position within office |
| `ENTITY-AR-AOC-DRUG-COURT-DIST01` | Specific court program |
| `ENTITY-AR-CMHC-OZARK` | Community Mental Health Center |

## Relationship to Other Artifacts

- **authority_reference**: Entities have `authorities[]` listing what governs them
- **money_flow**: `source`, `destination`, `intermediary` fields should match entity names
- **field_validation**: Validating entities should have registry entries

## Priority Entities to Populate

1. **DHS hierarchy** (DAABHS → OSAMH → positions)
2. **AOC** + Specialty Court Program Advisory Committee
3. **ARORP** + Attorney General opioid settlement administration
4. **45 Drug Courts** (by judicial district)
5. **CMHCs** (Community Mental Health Centers)
6. **Key federal sources** (SAMHSA, DOJ BJA, HRSA)
