# 990 Formula Library

**Status:** BUILDING
**Location:** `_formulas/990/`

## Structure

```
_formulas/
├── 990/
│   ├── README.md (this file)
│   ├── _raw/              # Unprocessed formulas from Codex
│   ├── _triage/           # One-pass sorted (keep/toss/upgrade)
│   ├── tier1_core/        # Essential extraction formulas
│   ├── tier2_useful/      # Good but not essential
│   ├── tier3_experimental/# May be useful, needs testing
│   └── _deprecated/       # Tossed but kept for reference
```

## Formula Categories

### Extraction Types
- **Identity** - EIN, name, address, fiscal year
- **Financial** - Revenue, expenses, assets, liabilities
- **Governance** - Officers, directors, compensation
- **Grants** - Received/paid, grant lists
- **Programs** - Program descriptions, accomplishments
- **Compliance** - Schedule flags, audit indicators

### Output Types
- **Single value** - Returns one field
- **List** - Returns array of items
- **Structured** - Returns object with multiple fields
- **Calculated** - Derives value from multiple inputs

## Formula Template

```markdown
# Formula: [NAME]

**Category:** [Extraction Type]
**Output:** [Single/List/Structured/Calculated]
**Tier:** [1/2/3]
**Tested:** [Yes/No]

## Purpose
[What this formula extracts]

## Input
- 990 Part/Schedule/Line: [reference]
- Required fields: [list]

## Formula
```
[the actual formula/logic]
```

## Example Output
```json
[sample output]
```

## Notes
[any caveats, edge cases, related formulas]
```

## Triage Criteria

### Tier 1 (Core) - KEEP
- Essential for artifact creation
- High accuracy on test data
- Directly links to money_flow or authority_reference

### Tier 2 (Useful) - KEEP
- Helpful context
- Reliable but not essential
- May support field_validation

### Tier 3 (Experimental) - EVALUATE
- Interesting but unproven
- Needs more testing
- May be promoted or deprecated

### Deprecated - TOSS (but archive)
- Low value
- Unreliable
- Redundant with better formula
