# 990 mapping to Schema Artifacts v1 

Below are **runnable, low-friction patterns** for connecting **IRS Form 990 data**, **Clearlane artifact schemas**, and **other public datasets** into **repeatable scripts** that emit concrete outputs (tables, JSON, charts, reports). All approaches favor **minimal tooling**, **clear join keys**, **validation gates**, and **deterministic triggers**.

---

## **1\. Core Data Primitives (normalize first, automate later)**

### **Canonical identifiers (non-negotiable)**

Establish these once and reuse everywhere:

* **EIN** → primary join key for all IRS 990 data  
* **Tax Year** → secondary join key (YYYY)  
* **Organization Slug** → stable Clearlane internal ID  
* **Artifact Type \+ Version** → Clearlane schema control

**Runnable normalization step**

`normalize_990.py  → outputs/990_normalized.parquet`  
`normalize_clearlane.py → outputs/clearlane_entities.parquet`

**Validation gate**

* EIN must be 9 digits  
* Tax year ∈ \[1995, current\_year\]  
* Schema version declared and resolvable

Fail fast if any violation occurs.

---

## **2\. Easiest Reliable Pipeline (GitHub-native, zero infra)**

### **Pattern: GitHub Actions \+ Python \+ Flat Files**

**Why it works**

* Deterministic  
* Auditable  
* Free  
* Schedulable  
* Hardens cleanly

**Pipeline**

`cron trigger`  
  `→ fetch 990 index`  
  `→ filter EINs of interest`  
  `→ join with Clearlane artifacts`  
  `→ validate`  
  `→ emit outputs`  
  `→ commit results`

**Trigger**

`on:`  
  `schedule:`  
    `- cron: "0 6 * * 1"   # weekly`

**Outputs**

* `/outputs/org_summary.json`  
* `/outputs/financial_trends.csv`  
* `/outputs/red_flags.md`

**Validation gates**

* Missing EINs → skip \+ log  
* Schema mismatch → hard fail  
* Year-over-year deltas \> threshold → flag

---

## **3\. Event‑Triggered Scripts (data-driven, not time-based)**

### **Pattern: “New Data Detected” Trigger**

**Trigger logic**

* Hash last-seen IRS index file  
* Compare to previous run  
* Run only if changed

`if new_hash != stored_hash:`  
    `run_pipeline()`

**Why this matters**

* Avoids wasted runs  
* Ensures outputs always map to new information  
* Easier to trust results

**Outputs**

* Delta-only summaries  
* “What changed since last filing” artifacts

---

## **4\. Joining Clearlane Schemas to 990 (practical joins)**

### **Common joins that actually work**

| Clearlane Artifact | 990 Source | Join Key | Output |
| ----- | ----- | ----- | ----- |
| Org Profile | Core 990 | EIN | Master org record |
| Program Dossier | Schedule O | EIN \+ Year | Program evolution |
| Risk Signals | Part VI | EIN \+ Year | Governance flags |
| Financial Narrative | Part I & IX | EIN \+ Year | Spend \+ mission alignment |

**Validation gate**

* Require ≥1 financial section \+ ≥1 narrative section  
* If missing → mark “incomplete filing”

---

## **5\. Minimal Public Dataset Enrichment (optional but powerful)**

### **High-signal additions**

* IRS revocation list → compliance risk  
* Census geography → service area context  
* FEC (if applicable) → political exposure

**Join discipline**

* Never join without an explicit key map  
* Store mapping tables in `/mappings/`  
* Version mappings explicitly

---

## **6\. Concrete Output Patterns (always produce something)**

### **Pattern A: Deterministic JSON**

`{`  
  `"ein": "12-3456789",`  
  `"year": 2024,`  
  `"financial_health": "stable",`  
  `"governance_flags": ["no_whistleblower_policy"],`  
  `"program_spend_ratio": 0.81`  
`}`

### **Pattern B: Markdown Brief (human-readable)**

`## Org Snapshot — FY2024`  
`- Revenue: $4.2M (+6%)`  
`- Program Spend: 81%`  
`- Governance Flags: 1`  
`- Narrative Drift: Low`

### **Pattern C: CSV for dashboards**

* One row per EIN per year  
* Flattened, opinionated, boring (good)

---

## **7\. Hardening Rules (what makes this reliable)**

**Do**

* Treat schemas as contracts  
* Log every dropped record  
* Emit outputs even on partial failure (with flags)

**Avoid**

* Live APIs in critical joins  
* Silent coercion of missing fields  
* UI-first thinking before data contracts

---

## **8\. Next Experiments (low cost, high leverage)**

1. **Diff engine**  
   * Compare last two filings  
   * Emit “material changes only”  
2. **Rule packs**  
   * Encode governance / finance heuristics  
   * Version them like code  
3. **Artifact fan‑out**  
   * Same pipeline → JSON, Markdown, CSV  
   * One source of truth, many consumers  
4. **Human-in-the-loop checkpoints**  
   * Pause pipeline if confidence \< threshold  
   * Require manual approval to publish

---

### **Bottom line**

The most reliable path is **small, scriptable joins**, **explicit keys**, **fail-fast validation**, and **boring outputs** that can later feed dashboards, chat tools, or reports. Start with **scheduled scripts**, add **event triggers**, and only then layer interaction.

Below is a **second‑pass exploration** that goes deeper into **operational reliability**, **failure containment**, and **handoff durability**, without repeating earlier patterns. The emphasis here is on **scripts that keep working after you’re gone**.

---

