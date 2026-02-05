# Composite Schema Cycling — Agent Mode Instructions

Use these instructions to run a complete 4-turn schema cycle with web research.

## Context

**Project:** Operation NAMI Clearlane / VECTOR 1  
**Purpose:** Generate Arkansas public-finance artifacts through schema rotation  
**Cycle ID:** CYCLE-20260205-023729-1e3051  
**Base Path:** `C:\Threshold\cleanroom\artifacts\validated`

## Your Task

Run through all 4 turns of the cycle. Each turn:
1. Read the prompt file
2. Research Arkansas law/budgets to fill the slots with REAL data
3. Save the filled response
4. Run the ingest and continue scripts

---

## TURN 1

### Step 1: Read the prompt
```
C:\Threshold\cleanroom\artifacts\validated\_cycles\CYCLE-20260205-023729-1e3051\turn_1_prompt.json
```

### Step 2: Research and fill
The anchor is `AUTH-AR-ACA-19-5-1144-ACCOUNTABILITY-COURT-FUND` (Arkansas Code §19-5-1144).

Research:
- Arkansas Code Annotated §19-5-1144 (Accountability Court Fund)
- FY2026 appropriations from Act 776 Section 31
- AOC specialty court funding

Fill the three slots with REAL Arkansas data.

### Step 3: Save response to
```
C:\Threshold\cleanroom\artifacts\validated\_cycles\CYCLE-20260205-023729-1e3051\turn_1_response.json
```

Response format:
```json
{
  "slots": {
    "money_flow": {
      "artifact": {
        "flow_id": "MF-AR-...",
        "source": "...",
        "intermediary": "...",
        "destination": "...",
        "amount": 0,
        "fund_type": "state",
        "fiscal_year": "2026",
        "restrictions": { "medicaid": false, "dhs_controlled": false },
        "statutory_basis": "...",
        "editor_status": "pending"
      }
    },
    "evidence_item": {
      "artifact": {
        "evidence_id": "EVID-AR-...",
        "section": "...",
        "claim_summary": "...",
        "evidence_type": "budget",
        "source": { "title": "...", "issuing_body": "...", "url": "..." },
        "confidence_level": "medium",
        "editor_status": "pending"
      }
    },
    "field_validation": {
      "artifact": {
        "fv_id": "FV-AR-...",
        "jurisdiction": "Arkansas",
        "validating_entity": "...",
        "alignment_status": "open",
        "evidence_basis": [],
        "disclosure_level": "public",
        "editor_status": "pending"
      }
    }
  }
}
```

### Step 4: Run scripts
```powershell
cd C:\Threshold\cleanroom\artifacts\validated
.\.venv\Scripts\python.exe scripts\schema_cycler.py ingest CYCLE-20260205-023729-1e3051 turn_1_response.json
.\.venv\Scripts\python.exe scripts\schema_cycler.py continue CYCLE-20260205-023729-1e3051
```

---

## TURN 2

### Step 1: Read the new prompt
```
C:\Threshold\cleanroom\artifacts\validated\_cycles\CYCLE-20260205-023729-1e3051\turn_2_prompt.json
```

The anchor will be the `money_flow` artifact you created in Turn 1.

### Step 2: Research and fill the three slots
Now fill: `authority_reference`, `evidence_item`, `field_validation`

### Step 3: Save to
```
C:\Threshold\cleanroom\artifacts\validated\_cycles\CYCLE-20260205-023729-1e3051\turn_2_response.json
```

### Step 4: Run scripts
```powershell
.\.venv\Scripts\python.exe scripts\schema_cycler.py ingest CYCLE-20260205-023729-1e3051 turn_2_response.json
.\.venv\Scripts\python.exe scripts\schema_cycler.py continue CYCLE-20260205-023729-1e3051
```

---

## TURN 3

### Step 1: Read
```
C:\Threshold\cleanroom\artifacts\validated\_cycles\CYCLE-20260205-023729-1e3051\turn_3_prompt.json
```

