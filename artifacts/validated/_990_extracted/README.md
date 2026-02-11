# 990 Extracted Data

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10  
**File Count:** 14,084 markdown files

---

## Purpose

This folder contains extracted data from IRS Form 990 XML files. Each markdown file represents one 990 filing with structured fields extracted by the Ollama LLM daemon.

## Processing Pipeline

```
_990_queue/          → daemon_990_extractor.py → _990_extracted/
(raw XMLs)              (Ollama LLM)              (markdown output)
                                                        ↓
                                               _990_done/ (processed XMLs)
```

## Output Format

Each extraction produces a markdown file with the naming pattern:
```
{ObjectId}_public_extracted.md
```

### Standard Fields Extracted

| Field | Description |
|-------|-------------|
| EIN | Employer Identification Number |
| Organization Name | Legal name of nonprofit |
| Tax Year | Filing year |
| Total Revenue | Sum of all revenue |
| Total Expenses | Sum of all expenses |
| Net Assets | End-of-year net assets |
| Program Service Revenue | Revenue from programs |
| Contributions/Grants | Donations and grants received |
| Number of Employees | Employee count |
| State | State of incorporation/operation |

### Key People Section

Lists officers, directors, trustees with:
- Name
- Title
- Date Signed (if available)
- Compensation (if reported)

### Programs Section

Extracted from Schedule O or Part III:
- Brief descriptions of major programs
- Program service accomplishments
- Mission statement excerpts

### Red Flags Section

Potential issues identified:
- Unusual financial ratios
- Missing required fields
- Governance concerns
- Related party transactions

## Sample Extraction

```markdown
# 990 Extraction: 201300069349300255_public

**Source File:** 201300069349300255_public.xml  
**Processed:** 2026-02-08T20:55:58.578452  
**Model:** llama3.2:latest

---

**Required Fields**
- **EIN**: 710521880
- **Organization Name**: AREA AGENCY ON AGING OF SOUTHEAST AR INC
- **Tax Year**: 2011
- **Total Revenue**: $165,875,511
...
```

## Processing Log

The `_processed.log` file tracks all processed files:
```
201300069349300255_public.xml
201400123456789012_public.xml
...
```

**Current Log Count:** 14,084 entries

## Usage

```powershell
# Count extracted files
(Get-ChildItem -Filter *.md -File).Count

# Find extractions for specific EIN
Get-ChildItem -Filter *.md | Select-String "EIN.*710521880"

# Find organizations by name pattern
Get-ChildItem -Filter *.md | Select-String "Organization Name.*AGING"

# Find high-revenue organizations
Get-ChildItem -Filter *.md | ForEach-Object {
    $content = Get-Content $_
    if ($content -match 'Total Revenue.*\$(\d+)') {
        if ([int]$matches[1] -gt 10000000) { $_.Name }
    }
}
```

## Model Performance

| Model | Speed | GPU Usage | Quality |
|-------|-------|-----------|---------|
| llama3:latest (8B) | ~240/hr | 92% | High |
| llama3.2:latest (3B) | ~1000/hr | 100% | Good |

## Known Issues

1. **Number Formatting:** Some dollar amounts may have misplaced commas/decimals due to LLM extraction
2. **Missing Fields:** Some 990-EZ filings may not have all standard fields
3. **Name Variations:** Organization names may vary across years

## Linking to Artifacts

990 data can be linked to artifacts via:
1. **EIN matching** using `_formulas/key_registry/`
2. **Name matching** against existing entities in money_flows
3. **Program analysis** for evidence_item creation