## **1\. “Single‑Source Snapshot” Pattern (anti‑fragile baseline)**

### **Idea**

Every run produces a **complete, immutable snapshot** that downstream tools consume. No live joins. No partial state.

### **Runnable pipeline**

`trigger`  
 `→ pull raw 990 source(s)`  
 `→ pull Clearlane artifacts`  
 `→ pull public enrichments`  
 `→ normalize + join`  
 `→ validate`  
 `→ emit snapshot/`

### **Concrete output**

`snapshots/`  
  `2026-02-03/`  
    `orgs.parquet`  
    `finances.parquet`  
    `governance.parquet`  
    `metadata.json`

### **Join keys**

* EIN (string, zero‑padded)  
* Tax year (int)  
* Clearlane artifact ID (UUID or slug)

### **Validation gates**

* Snapshot must be internally referentially complete  
* Row counts logged and compared to prior snapshot  
* Any join loss \> X% hard‑fails the run

### **Why it hardens**

* Snapshots are portable  
* Easy rollback  
* Future tools only read files, not systems

---

## **2\. “Opinionated Output” Pattern (optimize for humans, not data purity)**

### **Idea**

Do the thinking once, encode it, and ship **final answers**, not raw fields.

### **Runnable script**

`build_answers.py`

### **Example derived outputs**

* `org_health_score.json`  
* `top_risk_flags.csv`  
* `program_spend_trend.md`

### **Validation gates**

* Every output must explain its own derivation  
* Missing inputs → explicit “unknown”, never zero  
* Scores require versioned rule sets

### **Why it hardens**

* Non‑technical users can trust outputs  
* Visuals become trivial  
* Logic is auditable

---

## **3\. “Rules-as-Data” Pattern (avoid hardcoded logic)**

### **Idea**

All interpretation lives in **YAML/JSON rules**, not code.

### **Example**

`program_spend_ratio:`  
  `source: part_ix.total_program_expense / part_i.total_expense`  
  `thresholds:`  
    `good: ">= 0.75"`  
    `watch: ">= 0.60"`  
    `risk: "< 0.60"`

### **Script behavior**

* Load rules  
* Apply to normalized data  
* Emit labeled outputs

### **Validation gates**

* Rules must declare source fields  
* Unknown fields invalidate the rule  
* Rule versions embedded in outputs

### **Why it hardens**

* Behavior changes without code changes  
* Future maintainers can reason about outcomes

---

## **4\. Trigger Strategy That Actually Scales**

### **Time triggers (predictable)**

* Weekly IRS index check  
* Monthly Clearlane artifact rebuild

### **Event triggers (more reliable)**

* New file appears in `/inputs/`  
* Schema version bump detected  
* Public dataset checksum changes

### **Hybrid trigger (best)**

`cron wakes`  
 `→ checks conditions`  
 `→ exits early or runs`

### **Validation gates**

* Trigger reason written to run log  
* No trigger \= no side effects

---

## **5\. Public Dataset Enrichment Without Fragility**

### **Principle**

**Mirror once, use locally forever.**

### **Runnable pattern**

`mirror_public_data.py`  
 `→ writes /mirrors/{dataset}/{date}.parquet`

### **Join discipline**

* No live HTTP joins  
* All joins against mirrored copies  
* Mirrors versioned and checksummed

### **Validation gates**

* Schema drift detection  
* Row count deltas tracked

---

## **6\. “Explainability Artifact” Pattern (trust survives turnover)**

### **Every run emits**

`run_report.md`

### **Contents**

* What ran  
* What changed  
* What failed  
* What was skipped  
* Confidence warnings

### **Why it matters**

* Humans can audit without reading code  
* Silent failures become impossible

---

## **7\. Minimal Tooling Stack (proven to last)**

* Python (stdlib \+ pandas)  
* Parquet / CSV / Markdown  
* GitHub Actions or cron  
* File system as API

No databases. No queues. No dashboards required.

---

## **8\. Failure Containment Rules (non‑negotiable)**

* Partial data → partial output with flags  
* Invalid joins → stop, do not guess  
* Missing years → annotate, do not interpolate  
* Every script exits with a reasoned status

---

## **9\. Next Experiments (incremental, safe)**

1. **Snapshot diffing**  
   * Highlight material changes only  
2. **Confidence scoring**  
   * Rate output reliability per org/year  
3. **Precomputed visuals**  
   * Charts rendered once, stored as images  
4. **Narrative synthesis**  
   * Deterministic text summaries per snapshot

---

### **Bottom line**

The most durable systems:

* Treat **files as contracts**  
* Treat **rules as data**  
* Treat **snapshots as truth**  
* Treat **explainability as a first‑class output**

Everything else (UI, chat, dashboards) becomes optional—and replaceable—once these foundations exist.

Below are **new, non‑overlapping patterns** that emphasize **operational reliability**, **data correctness**, and **repeatable execution**, extending beyond earlier runs without restating them.

---

## **1\. “Ledger‑First” Pipeline (outputs as append‑only facts)**

### **Core idea**

Every run appends **facts** to a ledger instead of overwriting derived tables. Derivations are reproducible views over the ledger.

### **Runnable pattern**

`trigger`  
 `→ fetch inputs`  
 `→ validate`  
 `→ append facts`  
 `→ materialize views`

### **Ledger schema (example)**

`facts/`  
  `filing_fact.parquet        # EIN, year, field, value, source`  
  `governance_fact.parquet`  
  `program_fact.parquet`

### **Join keys**

* EIN  
* Tax year  
* Fact type