The anchor will be the `evidence_item` artifact from Turn 2.

### Step 2: Fill slots
Now fill: `authority_reference`, `money_flow`, `field_validation`

### Step 3: Save to
```
C:\Threshold\cleanroom\artifacts\validated\_cycles\CYCLE-20260205-023729-1e3051\turn_3_response.json
```

### Step 4: Run scripts
```powershell
.\.venv\Scripts\python.exe scripts\schema_cycler.py ingest CYCLE-20260205-023729-1e3051 turn_3_response.json
.\.venv\Scripts\python.exe scripts\schema_cycler.py continue CYCLE-20260205-023729-1e3051
```

---

## TURN 4

### Step 1: Read
```
C:\Threshold\cleanroom\artifacts\validated\_cycles\CYCLE-20260205-023729-1e3051\turn_4_prompt.json
```

The anchor will be the `field_validation` artifact from Turn 3.

### Step 2: Fill slots
Now fill: `authority_reference`, `money_flow`, `evidence_item`

### Step 3: Save to
```
C:\Threshold\cleanroom\artifacts\validated\_cycles\CYCLE-20260205-023729-1e3051\turn_4_response.json
```

### Step 4: Run scripts
```powershell
.\.venv\Scripts\python.exe scripts\schema_cycler.py ingest CYCLE-20260205-023729-1e3051 turn_4_response.json
.\.venv\Scripts\python.exe scripts\schema_cycler.py continue CYCLE-20260205-023729-1e3051
```

This will mark the cycle as completed.

---

## Check Status Anytime
```powershell
.\.venv\Scripts\python.exe scripts\schema_cycler.py status CYCLE-20260205-023729-1e3051
```

## Output Location
All generated artifacts are saved to:
```
C:\Threshold\cleanroom\artifacts\validated\_stubs\cycle_CYCLE-20260205-023729-1e3051\
```

---

## Schema Reference

### money_flow
| Field | Required | Type |
|-------|----------|------|
| flow_id | yes | string (MF-AR-* or AR_FY*) |
| source | yes | string |
| intermediary | yes | string or "None" |
| destination | yes | string |
| amount | yes | integer (USD) |
| fund_type | yes | "state" or "federal" |
| fiscal_year | yes | "2026" or "2025-2026" |
| restrictions.medicaid | yes | boolean |
| restrictions.dhs_controlled | yes | boolean |
| statutory_basis | yes | string |
| editor_status | yes | "pending" |

### authority_reference
| Field | Required | Type |
|-------|----------|------|
| authority_id | yes | string (AUTH-AR-* or AR-AUTH-*) |
| authority_type | yes | "statute", "regulation", or "policy" |
| citation | yes | string |
| administering_body | yes | string |
| governs | yes | array of strings |
| effects.access_limiting | yes | boolean |
| effects.appeal_mechanism | yes | boolean |
| editor_status | yes | "pending" |

### evidence_item
| Field | Required | Type |
|-------|----------|------|
| evidence_id | yes | string (EVID-AR-* or EV-AR-*) |
| section | yes | string |
| claim_summary | yes | string |
| evidence_type | yes | "budget", "audit", "policy" |
| source.title | yes | string |
| source.issuing_body | yes | string |
| source.url | yes | string |
| confidence_level | yes | "high", "medium", "low" |
| editor_status | yes | "pending" |

### field_validation
| Field | Required | Type |
|-------|----------|------|
| fv_id | yes | string (FV-AR-*) |
| jurisdiction | yes | "Arkansas" |
| validating_entity | yes | string |
| alignment_status | yes | "captured", "open", "mixed" |
| evidence_basis | yes | array of artifact IDs |
| disclosure_level | yes | "public" or "restricted" |
| editor_status | yes | "pending" |

---

## Rules
- Use REAL Arkansas data from web research
- Cite actual statutes, appropriation acts, and official URLs
- Set all `editor_status` to `"pending"`
- Do not reuse artifact IDs listed in `used_artifacts`
- Amount should be integer USD (no decimals)
