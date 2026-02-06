# Recommendations — Documentation, Methods, and Concepts

**Date:** 2026-02-05  
**Context:** Operation NAMI Clearlane / VECTOR 1  
**Purpose:** Actionable recommendations for improving documentation, methods, and operational clarity

---

## Documentation Recommendations

### 1. Create a Central Glossary

**Problem:** Key terms (VECTOR 1, Clearlane, Dossier, Agency, Capture) are defined across multiple files but no single glossary exists.

**Recommendation:** Create `docs/glossary.md` with:
- All canonical term definitions
- Cross-references to where each term is used
- Disambiguation of overlapping terms

---

### 2. Formalize Claim Assemblies as a First-Class Concept

**Problem:** The "CLAIM ASSEMBLIES!!!!" document describes a critical binding method that isn't referenced anywhere in the codebase.

**Recommendation:** 
- Create `docs/claim_assemblies.md` 
- Add a `_claims/` folder for Claim Assembly JSON files
- Consider a `claim_assembler.py` script to auto-generate claim tables from artifacts

---

### 3. Canonize the LLM Operating Instructions

**Problem:** The instruction YAML in temp_context has the full model behavioral contract (17+ rules) but only the schemas made it to copilot-instructions.md.

**Recommendation:** Create `docs/llm_operating_instructions.md` with:
- Model behavioral contract (all rules)
- Artifact category selection logic
- Output format specifications
- What the model must NEVER do

---

### 4. Version the Dossier State

**Problem:** No way to track "Dossier as of date X" — artifacts accumulate but snapshots aren't captured.

**Recommendation:**
- Add `_snapshots/` folder with dated JSON exports
- Create `snapshot.py` script to freeze current state
- Include in manifest: artifact count, orphan count, coverage %

---

### 5. Add Schema Validation to the Pipeline

**Problem:** Artifacts can be ingested with missing or malformed fields — no runtime validation exists.

**Recommendation:**
- Add `scripts/validate_schemas.py` using jsonschema
- Run on every `batch_ingest.py` execution
- Flag non-conformant artifacts before promotion

---

## Methods Recommendations

### 6. Implement Claim Table Export

**Problem:** The Claim Assembly concept describes a "Claim Table" format but no tool generates it.

**Recommendation:** Create `scripts/claim_table.py` that:
- Takes a claim statement as input
- Accepts artifact IDs by role (authority, evidence, validation)
- Outputs a formatted Claim Table (Markdown or JSON)

---

### 7. Add Coverage Metrics to Dashboard

**Problem:** Dashboard shows raw counts but not coverage ratios (validated vs. unvalidated, linked vs. orphan).

**Recommendation:** Add to dashboard:
- Validation Coverage: X% of money_flow/authority_reference have field_validation
- Linkage Density: Average links per artifact
- Orphan Rate: X% of artifacts are orphans

---

### 8. Create a "Gap Burndown" Visualization

**Problem:** Gap analysis produces a point-in-time count but no trend tracking.

**Recommendation:**
- Log gap counts to `_metrics/gap_history.json` on each run
- Add burndown chart to dashboard showing gap reduction over time
- Set targets: "Reduce orphans from 55 to 30 by end of week"

---

## Concept Recommendations

### 9. Define "Desk-Touch" as a Link Type

**Problem:** The Desk-Touch Map describes activation patterns but these aren't captured as artifact relationships.

**Recommendation:** Consider adding to linkage analysis:
- `desk_touch` link type
- Source: money_flow or authority_reference
- Target: desk identifier (AOC, DHS, ADH)
- Enables: "Show all artifacts that touch DHS desks"

---

### 10. Create "Clearlane Status" Field for Artifacts

**Problem:** The NAMI Clearlane Guide describes three status levels (Clearlane-Open, Clearlane-Conditional, Clearlane-Unverified) but these aren't tracked per artifact.

**Recommendation:** Add optional `clearlane_status` field:
- `"open"` — Authority validated, no capture risk
- `"conditional"` — Authority present, implementation pending
- `"unverified"` — Authority unclear or undocumented

---

### 11. Implement "Authority Gravity" Scoring

**Problem:** The Agency Doctrine describes "authority gravity" (DHS desks = high, AOC = low) but no quantitative scoring exists.

**Recommendation:**
- Assign gravity scores to desks/entities (1-5 scale)
- Calculate aggregate gravity for each money_flow path
- Flag high-gravity flows for manual review

---

### 12. Create an "Activation Potential" Report

**Problem:** The "Mapping Hidden Authority Layers" method describes identifying activation potential but no output format exists.

**Recommendation:** Create `scripts/activation_scanner.py` that:
- Takes a money_flow or authority_reference as input
- Identifies trigger classes that *could* activate
- Outputs an "Activation Potential Report" with risk levels

---

## Priority Ranking

| # | Recommendation | Effort | Impact | Priority |
|---|----------------|--------|--------|----------|
| 2 | Formalize Claim Assemblies | Medium | High | 🔴 Critical |
| 3 | Canonize LLM Instructions | Low | High | 🔴 Critical |
| 1 | Create Central Glossary | Low | Medium | 🟡 High |
| 5 | Add Schema Validation | Medium | High | 🟡 High |
| 7 | Add Coverage Metrics | Low | Medium | 🟡 High |
| 8 | Gap Burndown Visualization | Medium | Medium | 🟢 Medium |
| 4 | Version Dossier State | Low | Medium | 🟢 Medium |
| 6 | Claim Table Export | Medium | Medium | 🟢 Medium |
| 10 | Clearlane Status Field | Low | Medium | 🟢 Medium |
| 9 | Desk-Touch Link Type | Medium | Low | 🔵 Low |
| 11 | Authority Gravity Scoring | High | Medium | 🔵 Low |
| 12 | Activation Potential Report | High | Medium | 🔵 Low |

---

## Immediate Actions (Today)

1. ✅ Created READMEs for `server/`, `_data/`, `_agent_runs/`
2. ✅ Created `docs/canonization_status.md`
3. ✅ Created this recommendations file
4. ⏳ Run exhaustive schema cycle to reduce orphans
5. ⏳ After cycle: create `docs/claim_assemblies.md`