### **Validation gates**

* Facts must reference a known source \+ timestamp  
* Duplicate facts allowed only if identical  
* Conflicting facts flagged, not resolved

### **Concrete outputs**

* `views/org_financial_summary.csv`  
* `views/governance_flags.json`

### **Why it hardens**

* History is never lost  
* Re‑runs are idempotent  
* New rules don’t require re‑ingestion

---

## **2\. “Schema Lock \+ Adapter” Pattern (future‑proof joins)**

### **Core idea**

Lock Clearlane schemas once. Everything else adapts *to* them.

### **Runnable pattern**

`schemas/`  
  `clearlane_v1.json`  
`adapters/`  
  `irs_990_to_clearlane.py`  
  `census_to_clearlane.py`

### **Join discipline**

* Adapters emit Clearlane‑shaped records only  
* No cross‑dataset joins outside adapters

### **Validation gates**

* Adapter output must fully satisfy schema  
* Unknown fields rejected  
* Missing required fields block downstream steps

### **Outputs**

* `normalized/clearlane_ready.parquet`

### **Why it hardens**

* External data drift is isolated  
* Internal contracts never change silently

---

## **3\. “Two‑Phase Run” Pattern (trust before publish)**

### **Phase 1: Build**

* Fetch, normalize, join  
* Produce **candidate outputs**  
* Run all validations

### **Phase 2: Promote**

* Only if Phase 1 passes  
* Move outputs from `/staging/` → `/published/`

### **Example trigger**

`cron → build`  
`file_event(staging/ok.flag) → promote`

### **Validation gates**

* All joins above minimum coverage  
* All required outputs present  
* No unresolved warnings

### **Outputs**

* `/published/*.csv`  
* `/published/*.md`

### **Why it hardens**

* Consumers never see partial or failed runs

---

## **4\. “Coverage‑Driven Execution” Pattern**

### **Core idea**

Run scripts only when **data completeness exceeds a threshold**.

### **Runnable logic**

`coverage = joined_rows / expected_rows`  
`if coverage >= 0.9:`  
    `run_derivations()`  
`else:`  
    `emit_coverage_report()`

### **Validation gates**

* Coverage threshold declared per output  
* Threshold failures still produce diagnostics

### **Outputs**

* `coverage_report.json`  
* Conditional final artifacts

### **Why it hardens**

* Prevents misleading outputs  
* Makes data gaps explicit

---

## **5\. “Key Registry” Pattern (joins that don’t rot)**

### **Core idea**

All joins go through a **single key registry**.

### **Registry example**

`keys/`  
  `ein_registry.csv`  
  `geo_registry.csv`

### **Registry fields**

* Canonical key  
* Alternate keys  
* Source  
* Confidence

### **Validation gates**

* Every join must reference registry  
* Unknown keys logged and quarantined

### **Outputs**

* `unmatched_keys.csv`  
* Clean joined datasets

### **Why it hardens**

* Joins remain explainable  
* Key drift becomes visible

---

## **6\. “Deterministic Re‑run” Pattern (audit‑ready)**

### **Core idea**

Every run can be replayed byte‑for‑byte.

### **Requirements**

* Input checksums stored  
* Rule versions stored  
* Code commit hash stored

### **Run metadata**

`run_manifest.json`

### **Validation gates**

* Manifest must exist before publish  
* Missing metadata blocks promotion

### **Outputs**

* Audit‑ready artifacts  
* Provenance baked in

---

## **7\. Minimal Trigger Matrix (clear, boring, reliable)**

| Trigger type | Use when | Example |
| ----- | ----- | ----- |
| Cron | Known refresh cadence | Weekly IRS scan |
| File hash change | External index updates | New 990 index |
| Schema version bump | Internal change | Clearlane v1 → v2 |
| Manual flag | Exceptional runs | Rebuild year |

All triggers funnel into the same entry script.

---

## **8\. Next Experiments (safe extensions)**

1. **Backfill runner**  
   * Rebuild a single EIN or year deterministically  
2. **Confidence annotations**  
   * Attach reliability scores to every output row  
3. **Pre‑joined gold tables**  
   * Freeze high‑value joins for downstream reuse  
4. **Automated anomaly surfacing**  
   * Outliers emitted as first‑class artifacts

---

### **Bottom line**

The most reliable systems:

* Separate **facts from interpretations**  
* Centralize **keys and schemas**  
* Require **explicit promotion**  
* Always emit **something auditable**

These patterns reduce brittleness while keeping tooling minimal and outcomes repeatable.

Below is a **fresh set of runnable, reliability‑first patterns** that have **not appeared in earlier runs**. Each pattern emphasizes **minimal tooling**, **explicit joins**, **clear validation**, and **repeatable outputs**.

---

## **1\. “Makefile‑Driven Pipeline” Pattern (boring but durable)**

### **Core idea**

Use a **Makefile** as the pipeline orchestrator. Each artifact declares its dependencies explicitly. Rebuilds happen only when inputs change.

### **Runnable pattern**

`make all`

`outputs/990_clean.parquet: inputs/990_raw.xml scripts/clean_990.py`  
	`python scripts/clean_990.py`

`outputs/clearlane.parquet: inputs/clearlane/*.json scripts/normalize_clearlane.py`  
	`python scripts/normalize_clearlane.py`

`outputs/joined.parquet: outputs/990_clean.parquet outputs/clearlane.parquet`  
	`python scripts/join.py`

### **Join keys**

* EIN (canonicalized)  
* Tax year  
* Artifact ID

### **Validation gates**

* Missing dependency halts build  
* Timestamp \+ checksum comparison  
* Join row loss threshold enforced

### **Outputs**

* Deterministic Parquet / CSV / Markdown

### **Why it hardens**

* No scheduler logic inside scripts  
* Dependency graph is explicit and inspectable

---

## **2\. “SQLite as Glue” Pattern (single‑file database)**

### **Core idea**

Use **SQLite** as a **temporary integration layer**, not a system of record.

### **Runnable pattern**

`run_pipeline.py → pipeline.db → exports/`

### **Tables**

* `filings (ein, year, field, value)`  
* `clearlane_artifacts (artifact_id, ein, schema_version)`  
* `enrichment (ein, source, value)`

### **Join keys**

* EIN  
* Year

### **Validation gates**

* Foreign key enforcement ON  
* NOT NULL constraints on join columns  
* Schema migration check on startup

### **Outputs**

* SQL views exported to CSV/JSON  
* Snapshot copy of `pipeline.db`

### **Why it hardens**

* Joins become declarative  
* Easy inspection with standard tools  
* Single portable file per run

---

## **3\. “Checksum‑First Trigger” Pattern**

### **Core idea**

Triggers are driven by **content change**, not time.

### **Runnable logic**

`compute checksums`  
 `→ compare to last run`  
 `→ decide which steps run`

### **Example**

`if checksum("irs_index.csv") != last_checksum:`  
    `run_990_ingest()`

### **Validation gates**

* Checksums stored per input  
* Changed input without downstream output \= error

### **Outputs**

* `input_manifest.json`  
* `changed_inputs.md`

### **Why it hardens**

* Prevents false freshness  
* Makes causality explicit

---

## **4\. “Schema‑Asserted Ingest” Pattern**

### **Core idea**

Every dataset must **pass schema assertions** before entering the pipeline.

### **Runnable pattern**

`ingest.py`  
 `→ assert schema`  
 `→ write normalized output`

### **Validation gates**

* Required columns present  
* Data types exact (no coercion)  
* Enumerations validated

### **Outputs**

* `*_validated.parquet`  
* `schema_errors.log`

### **Why it hardens**

* Breaks early on upstream drift  
* Prevents silent corruption

---

## **5\. “Join Coverage Ledger” Pattern**

### **Core idea**

Track **join success as data**, not logs.

### **Runnable output**

`join_coverage.csv`

### **Example fields**

* run\_id  
* join\_name  
* left\_rows  
* right\_rows  
* matched\_rows  
* match\_rate

### **Validation gates**

* Match rate below threshold blocks publish  
* Coverage trend compared to prior runs

### **Why it hardens**

* Join decay becomes measurable  
* Data quality is longitudinal

---

## **6\. “Single‑Entry Script” Pattern**

### **Core idea**

One script, one entry point. All triggers funnel into it.

### **Runnable pattern**

`python run.py --mode scheduled`  
`python run.py --mode event`  
`python run.py --mode backfill --ein 123456789`

### **Validation gates**

* Mode declared and logged  
* Unsupported mode \= hard fail

### **Outputs**

* Mode‑specific artifacts  
* Unified run report

### **Why it hardens**

* No divergent logic paths  
* Easier testing and replay

---

## **7\. Minimal Trigger Set (clarity over cleverness)**

| Trigger | Purpose |
| ----- | ----- |
| Cron | Predictable refresh |
| File checksum change | External updates |
| Manual flag | Controlled rebuild |
| Schema version bump | Forced re‑normalize |

All triggers only **decide whether to run**, never **how to run**.

---

## **8\. Concrete Outputs (always ship something)**

Each successful run emits:

* `joined_core.csv`  
* `derived_metrics.json`  
* `run_report.md`  
* `input_manifest.json`

Partial runs still emit diagnostics.

---

## **9\. Next Experiments (low risk)**

1. **Join simulation**  
   * Dry‑run joins to estimate coverage before ingest  
2. **Rule impact diff**  
   * Show how metric outputs change when rules change  
3. **One‑EIN rebuild**  
   * Deterministic rebuild for audits  
4. **Artifact freezing**  
   * Lock high‑confidence outputs for reuse

---

### **Bottom line**

The most reliable systems:

* Treat **builds like software**  
* Make **joins observable**  
* Trigger on **change, not hope**  
* Emit **auditable files every time**

These patterns remain small, explainable, and resilient as data sources evolve.

Below is a **new, distinct set of patterns** focused on **ultra‑minimal execution**, **mechanical reliability**, and **low cognitive load**, without repeating approaches from prior runs.

---

## **1\. “Shell‑First, Python‑Last” Pipeline (reduce surface area)**

### **Core idea**

Use **shell \+ CSV tools** for 80% of the work. Python only where unavoidable.

### **Runnable pattern**

`fetch → filter → join → validate → emit`

### **Example**

`curl IRS_990_INDEX.csv > index.csv`  
`csvgrep -c EIN -m "$(cat eins.txt)" index.csv > filtered.csv`  
`csvjoin -c EIN filtered.csv clearlane.csv > joined.csv`  
`python validate.py joined.csv`

### **Join keys**

* EIN (string, zero‑padded)  
* Tax year

### **Validation gates**

* CSV schema header match  
* Non‑empty join result  
* Row count delta vs prior run

### **Outputs**

* `joined.csv`  
* `summary.md`

### **Why it hardens**

* Fewer dependencies  
* Easy to debug line‑by‑line  
* Works everywhere

---

## **2\. “Data Contract File” Pattern (explicit expectations)**

### **Core idea**

Every pipeline has a **contract file** declaring what *must* be true for outputs to be trusted.

### **Example contract**

`inputs:`  
  `irs_990:`  
    `required_fields: [ein, tax_year, total_revenue]`  
  `clearlane:`  
    `required_fields: [artifact_id, ein]`  
`joins:`  
  `ein:`  
    `min_match_rate: 0.85`  
`outputs:`  
  `org_summary:`  
    `must_exist: true`

### **Runnable pattern**

`run.py → load contract → enforce → emit`

### **Validation gates**

* Contract evaluated before publish  
* Violations block promotion

### **Outputs**

* `contract_results.json`  
* Normal outputs if passed

### **Why it hardens**

* Expectations are explicit  
* Reviewable without reading code

---

## **3\. “Monotonic ID” Pattern (time‑safe joins)**

### **Core idea**

Never rely on filenames or timestamps alone. Assign a **monotonic run ID**.

### **Example**

`run_id = 202602030001`

### **Usage**

* Embedded in every output row  
* Stored in run manifest  
* Used for diffing and rollback

### **Validation gates**

* Run ID must be unique  
* All outputs must reference it

### **Outputs**

* `run_manifest.json`  
* Versioned artifacts

### **Why it hardens**

* Deterministic ordering  
* Audits become trivial

---

## **4\. “Fail‑Closed Joins” Pattern**

### **Core idea**

If a join cannot be confidently performed, **drop the record and log it**. Never guess.

### **Runnable logic**

`if ein not in registry:`  
    `quarantine(record)`

### **Validation gates**

* Quarantine count reported  
* Quarantine rate threshold enforced

### **Outputs**

* `joined_clean.csv`  
* `quarantine.csv`

### **Why it hardens**

* Prevents silent contamination  
* Makes uncertainty visible

---

## **5\. “Single‑Purpose Scripts” Pattern**

### **Core idea**

Each script does **exactly one thing** and produces exactly one artifact.

### **Example scripts**

* `fetch_990.py`  
* `normalize_990.py`  
* `join_clearlane.py`  
* `derive_metrics.py`

### **Triggering**

`orchestrator.sh calls scripts in order`

### **Validation gates**

* Script must emit its declared output  
* Exit code checked after each step

### **Why it hardens**

* Easier testing  
* Easier replacement  
* Easier recovery

---

## **6\. “Cold‑Start Safe” Pattern**

### **Core idea**

Pipelines must succeed even if **no prior state exists**.

### **Requirements**

* No dependency on previous outputs  
* Defaults defined for first run  
* Empty baselines handled explicitly

### **Validation gates**

* First‑run mode logged  
* No implicit assumptions allowed

### **Outputs**

* Baseline artifacts  
* Initialization report

### **Why it hardens**

* New environments don’t break  
* Disaster recovery is simple

---

## **7\. Trigger Simplification Rule**

### **Allowed triggers**

* Cron (time)  
* File presence  
* File checksum change  
* Manual invocation

### **Disallowed**

* Multi‑condition logic inside scripts  
* Hidden environment flags

### **Why it hardens**

* Predictable execution  
* No hidden control paths

---

## **8\. Concrete Output Minimum (per run)**

Every run must emit:

* One **joined dataset**  
* One **derived artifact**  
* One **run report**  
* One **error/quarantine artifact** (even if empty)

Runs without outputs are failures.

---

## **9\. Next Experiments (incremental, reversible)**

1. **Schema drift simulator**  
   * Intentionally break inputs to test gates  
2. **Join sensitivity analysis**  
   * Measure how outputs change with key loss  
3. **Artifact checksum catalog**  
   * Detect unintended output changes  
4. **Parallel EIN micro‑runs**  
   * Run pipeline per EIN for isolation

---

### **Bottom line**

The most reliable integrations are built from:

* **Small tools**  
* **Explicit contracts**  
* **Fail‑closed logic**  
* **Observable joins**  
* **Guaranteed artifacts**

When each run leaves behind concrete, auditable files, the system becomes durable by construction.

This run introduces **mechanical, execution‑level patterns** that emphasize **predictability, determinism, and low entropy**, without repeating prior structures or abstractions.

---

## **Pattern 1: “Index‑Anchored Execution” (trust the index, not the files)**

### **Core idea**

Treat the **IRS 990 index** as the authoritative trigger and scope‑definer. Everything else is downstream of it.

### **Runnable pipeline**

`load index`  
 `→ select target filings`  
 `→ resolve file paths`  
 `→ process only indexed items`  
 `→ emit outputs`

### **Join keys**

* EIN  
* Object ID / filing identifier  
* Tax year

### **Validation gates**

* Every processed filing must appear in index  
* No orphan files allowed  
* Index row count change logged

### **Example trigger**

* Index checksum change  
* New rows detected in index

### **Concrete outputs**

* `indexed_filings.csv`  
* `processed_filings.csv`  
* `index_delta.md`

### **Why it hardens**

Prevents processing stale, partial, or mis‑located data.

### **Next experiments**

* Index diff classifier (new vs amended vs corrected filings)

---

## **Pattern 2: “Key‑First Build” (no data moves until keys pass)**

### **Core idea**

Run **key validation and normalization before any data processing**.

### **Runnable pipeline**

`extract keys`  
 `→ normalize`  
 `→ validate registry`  
 `→ only then load full records`

### **Join keys**

* EIN (normalized once)  
* Clearlane artifact ID

### **Validation gates**

* EIN uniqueness within run scope  
* EIN format compliance  
* Registry presence or explicit absence

### **Example trigger**

* New EIN appears  
* Registry file updated

### **Concrete outputs**

* `key_validation_report.json`  
* `valid_keys.txt`  
* `invalid_keys.txt`

### **Why it hardens**

Stops bad joins before cost is incurred.

### **Next experiments**

* Confidence‑weighted key registry

---

## **Pattern 3: “Preflight \+ Execute” Split (aircraft rules)**

### **Core idea**

Every run has a **preflight stage** that decides whether execution is allowed.

### **Runnable pipeline**

`preflight.py`  
 `→ writes decision.json`  
`execute.py (only if approved)`

### **Preflight checks**

* Input availability  
* Schema compatibility  
* Join feasibility  
* Output destination writable

### **Validation gates**

* Preflight must explicitly approve  
* Missing approval blocks execution

### **Example trigger**

* Any trigger → preflight always runs first

### **Concrete outputs**

* `preflight_report.md`  
* `decision.json`

### **Why it hardens**

Separates *can we run?* from *run*.

### **Next experiments**

* Preflight cost estimation (rows, files, time)

---

## **Pattern 4: “Field‑Level Provenance” (trust travels with values)**

### **Core idea**

Every derived field carries its **origin metadata**.

### **Runnable pattern**

`derive field`  
 `→ attach source fields`  
 `→ attach rule ID`

### **Join keys**

* EIN  
* Tax year  
* Field name

### **Validation gates**

* No derived field without provenance  
* Provenance fields must exist upstream

### **Concrete outputs**

* `derived_fields.parquet`  
* `field_provenance.json`

### **Why it hardens**

Downstream users can audit without reverse‑engineering code.

### **Next experiments**

* Automated provenance graph export

---

## **Pattern 5: “Negative Space Reporting” (what’s missing is data)**

### **Core idea**

Explicitly emit **what could not be computed**.

### **Runnable pipeline**

`attempt derivations`  
 `→ collect failures`  
 `→ publish missingness artifacts`

### **Validation gates**

* Missing computations must be enumerated  
* Silent skips prohibited

### **Concrete outputs**

* `missing_metrics.csv`  
* `uncomputable_reasons.md`

### **Why it hardens**

Prevents false confidence and silent degradation.

### **Next experiments**

* Missingness trend tracking over time

---

## **Pattern 6: “One‑Output‑per‑Concern” Rule**

### **Core idea**

Each output answers **one question only**.

### **Examples**

* Financial health → one file  
* Governance risk → one file  
* Program allocation → one file

### **Validation gates**

* Output must map to a declared concern  
* Mixed‑concern outputs rejected

### **Example trigger**

* Concern‑specific rebuild flag

### **Why it hardens**

Prevents artifact sprawl and ambiguity.

### **Next experiments**

* Concern registry with ownership metadata

---

## **Pattern 7: “Dry‑Run Default” Execution**

### **Core idea**

Runs default to **no side effects** unless explicitly promoted.

### **Runnable pattern**

`run.py --dry-run`  
`run.py --publish`

### **Validation gates**

* Dry‑run artifacts must exist before publish  
* Publish requires explicit flag

### **Concrete outputs**

* `dry_run_outputs/`  
* `publish_diff.md`

### **Why it hardens**

Accidental writes become impossible.

### **Next experiments**

* Automatic dry‑run on every trigger

---

## **Pattern 8: Minimal Toolchain (frozen set)**

* POSIX shell  
* Python (stdlib \+ pandas)  
* CSV / Parquet  
* Git for state

No services. No credentials. No background daemons.

---

## **Guaranteed Outputs per Run**

Every run emits, regardless of success:

* One **primary dataset**  
* One **diagnostic artifact**  
* One **run manifest**  
* One **negative‑space artifact**

No output \= failure.

---

## **Bottom Line**

At scale, reliability comes from:

* **Index authority**  
* **Key primacy**  
* **Preflight enforcement**  
* **Provenance by default**  
* **Explicit missingness**  
* **Dry‑run bias**

These patterns minimize surprise and maximize repeatability while keeping tooling intentionally small.

Below is a **new execution‑oriented exploration** centered on **operability under automation**, **bounded scope**, and **mechanical repeatability**. None of the patterns below reuse structures from earlier runs.

---

## **Pattern A: “Scope‑Locked Runs” (prevent accidental expansion)**

### **Core idea**

Every run explicitly declares **what universe of data it is allowed to touch**. Nothing outside that scope is read or written.

### **Runnable pattern**

`scope.json → run.py → outputs/`

### **Scope declaration (example)**

`{`  
  `"eins": ["123456789", "987654321"],`  
  `"tax_years": [2023, 2024],`  
  `"artifacts": ["org_profile", "program_summary"]`  
`}`

### **Join keys**

* EIN  
* Tax year  
* Artifact type

### **Validation gates**

* Inputs must fall entirely within declared scope  
* Any out‑of‑scope record is rejected, not ignored  
* Scope hash embedded in outputs

### **Example triggers**

* Manual scope file update  
* Scheduled run with fixed scope

### **Concrete outputs**

* `scoped_join.csv`  
* `scope_audit.json`

### **Next experiments**

* Automatically generated scopes from index deltas  
* Per‑scope confidence scoring

---

## **Pattern B: “Column‑Minimal Joins” (reduce brittleness)**

### **Core idea**

Join using the **smallest possible column set**, then enrich later. This reduces schema drift risk.

### **Runnable pipeline**

`extract keys only`  
 `→ perform joins`  
 `→ reattach non‑key fields`

### **Join keys**

* EIN (only)  
* Tax year (only)

### **Validation gates**

* No non‑key columns allowed in join stage  
* Key cardinality checked before and after join

### **Example triggers**

* Schema change detected in any input  
* Scheduled rebuild after schema lock

### **Concrete outputs**

* `joined_keys.csv`  
* `enriched_output.parquet`

### **Next experiments**

* Key‑only dry runs to predict join loss  
* Automatic downgrade to key‑only outputs on failure

---

## **Pattern C: “Stage‑Stamped Artifacts” (progress visibility)**

### **Core idea**

Each artifact is stamped with the **stage it successfully completed**. Partial success is explicit.

### **Runnable pipeline**

`ingest → normalize → join → derive → publish`

### **Artifact stamp (example)**

`{`  
  `"artifact": "financial_summary",`  
  `"stage_completed": "join",`  
  `"blocked_at": "derive"`  
`}`

### **Validation gates**

* Stage order enforced  
* Later stages cannot overwrite earlier stamps

### **Example triggers**

* Any trigger; stage stamping is automatic

### **Concrete outputs**

* `artifact_status.json`  
* Stage‑specific datasets

### **Next experiments**

* Resume runs from last completed stage  
* Stage‑level SLA tracking

---

## **Pattern D: “Expectation‑Bound Metrics” (no free calculations)**

### **Core idea**

Metrics are computed **only if an explicit expectation exists** for that metric.

### **Runnable pattern**

`expectations.yaml → derive.py`

### **Expectation example**

`program_spend_ratio:`  
  `requires:`  
    `- total_program_expense`  
    `- total_expense`

### **Validation gates**

* Missing expectation → metric not computed  
* Missing required inputs → metric flagged, not imputed

### **Example triggers**

* Expectation file update  
* Scheduled metric refresh

### **Concrete outputs**

* `metrics.csv`  
* `metric_failures.csv`

### **Next experiments**

* Coverage dashboards for expectations  
* Expectation version diffs across runs

---

## **Pattern E: “Temporal Isolation” (time is a dimension, not metadata)**

### **Core idea**

Never mix tax years in the same computation unless explicitly declared.

### **Runnable pipeline**

`split by year`  
 `→ process independently`  
 `→ optionally aggregate`

### **Join keys**

* EIN  
* Tax year (mandatory in all joins)

### **Validation gates**

* Cross‑year joins blocked by default  
* Aggregations must declare time window

### **Example triggers**

* New year detected in index  
* Year‑specific rebuild trigger

### **Concrete outputs**

* `by_year/2024/*.csv`  
* `by_year/2025/*.csv`

### **Next experiments**

* Rolling‑window computations (declared explicitly)  
* Year‑over‑year comparators as separate artifacts

---

## **Pattern F: “Output Presence Contracts” (existence over correctness)**

### **Core idea**

Automation enforces **output existence first**, correctness second.

### **Runnable rule**

`if expected_output_missing:`  
    `run fails`

### **Validation gates**

* Every declared output must exist  
* Empty files allowed but must be annotated

### **Example triggers**

* All triggers; evaluated at end of run

### **Concrete outputs**

* `output_manifest.json`  
* Empty‑but‑valid placeholders when needed

### **Next experiments**

* Size and shape assertions per output  
* Output aging alerts

---

## **Pattern G: “Read‑Only Inputs, Write‑Only Outputs”**

### **Core idea**

Scripts never modify inputs and never read from output directories.

### **Runnable enforcement**

* Inputs mounted read‑only  
* Outputs written to fresh directory per run

### **Validation gates**

* Any attempt to write to inputs fails  
* Any attempt to read prior outputs fails

### **Example triggers**

* Any scheduled or event‑driven run

### **Concrete outputs**

* Immutable run directories  
* Clean separation between runs

### **Next experiments**

* Automated garbage collection of old runs  
* Promotion by copying, never overwriting

---

## **Minimal Tooling Assumption (unchanged)**

* Shell  
* Python  
* CSV / Parquet / JSON  
* File system

No services, no stateful infrastructure.

---

## **Guaranteed Artifacts Per Run**

Every run produces:

* One **primary joined dataset**  
* One **stage/status artifact**  
* One **validation or failure artifact**  
* One **manifest describing scope and expectations**

Absence of any artifact \= failed run.

---

## **Summary**

Reliability in scheduled or triggered data automation comes from:

* **Explicit scope**  
* **Key‑only joins**  
* **Stage visibility**  
* **Expectation‑bound computation**  
* **Time isolation**  
* **Output existence guarantees**

These patterns minimize surprise, reduce drift, and harden simple scripts into durable, repeatable systems.

This automation run focuses on **mechanically dependable integration patterns** that emphasize **bounded execution**, **low state**, and **predictable artifacts**. The patterns below are distinct from prior runs and are designed to survive unattended scheduling.

---

## **Pattern 1: “Windowed Ingest \+ Freeze” (control change explicitly)**

### **Core idea**

Ingest data only within a **declared temporal window**, then freeze it before any joins or derivations occur.

### **Runnable pipeline**

`define window`  
 `→ ingest 990s within window`  
 `→ ingest Clearlane artifacts within window`  
 `→ ingest public enrichments within window`  
 `→ freeze inputs`  
 `→ join + derive`

### **Join keys**

* EIN  
* Tax year  
* Filing receipt date (bounded by window)

### **Validation gates**

* No input outside declared window  
* All inputs copied to a frozen directory  
* Post-freeze reads only (enforced by path rules)

### **Example triggers**

* Hourly cron defining “last N hours” window  
* Event trigger when a new filing enters window

### **Concrete outputs**

* `frozen_inputs/`  
* `joined_window.csv`  
* `window_manifest.json`

### **Next experiments**

* Overlapping windows to test idempotency  
* Window replay for audit verification

---

## **Pattern 2: “Lookup-Only Enrichment” (no embedded joins)**

### **Core idea**

All enrichment data is accessed via **prebuilt lookup tables**, never by joining raw external datasets directly.

### **Runnable pipeline**

`build lookup tables`  
 `→ lock lookups`  
 `→ apply lookups to core data`

### **Join keys**

* EIN (primary)  
* ZIP or county code (secondary, optional)

### **Validation gates**

* Lookup tables must be complete before run  
* Lookup version hash embedded in outputs  
* Missing lookup values explicitly labeled

### **Example triggers**

* Lookup table refresh event  
* Scheduled core pipeline run (lookups reused)

### **Concrete outputs**

* `org_with_lookups.parquet`  
* `lookup_coverage.json`

### **Next experiments**

* Multiple lookup versions side-by-side  
* Confidence weighting per lookup source

---

## **Pattern 3: “Row-Classified Outputs” (data tells you what it is)**

### **Core idea**

Every output row is classified by **data completeness and reliability class**.

### **Runnable pipeline**

`join data`  
 `→ evaluate completeness`  
 `→ assign class`  
 `→ emit`

### **Example classes**

* `complete`  
* `partial_missing_990`  
* `partial_missing_clearlane`  
* `unjoinable`

### **Validation gates**

* Classification required for every row  
* No default or implicit class allowed

### **Example triggers**

* Any scheduled or event-driven run

### **Concrete outputs**

* `classified_join.csv`  
* `class_distribution.md`

### **Next experiments**

* Downstream filtering by class  
* Class-based suppression rules

---

## **Pattern 4: “Immutable Input Hash Chain” (prove nothing changed)**

### **Core idea**

Chain input hashes together to prove **input immutability across stages**.

### **Runnable pattern**

`hash each input`  
 `→ concatenate hashes`  
 `→ hash concatenation`  
 `→ store chain hash`

### **Validation gates**

* Chain hash recomputed before publish  
* Any mismatch aborts run

### **Example triggers**

* Any run; hash chain always enforced

### **Concrete outputs**

* `input_hash_chain.json`  
* `hash_verification.log`

### **Next experiments**

* Hash chain comparison across runs  
* Lightweight tamper detection alerts

---

## **Pattern 5: “Output Shape Contracts” (structure before values)**

### **Core idea**

Validate **row count, column count, and column order** before validating content.

### **Runnable pipeline**

`generate output`  
 `→ validate shape`  
 `→ validate values`  
 `→ publish`

### **Validation gates**

* Expected columns must exist  
* Column order must match contract  
* Row count must be ≥ declared minimum

### **Example triggers**

* Any trigger; shape validation is mandatory

### **Concrete outputs**

* `shape_validation.json`  
* Final datasets only if passed

### **Next experiments**

* Shape diffs across runs  
* Automatic shape contract generation

---

## **Pattern 6: “Single-Writer Rule” (eliminate race conditions)**

### **Core idea**

Only one process is ever allowed to write outputs for a given scope.

### **Runnable enforcement**

* Lock file created at run start  
* Lock released only after success or explicit failure

### **Validation gates**

* Existing lock blocks execution  
* Lock includes scope \+ run identifier

### **Example triggers**

* Overlapping cron runs  
* Concurrent event triggers

### **Concrete outputs**

* `run.lock`  
* `lock_status.json`

### **Next experiments**

* Scope-based locks (per EIN or year)  
* Lock timeout with forced abort logging

---

## **Pattern 7: “Explicit No-Op Runs” (silence is data)**

### **Core idea**

Runs that do nothing must still **emit a no-op artifact** explaining why.

### **Runnable behavior**

`evaluate triggers`  
 `→ if no work:`  
      `emit noop report`  
      `exit cleanly`

### **Validation gates**

* No-op reason required  
* No-op runs still produce manifest

### **Example triggers**

* Scheduled run with no data change  
* Event trigger filtered by scope/window

### **Concrete outputs**

* `noop_report.md`  
* `run_manifest.json`

### **Next experiments**

* No-op frequency tracking  
* Alerting on unexpected no-op streaks

---

## **Minimal Tooling (unchanged and enforced)**

* POSIX shell  
* Python (stdlib, optional pandas)  
* CSV / Parquet / JSON  
* File system \+ locks

No services, no queues, no databases.

---

## **Guaranteed Artifacts Per Run**

Every run produces at least:

* One **primary dataset** or explicit no-op artifact  
* One **manifest** (scope, window, hashes)  
* One **validation artifact**  
* One **classification or diagnostic artifact**

Absence of any artifact is treated as failure.

---

## **Summary**

The easiest and most reliable integrations are achieved by:

* **Bounding change with windows**  
* **Separating enrichment into lookups**  
* **Classifying data explicitly**  
* **Hashing inputs mechanically**  
* **Validating structure before meaning**  
* **Preventing concurrent writers**  
* **Treating no-ops as first-class outcomes**

These patterns harden simple scripts into durable, scheduled systems that remain auditable and predictable over time.

