# PULSE DUMP — 2026-02-10 — 990 Data Spine Evolution

**Theme:** Structural hardening, epistemic governance, and institutional resilience for the IRS 990-based nonprofit identity spine.

**Context:** These 8 runs systematically expand the 990 data spine from "reliable backbone" into a governed, time-aware, authority-preserving, misuse-resistant system of record.

---

## Pulse 1: Structural Hardening & Constraint Engineering

---
pulse_number: 1
temporal_hash: "#021020262200"
thread_title: "990 Spine Run 1 — Make It Trustworthy"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - key_registry_candidate
  - data_integrity

priority: critical
impact: foundational

topics:
  - 990_spine
  - authority_tiering
  - negative_space
  - immutability
  - join_constraints
  - identity_windows

related_pulses:
  - "#021020261930"
fills_gaps:
  - "INCOMPLETE_CHAIN:key_registry_trust_levels"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T22:00:00Z"
promoted_to: []
---

### I. Authority Tiering (Formalize Trust Levels)

Introduce explicit authority classes for every attached datum:

| Tier | Source Type | Examples |
|------|-------------|----------|
| A | IRS-originated | 990, EO Master File |
| B | Federal award systems | USAspending, SAM |
| C | State payment systems | Transparency.Arkansas.gov |
| D | Third-party registries | NPI, charity watchdogs |
| E | Derived / inferred / normalized | Fuzzy matches, calculations |

Each field stores:
- `authority_tier`
- `source_system`
- `as_of_date`
- `confidence_score`

**Effect:** Prevents silent authority inversion (e.g., state payee names overwriting IRS identity).

### II. Negative Space Preservation

Explicitly encode absence as data:
- `no_990_required`
- `990-N_only`
- `no_federal_awards_detected`
- `inactive_but_not_revoked`

**Effect:** Prevents inference inflation and supports compliance-aware analytics.

### III. Spine Immutability Rules

Split data into:
- **Immutable spine layers:** EIN, filing existence, revocation status
- **Mutable overlays:** addresses, names, officers

Changes to immutable layers require:
- Multi-source corroboration
- Logged justification
- Versioned lineage

### IV. Join Preconditions as First-Class Objects

Every join is governed by a declared constraint set:
- Temporal overlap required?
- Name similarity threshold?
- Geography match required?
- Identifier freshness window?

Joins that fail constraints persist as **quarantined edges**, not discarded.

### V. Time-Bound Identity Windows

Model EIN identity as a sequence of validity windows:

```yaml
org_identity_id: "EIN-123456789-V2"
valid_from: "2018-01-01"
valid_to: "2023-06-30"
```

**Effect:** Allows correct historical joins (e.g., awards issued under old names).

### VI. Filing Behavior Metrics

Derive non-financial signals:
- Filing punctuality score
- Filing volatility (form switching, gaps)
- Amendment frequency
- Revocation/reinstatement cycles

These become organizational stability indicators, not financial metrics.

### VII. Officer & Address Churn Indices

Track:
- Executive turnover rate
- Address change frequency
- P.O. box vs physical drift

**Effect:** Surfaces shell-like behavior or administrative fragility.

### VIII. Confidence-Weighted Aggregations

Any roll-up metric computed as:

```
Σ(value × confidence × authority_weight)
```

Never raw sums.

**Promotion Note:** Not yet promoted. Establishes trust architecture for entire spine. Required before any downstream analytics.

---

## Pulse 2: Adversarial Modeling & Cross-Regime Interoperability

---
pulse_number: 2
temporal_hash: "#021020262215"
thread_title: "990 Spine Run 2 — Constraint Inversion & Counterfactuals"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - threat_modeling
  - data_integrity

priority: high
impact: foundational

topics:
  - 990_spine
  - adversarial_modeling
  - fiscal_sponsors
  - counterfactual_analysis
  - dormancy_detection
  - cross_regime

related_pulses:
  - "#021020262200"
fills_gaps:
  - "MISSING_VALIDATION:shell_detection"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T22:15:00Z"
promoted_to: []
---

### I. Adversarial Data Modeling

Assume:
- Deliberate name obfuscation
- EIN laundering via fiscal sponsors
- Shell reactivation after dormancy

Introduce threat models for nonprofit identity misuse:

| Pattern | Description |
|---------|-------------|
| Fiscal sponsor shadowing | Real activity hidden behind sponsor's EIN |
| EIN parking | Dormant EIN reactivated for new purpose |
| Officer recycling | Same individuals across multiple entities |

Output: `risk_surface_flags` (non-accusatory, structural only).

### II. Constraint Stress-Testing

Run synthetic stress tests:
- Randomized name drift
- Partial-year filings
- Address multiplexing

Measure spine breakpoints (where joins or identity continuity fail).

### III. Legal-Regime Alignment Layer

Align 990 spine with:
- UCC filings (credit exposure)
- State charity regulators
- Attorney general enforcement actions

This is not enrichment, but **jurisdictional coherence mapping**.

### IV. Accounting Standards Translation

Create a translation matrix between:
- IRS functional expenses
- GASB-style program reporting
- Grantor-specific cost categories

Enables cross-institution comparability without reclassification.

### V. "Should-Exist" Detection

Model expected filings based on:
- Past continuity
- Award activity
- Public signals (web presence, press)

Flag expected-but-missing filings as **analytical gaps**, not errors.

### VI. Dormancy vs Invisibility Differentiation

| State | Description |
|-------|-------------|
| Inactive | No filings, no operations |
| Administratively alive | Legal status current, operationally dark |
| Externally funded silent | Receiving money, no public disclosure |

Produces a **visibility state machine**, not a binary status.

### VII. Lag-Aware Analytics

All analytics tagged with:
- Reporting lag
- Correction latency
- Amendment probability

Prevents real-time misuse of retrospective data.

### VIII. Spine-Relative Metrics

Metrics expressed as:
- Deviation from org's own historical baseline
- Deviation from peer cohort trajectory

Avoids false normalization across heterogeneous nonprofits.

**Promotion Note:** Not yet promoted. Required before any identity resolution at scale.

---

## Pulse 3: Failure Modes & Edge Governance

---
pulse_number: 3
temporal_hash: "#021020262230"
thread_title: "990 Spine Run 3 — Designing for Breakage"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - data_integrity
  - validation_candidate

priority: high
impact: foundational

topics:
  - 990_spine
  - failure_modes
  - degradation_states
  - partial_truth
  - legal_translation
  - reversibility

related_pulses:
  - "#021020262215"
  - "#021020262200"
fills_gaps:
  - "MISSING_VALIDATION:spine_failure_handling"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T22:30:00Z"
promoted_to: []
---

### I. Spine Degradation States

Explicitly model degradation modes rather than binary validity:

| State | Description |
|-------|-------------|
| Complete | Filings current, identity stable |
| Lagged | Filings present but temporally stale |
| Fragmented | Filings exist but identity continuity broken |
| Orphaned | EIN valid, no recent filings, external activity detected |
| Contested | Conflicting authoritative records |

Each state constrains what operations are permitted.

### II. Partial Truth Tolerance

Allow the spine to operate under incomplete certainty:
- Fields can be "known false," not just unknown
- Contradictory facts can coexist with scoped validity

This avoids premature resolution and preserves investigative integrity.

### III. Legal Translation Layer

Map 990 concepts into legal primitives:

| 990 Concept | Legal Primitive |
|-------------|-----------------|
| "organization" | Legal personhood instances |
| "officer" | Fiduciary role assertions |
| "program service" | Declared public purpose |

Enables use in legal review, litigation support, and compliance, without reinterpretation.

### IV. Budgetary Translation Layer

Translate 990 financials into budgetary semantics:
- Fixed vs variable cost signals
- Restricted vs unrestricted resource indicators
- Operational leverage proxies

Allows scenario modeling without treating 990s as forecasts.

### V. Data Source Expansion

**Postal & Address Intelligence:**
- USPS delivery point validation
- CMRA / virtual office indicators

Used only to classify address types, not to judge legitimacy.

**Domain & Digital Persistence Signals:**
- Domain registration continuity
- Website liveness over time
- DNS ownership changes

Used as operational existence signals, never as proxies for impact.

### VI. Internal Consistency Validators

Check for:
- Mathematical impossibilities across years
- Governance structures that contradict reported size
- Program counts that exceed plausible administrative capacity

Flags inconsistencies without asserting fraud.

### VII. Narrative Consistency Checks

Compare:
- Mission statements over time
- Program descriptions year-over-year

Detect semantic drift or sudden pivots as **events**, not anomalies.

### VIII. Reversibility as a Requirement

All transformations must be:
- Reversible
- Replayable
- Attributable

This allows future reinterpretation as standards evolve.

### IX. Spine as "Nonprofit DNS"

Position the spine as:
- A resolution system for nonprofit identity
- Not a datastore, not a score engine

Other systems query, none overwrite.

**Promotion Note:** Not yet promoted. Establishes failure handling before production use.

---

## Pulse 4: Epistemic Controls & Lifecycle Modeling

---
pulse_number: 4
temporal_hash: "#021020262245"
thread_title: "990 Spine Run 4 — What the Spine Is Allowed to Know"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - epistemic_governance
  - lifecycle_modeling

priority: high
impact: foundational

topics:
  - 990_spine
  - knowledge_classification
  - epistemic_decay
  - operating_states
  - regulator_views
  - schema_evolution

related_pulses:
  - "#021020262230"
  - "#021020262215"
  - "#021020262200"
fills_gaps:
  - "MISSING_VALIDATION:epistemic_controls"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T22:45:00Z"
promoted_to: []
---

### I. Knowledge Classification Layer

Every field explicitly tagged as:

| Class | Description |
|-------|-------------|
| Declared | Self-reported by filer |
| Observed | Externally measured |
| Calculated | Mechanical derivation |
| Inferred | Model-based |
| Imputed | Gap-filled |

Downstream systems may only consume allowed classes.

### II. Epistemic Decay Modeling

Attach decay functions to fields:
- Financial figures decay slower than contact info
- Governance composition decays faster than legal status

This constrains reuse of stale data without deleting it.

### III. Organizational Operating States

Model organizations as transitioning through states:

```
formation → scaling → steady operation → contraction → wind-down → dormancy → legal persistence without operations
```

These are descriptive states, not performance labels.

### IV. Administrative Load Surfaces

Estimate administrative complexity from structure alone:
- Number of officers
- Committee density
- Filing complexity
- Related-entity disclosures

Used to contextualize reporting behavior, not efficiency.

### V. Regulator-Specific Views

Generate regulator-aligned representations:

| View | Purpose |
|------|---------|
| IRS view | Compliance focus |
| State charity regulator view | Registration/renewal |
| Grantor compliance view | Award conditions |

Same data, different structural emphasis, no duplication.

### VI. Procurement & Grants Interface Layer

Translate spine outputs into:
- Eligibility attestations
- Compliance checklists
- Audit readiness snapshots

Without embedding eligibility logic in the spine itself.

### VII. Bankruptcy & Insolvency Records

Attach public insolvency events:
- Filings
- Dismissals
- Restructurings

Used only to anchor timelines and operating states.

### VIII. Litigation Presence Signals

Track presence in:
- Civil dockets
- Consent decrees
- Settlements

Encoded as events, never as risk scores.

### IX. Path Dependency Encoding

Track how past states constrain future possibilities:
- Reinstatement after revocation
- Repeated amendments
- Chronic late filing

Used for trajectory analysis, not prediction.

### X. Schema Evolution Protocol

Formal rules for:
- Adding new fields
- Deprecating old ones
- Preserving backward compatibility

Prevents silent semantic drift.

**Promotion Note:** Not yet promoted. Required for institutional-grade governance.

---

## Pulse 5: Privacy, Cryptographic Integrity & Simulation

---
pulse_number: 5
temporal_hash: "#021020262300"
thread_title: "990 Spine Run 5 — Resilience & Computational Integrity"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - privacy_engineering
  - cryptographic_integrity
  - simulation_capability

priority: high
impact: foundational

topics:
  - 990_spine
  - hash_lineage
  - differential_privacy
  - synthetic_data
  - ml_governance
  - international_extension

related_pulses:
  - "#021020262245"
  - "#021020262230"
  - "#021020262215"
  - "#021020262200"
fills_gaps:
  - "MISSING_VALIDATION:cryptographic_integrity"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T23:00:00Z"
promoted_to: []
---

### I. Verifiable Data Lineage (Hash-Based)

Each immutable filing artifact is:
- Content-hashed
- Timestamped
- Chain-linked to prior versions

Enables independent verification that:
- No retroactive mutation occurred
- Transformations are provably derived

This supports evidentiary and audit-grade use without central trust.

### II. Selective Disclosure Proofs

Enable cryptographic proofs that:
- A condition is satisfied (e.g., filing exists, status valid)
- Without revealing underlying values

This allows compliance verification without data leakage.

### III. Differentially Private Aggregates

Allow aggregate statistics with:
- Calibrated noise
- Bounded contribution per EIN

Enables public or policy analytics without re-identification risk.

### IV. Field-Level Sensitivity Classes

| Class | Description |
|-------|-------------|
| public-safe | No restrictions |
| restricted-context | Limited use cases |
| non-exportable | Internal only |

Export, join, and compute operations enforce these constraints automatically.

### V. Synthetic Spine Generation

Generate statistically faithful synthetic 990 populations:
- Preserves distributions and correlations
- Breaks entity-level traceability

Used for:
- Method testing
- Policy simulation
- Tooling development

### VI. Counterfactual Policy Simulation

Model effects of hypothetical changes:
- Filing thresholds
- Reporting requirements
- Enforcement regimes

Outputs are system-level deltas, not organizational predictions.

### VII. Model Boundary Contracts

Any ML model touching the spine must declare:
- Allowed input fields
- Prohibited outputs
- Non-inferable attributes

Violations invalidate model deployment.

### VIII. Human-in-the-Loop Checkpoints

Critical transformations require:
- Explicit human attestation
- Recorded rationale
- Scope-limited approval

Prevents silent algorithmic drift.

### IX. Cost Surfaces for Queries

Every query returns:
- Computational cost
- Data exposure surface
- Aggregation depth

Discourages bulk misuse and enables internal budgeting.

### X. Complexity Caps

Hard limits on:
- Join fan-out
- Longitudinal depth
- Inference stacking

Prevents accidental construction of opaque or brittle analyses.

### XI. Degradation-Aware Outputs

When inputs degrade:
- Outputs annotate reliability loss
- Precision is reduced by design

System fails informatively, not silently.

### XII. Jurisdiction-Agnostic Core

Abstract core concepts:
- Legal entity
- Public purpose
- Financial disclosure
- Governing body

Allows parallel spines for non-US nonprofit regimes without schema fork.

**Promotion Note:** Not yet promoted. Establishes privacy and integrity architecture.

---

## Pulse 6: Semantic Governance & Economic Guardrails

---
pulse_number: 6
temporal_hash: "#021020262315"
thread_title: "990 Spine Run 6 — Meaning Before Data"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - semantic_governance
  - anti_financialization

priority: high
impact: foundational

topics:
  - 990_spine
  - formal_ontology
  - polysemy_control
  - resource_flow
  - decision_readiness
  - institutional_memory

related_pulses:
  - "#021020262300"
  - "#021020262245"
  - "#021020262230"
  - "#021020262215"
  - "#021020262200"
fills_gaps:
  - "MISSING_VALIDATION:semantic_controls"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T23:15:00Z"
promoted_to: []
---

### I. Formal Ontology Layer

Define a controlled ontology for:
- organization
- activity
- program
- revenue type
- expense function
- governing role
- related entity

All fields map to ontology terms with:
- Scope
- Exclusions
- Allowed transformations

Prevents semantic drift across systems and over time.

### II. Polysemy Control (One Term, Many Meanings)

Explicitly encode when identical labels mean different things:

| Term | Context A | Context B |
|------|-----------|-----------|
| "program service" | IRS meaning | Grantor meaning |
| "affiliate" | Tax definition | Corporate definition |
| "support" | Revenue type | Functional expense |

Disambiguation is structural, not interpretive.

### III. Anti-Financialization Constraints

Prohibit direct derivation of:
- ROI
- Cost-effectiveness ratios
- Efficiency rankings

The spine enforces economic description, not valuation or optimization.

### IV. Resource Flow Topology

Model flows as:

```
sources → controls → uses
```

Not "income vs expenses," but **control surfaces over resources**, preserving donor restriction semantics.

### V. Decision-Readiness States

Encode whether the spine is suitable for:

| Use Case | Readiness |
|----------|-----------|
| Compliance confirmation | ✓ |
| Eligibility screening | ✓ |
| Investigative support | Limited |
| Policy analysis | ✓ |

States gate downstream use automatically.

### VI. Advisory vs Determinative Boundary

Every output explicitly classified as:
- Descriptive
- Advisory
- Evidentiary

**No output is determinative by default.**

### VII. Precedent Encoding

Store historical interpretations:
- Prior regulator treatment
- Prior audit resolutions
- Prior classification decisions

These are preserved as **precedents**, not facts.

### VIII. Organizational Narrative Thread

Maintain a neutral, event-linked narrative spine:
- Formation rationale
- Major restructurings
- Mission reframings

Narratives are sourced, versioned, and non-analytic.

### IX. Semantic Consistency Checks

Detect contradictions:
- Exempt purpose vs disclosed activities
- Governance structure vs stated independence
- Program descriptions vs expense allocations

Flags are semantic, not numeric.

### X. Role–Authority Alignment Validation

Check that:
- Individuals listed have authority consistent with role
- Signatures align with disclosed governance

Used to detect structural misalignment, not misconduct.

### XI. Plug-in Validation Modules

Allow independent validators to attach:
- Rule sets
- Semantic checks
- Jurisdiction-specific constraints

Modules can be added or retired without altering the core spine.

**Promotion Note:** Not yet promoted. Establishes semantic governance layer.

---

## Pulse 7: Control Theory & Evidentiary Boundaries

---
pulse_number: 7
temporal_hash: "#021020262330"
thread_title: "990 Spine Run 7 — Stability Over Insight"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - control_theory
  - evidentiary_alignment
  - misinterpretation_defense

priority: high
impact: foundational

topics:
  - 990_spine
  - feedback_loops
  - legal_evidence
  - narrative_collapse
  - proxy_abuse
  - policy_distortion

related_pulses:
  - "#021020262315"
  - "#021020262300"
  - "#021020262245"
  - "#021020262230"
  - "#021020262215"
  - "#021020262200"
fills_gaps:
  - "MISSING_VALIDATION:control_stability"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T23:30:00Z"
promoted_to: []
---

### I. Feedback Loop Identification

Explicitly model where the spine influences behavior:
- Grant eligibility heuristics
- Regulatory scrutiny targeting
- Public reputation signals

These are tagged as **feedback-sensitive surfaces** and throttled to prevent runaway reinforcement.

### II. Control vs Observation Separation

Separate:
- **Observed state:** What filings show
- **Controlled state:** What actors can change in response

Prevents analysts from mistaking adaptive behavior for structural truth.

### III. Legal Evidence Alignment

Classify every field by admissibility posture:

| Class | Description |
|-------|-------------|
| Hearsay-equivalent | Filer assertion only |
| Self-attested | Signed declaration |
| Corroborated | Multiple source agreement |
| Externally certified | Third-party validation |

Allows lawful use without reclassification or overreach.

### IV. Burden-of-Proof Encoding

Attach an explicit burden model:
- What the data can support
- What it cannot support
- What additional evidence would be required

Transforms the spine into a **boundary-aware evidentiary substrate**.

### V. Narrative Collapse Guards

Detect when multi-field interpretations collapse into:
- Moral judgments
- Performance claims
- Causal assertions

System intervenes by:
- Downgrading output resolution
- Inserting interpretive constraints
- Suppressing misleading composites

### VI. Proxy Abuse Detection

Monitor for repeated use of weak proxies:
- Overhead ratios
- Officer compensation without context
- Filing gaps as intent signals

Flags methodological misuse, not organizations.

### VII. Policy-Induced Behavior Modeling

Track changes following:
- Regulatory updates
- Enforcement campaigns
- Public reporting changes

Distinguish:
- Genuine operational change
- Reporting adaptation
- Disclosure minimization

### VIII. Measurement-Induced Distortion

Identify fields likely to distort reality when measured:
- Program categorization
- Beneficiary counts
- Outcome descriptions

These fields carry **observer-effect warnings**.

### IX. Population-Level Consistency Laws

Enforce macro constraints:
- Aggregate revenue plausibility by sector
- Officer counts vs population size
- Filing volume vs IRS capacity

Catches systemic ingestion or normalization errors.

### X. Cross-Cohort Drift Detection

Detect when entire cohorts shift simultaneously:
- Suggests schema change
- Reporting instruction change
- Upstream data mutation

Prevents false attribution to organizational behavior.

### XI. Non-Causal Trajectory Encoding

Represent change as:
- Sequences
- Phase transitions
- Regime shifts

Explicitly prohibit causal labeling unless externally sourced.

### XII. Read-Only Canonical Core

Define a minimal, frozen canonical core:
- Existence
- Filing events
- Legal status

All analysis occurs in detached interpretive layers.

### XIII. Interpretation Sandboxes

Require experimental metrics to live in:
- Isolated namespaces
- Time-limited scopes
- Non-exportable contexts

Prevents experimental logic from hardening into doctrine.

**Promotion Note:** Not yet promoted. Establishes control-theoretic stability layer.

---

## Pulse 8: Authority, Incentives & Institutional Game Theory

---
pulse_number: 8
temporal_hash: "#021020262345"
thread_title: "990 Spine Run 8 — Power-Aware Design"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - game_theory
  - incentive_modeling
  - power_transparency

priority: high
impact: foundational

topics:
  - 990_spine
  - authority_provenance
  - legitimacy_gradient
  - strategic_disclosure
  - compliance_gaming
  - regulatory_arbitrage
  - contestability

related_pulses:
  - "#021020262330"
  - "#021020262315"
  - "#021020262300"
  - "#021020262245"
  - "#021020262230"
  - "#021020262215"
  - "#021020262200"
fills_gaps:
  - "MISSING_VALIDATION:incentive_modeling"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T23:45:00Z"
promoted_to: []
---

### I. Authority Provenance Layer

Explicitly encode who is asserting or relying on the spine:

| Authority Class | Examples |
|-----------------|----------|
| Filer | Self-reported data |
| Regulator | IRS, state charity office |
| Auditor | Independent examination |
| Grantor | Award conditions |
| Researcher | Analytical use |
| Media intermediary | Public reporting |

Each authority class has:
- Permitted claims
- Prohibited interpretations
- Escalation boundaries

**Prevents authority laundering via data reuse.**

### II. Legitimacy Gradient Encoding

Model legitimacy as contextual and bounded, not binary:
- Legally valid but institutionally contested
- Compliant but procedurally fragile
- Accepted historically but deprecated prospectively

Allows coexistence of lawful ambiguity without forced resolution.

### III. Strategic Disclosure Surface Mapping

Identify fields most susceptible to strategic shaping:
- Program descriptions
- Officer titles
- Related-entity narratives
- Public benefit language

Mark these as **high-incentive fields** requiring contextualization, not normalization.

### IV. Incentive Distortion Warnings

Attach warnings when downstream use creates perverse incentives:
- Grant screening based on reporting artifacts
- Reputational scoring from compliance timing
- Enforcement targeting via proxy metrics

The system flags **use-induced distortion**, not data defects.

### V. Compliance Optimization Detection

Detect patterns consistent with:
- Minimum viable disclosure
- Form-maximization without operational change
- Defensive over-documentation

Logged as **strategic adaptation events**, not misconduct.

### VI. Regulatory Arbitrage Mapping

Track movement across:
- Filing thresholds
- Entity structures
- Fiscal sponsorship arrangements
- Jurisdictional regimes

Encoded as structural transitions, not intent signals.

### VII. Multi-Actor Interaction Modeling

Represent the nonprofit ecosystem as interacting agents:
- Nonprofits
- Regulators
- Funders
- Watchdogs
- Data aggregators

The spine tracks interaction patterns, not outcomes.

### VIII. Policy Feedback Anticipation

Model how changes to the spine's use could alter behavior:
- Increased disclosure avoidance
- Form homogenization
- Narrative convergence

Used to evaluate second-order policy risk before deployment.

### IX. Plausibility vs Accuracy Separation

Differentiate:
- Numerically accurate but institutionally implausible
- Plausible but weakly supported
- Accurate within a narrow procedural context

Prevents false confidence from formal correctness alone.

### X. Cross-Institution Contradiction Preservation

Allow contradictions to persist:
- IRS vs state regulator
- Auditor vs filer
- Grantor vs public record

Contradictions are indexed, not resolved.

### XI. Organizational Strategy Trajectories

Track long-run strategies:
- Professionalization
- Decentralization
- Compliance hardening
- Reputational shielding

Derived only from structural change sequences.

### XII. Spine as Power-Transparent Infrastructure

Expose where power concentrates:
- Which actors define meaning
- Who benefits from standardization
- Who bears compliance cost

This is descriptive, not normative.

### XIII. Interpretive Asymmetry Controls

Prevent asymmetry where:
- One actor gains decisive insight
- Others cannot contest interpretation

Achieved via:
- Shared context injection
- Interpretation traceability
- Contestability hooks

### XIV. Strategic Use Review Gates

High-impact uses (e.g., eligibility, enforcement support) require:
- Documented justification
- Alternative interpretations logged
- Explicit rejection of unsupported inferences

These gates are procedural, not discretionary.

**Promotion Note:** Not yet promoted. Completes the 8-run evolution series. Ready for integration into FIS architecture documentation.

---

## Summary: 990 Spine Evolution Arc

| Run | Focus | Key Capability |
|-----|-------|----------------|
| 1 | Structural Hardening | Authority tiering, immutability, time windows |
| 2 | Adversarial Modeling | Threat models, counterfactuals, cross-regime |
| 3 | Failure Modes | Degradation states, partial truth, reversibility |
| 4 | Epistemic Controls | Knowledge classification, decay, lifecycle |
| 5 | Privacy & Integrity | Hash lineage, differential privacy, simulation |
| 6 | Semantic Governance | Ontology, anti-financialization, decision boundaries |
| 7 | Control Theory | Feedback loops, evidentiary limits, narrative guards |
| 8 | Game Theory | Authority provenance, incentives, contestability |

**Net Result:** The 990 data spine evolves from "a reliable backbone" into "a governed, time-aware, authority-preserving, misuse-resistant system of record that tolerates uncertainty without hiding it."

**Next Vectors (Unexplored):**
- Fiscal sponsorship disentanglement at event level
- Court-supervised nonprofit lifecycle modeling
- Merger/split/successor organization lineage
- International NGO equivalency modeling
- Grant-condition execution tracing

---

## Pulse 9: Index-Led Orchestration Pattern

---
pulse_number: 9
temporal_hash: "#021020262400"
thread_title: "990 Integration Run 1 — Index as Source of Truth"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - pipeline_pattern
  - automation_candidate

priority: high
impact: foundational

topics:
  - 990_spine
  - index_driven
  - pipeline_orchestration
  - scope_control
  - validation_gates

related_pulses:
  - "#021020262345"
  - "#021020261930"
fills_gaps:
  - "INCOMPLETE_CHAIN:990_processing_scope"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T24:00:00Z"
promoted_to: []
---

### Core Idea

Treat the IRS Form 990 **index file** as the sole driver of scope, ordering, and eligibility. No downstream file is processed unless referenced in the index.

### Runnable Pipeline

```
load index
 → filter scope (year, status)
 → resolve file paths
 → process referenced filings only
```

### Join Keys

| Key | Purpose |
|-----|---------|
| EIN | Canonical org identifier |
| Object ID / Filing ID | Specific filing instance |
| Tax Year | Temporal scope |

### Validation Gates

- Every processed filing must appear in index
- Index row count recorded and compared to prior run
- Missing referenced files block execution

### Example Triggers

- Scheduled index refresh
- Event: index checksum change

### Concrete Outputs

| Artifact | Purpose |
|----------|---------|
| `indexed_scope.csv` | What's in scope for this run |
| `processed_filings.csv` | What was actually processed |
| `index_audit.json` | Validation results |

### Next Experiments

- Index delta classification (new vs amended vs superseded)
- Index-only dry runs to forecast workload

**Promotion Note:** Not yet promoted. Pipeline pattern for 990 processing automation.

---

## Pulse 10: Schema-Pinned Inputs Pattern

---
pulse_number: 10
temporal_hash: "#021020262405"
thread_title: "990 Integration Run 2 — Fail on Drift, Not Results"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - pipeline_pattern
  - validation_candidate

priority: high
impact: foundational

topics:
  - 990_spine
  - schema_validation
  - drift_detection
  - input_contracts
  - fail_fast

related_pulses:
  - "#021020262400"
  - "#021020262245"
fills_gaps:
  - "MISSING_VALIDATION:input_schema_enforcement"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T24:05:00Z"
promoted_to: []
---

### Core Idea

Each input dataset is pinned to an **explicit schema contract**. Any schema drift fails the run before joins occur.

### Runnable Pipeline

```
load schemas
 → validate inputs against schemas
 → proceed only if all match
```

### Join Keys

| Key | Type |
|-----|------|
| EIN | string |
| Tax Year | integer |

### Validation Gates

- Field presence and type must match schema
- Unexpected extra fields flagged
- Missing required fields block run

### Example Triggers

- Scheduled validation job
- Event: upstream data refresh

### Concrete Outputs

| Artifact | Purpose |
|----------|---------|
| `schema_validation_report.json` | Pass/fail with details |
| No data outputs | If validation fails |

### Next Experiments

- Schema version compatibility matrices
- Controlled schema evolution with grace windows

**Promotion Note:** Not yet promoted. Enables fail-fast validation before expensive processing.

---

## Pulse 11: Join-Loss Accounting Pattern

---
pulse_number: 11
temporal_hash: "#021020262410"
thread_title: "990 Integration Run 3 — Loss Is Measured, Not Hidden"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - pipeline_pattern
  - audit_candidate

priority: high
impact: foundational

topics:
  - 990_spine
  - join_accounting
  - data_loss
  - match_classification
  - audit_trail

related_pulses:
  - "#021020262405"
  - "#021020262400"
fills_gaps:
  - "MISSING_VALIDATION:join_loss_tracking"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T24:10:00Z"
promoted_to: []
---

### Core Idea

Every join explicitly accounts for **matched, unmatched, and dropped rows** as first-class outputs.

### Runnable Pipeline

```
attempt join
 → classify rows
 → emit all classes
```

### Join Keys

| Key | Purpose |
|-----|---------|
| EIN | Canonical org identifier |
| Tax Year | Temporal alignment |

### Validation Gates

- Sum of matched + unmatched equals input rows
- Drop reasons required for every non-match
- Loss rate compared against threshold

### Example Triggers

- Any join execution

### Concrete Outputs

| Artifact | Purpose |
|----------|---------|
| `joined_rows.csv` | Successful matches |
| `unmatched_rows.csv` | Failed matches with reasons |
| `join_loss_summary.json` | Aggregate statistics |

### Conservation Law

```
input_rows = matched_rows + unmatched_left + unmatched_right + dropped_rows
```

If this equation doesn't balance, the join is invalid.

### Next Experiments

- Historical loss trend tracking
- Automated alerts on new loss patterns

**Promotion Note:** Not yet promoted. Critical for auditable data pipelines.

---

## Pulse 12: Artifact-First Outputs Pattern

---
pulse_number: 12
temporal_hash: "#021020262415"
thread_title: "990 Integration Run 4 — Clearlane Defines Shape"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - pipeline_pattern
  - clearlane_core

priority: critical
impact: foundational

topics:
  - 990_spine
  - artifact_schema
  - output_shape
  - field_mapping
  - clearlane_integration

related_pulses:
  - "#021020262410"
  - "#021020262405"
  - "#021020262400"
fills_gaps:
  - "INCOMPLETE_CHAIN:990_to_clearlane"
strengthens:
  - "key_registry.yaml"
  - "money_flow/*"
  - "entity_registry/*"

created_at: "2026-02-10T24:15:00Z"
promoted_to: []
---

### Core Idea

Clearlane artifact schemas define **output shape first**; IRS and public data are adapted to fit, not the reverse.

### Runnable Pipeline

```
load Clearlane artifact schema
 → map IRS/public fields
 → populate artifact
```

### Join Keys

| Key | Purpose |
|-----|---------|
| EIN | Canonical org identifier |
| Artifact ID | Target artifact instance |
| Tax Year | If applicable |

### Validation Gates

- Artifact schema must be satisfied
- Unmapped required fields block output
- Extra fields prohibited

### Field Mapping Contract

```yaml
# Example: 990 → entity_registry mapping
entity_id: "ENTITY-AR-{EIN}"
name: Return/ReturnHeader/Filer/BusinessName/BusinessNameLine1Txt
ein: Return/ReturnHeader/Filer/EIN
address:
  street: Return/ReturnHeader/Filer/USAddress/AddressLine1Txt
  city: Return/ReturnHeader/Filer/USAddress/CityNm
  state: Return/ReturnHeader/Filer/USAddress/StateAbbreviationCd
  zip: Return/ReturnHeader/Filer/USAddress/ZIPCd
```

### Example Triggers

- Clearlane artifact schema update
- Scheduled artifact rebuild

### Concrete Outputs

| Artifact | Purpose |
|----------|---------|
| `artifact_<name>.json` | Populated artifact |
| `artifact_mapping_report.md` | Field mapping documentation |

### Next Experiments

- Multiple artifact projections from same core data
- Artifact completeness scoring

**Promotion Note:** Not yet promoted. Core integration pattern for 990 → Clearlane.

---

## Pulse 13: Run-Scoped Directories Pattern

---
pulse_number: 13
temporal_hash: "#021020262420"
thread_title: "990 Integration Run 5 — State Is the Filesystem"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - pipeline_pattern
  - automation_candidate

priority: high
impact: foundational

topics:
  - 990_spine
  - run_isolation
  - filesystem_state
  - reproducibility
  - garbage_collection

related_pulses:
  - "#021020262415"
  - "#021020262410"
  - "#021020262405"
  - "#021020262400"
fills_gaps:
  - "MISSING_VALIDATION:run_isolation"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T24:20:00Z"
promoted_to: []
---

### Core Idea

Each run writes to a **fresh, isolated directory**; no run reads outputs from another run.

### Runnable Layout

```
runs/<run_id>/
  inputs/
  outputs/
  validations/
  manifest.json
```

### Join Keys

Not applicable (execution control pattern).

### Validation Gates

- Output directory must not exist before run
- All declared artifacts must exist at end
- Manifest checksum verified

### Manifest Schema

```json
{
  "run_id": "2026-02-10T14-30-00Z",
  "scope": {
    "tax_years": [2023, 2024],
    "ein_count": 1234
  },
  "inputs": ["index_2024.csv", "eo_bmf_2024.csv"],
  "outputs": ["joined_rows.csv", "artifacts/*.json"],
  "validations": ["schema_report.json", "join_loss.json"],
  "status": "success",
  "duration_seconds": 847
}
```

### Example Triggers

- Any scheduled or event-driven run

### Concrete Outputs

| Artifact | Purpose |
|----------|---------|
| Run-isolated datasets | All inputs/outputs in run scope |
| `manifest.json` | Run metadata and results |

### Next Experiments

- Garbage collection by retention policy
- Promotion of selected runs to stable paths
- Run comparison tooling

**Promotion Note:** Not yet promoted. Enables reproducible, isolated execution.

---

## Pulse 14: Event Payload as Data Pattern

---
pulse_number: 14
temporal_hash: "#021020262425"
thread_title: "990 Integration Run 6 — Events Are Inputs"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - pipeline_pattern
  - event_driven

priority: high
impact: foundational

topics:
  - 990_spine
  - event_driven
  - payload_schema
  - trigger_data
  - replay_capability

related_pulses:
  - "#021020262420"
  - "#021020262415"
  - "#021020262410"
fills_gaps:
  - "MISSING_VALIDATION:event_handling"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T24:25:00Z"
promoted_to: []
---

### Core Idea

Event triggers supply a **payload file** that is treated like any other input dataset.

### Runnable Pipeline

```
receive event payload
 → validate payload schema
 → process as scope definition
```

### Example Payload

```json
{
  "ein": "123456789",
  "tax_year": 2024,
  "reason": "new_filing",
  "source": "irs_index_update",
  "timestamp": "2026-02-10T14:30:00Z"
}
```

### Validation Gates

- Payload schema validation
- Required fields present
- Payload archived with outputs

### Example Triggers

- New filing detected
- Clearlane artifact change event
- EO BMF status change

### Concrete Outputs

| Artifact | Purpose |
|----------|---------|
| `event_payload.json` | Frozen trigger data |
| Scoped joined datasets | Based on payload scope |

### Event Types

| Event | Payload | Action |
|-------|---------|--------|
| `new_filing` | EIN, tax_year, object_id | Process single filing |
| `batch_update` | tax_year, ein_list | Process batch |
| `schema_change` | artifact_type, version | Rebuild affected artifacts |
| `index_refresh` | checksum, row_count | Full scope revalidation |

### Next Experiments

- Event replay for deterministic backfills
- Multiple payloads batched into single run
- Event sourcing for full audit trail

**Promotion Note:** Not yet promoted. Enables event-driven automation.

---

## Pulse 15: Value-Blind Core Joins Pattern

---
pulse_number: 15
temporal_hash: "#021020262430"
thread_title: "990 Integration Run 7 — Numbers Come Later"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - pipeline_pattern
  - validation_candidate

priority: high
impact: foundational

topics:
  - 990_spine
  - identifier_joins
  - structural_validation
  - metric_separation
  - join_maps

related_pulses:
  - "#021020262425"
  - "#021020262420"
  - "#021020262415"
  - "#021020262410"
fills_gaps:
  - "MISSING_VALIDATION:structural_integrity"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T24:30:00Z"
promoted_to: []
---

### Core Idea

Perform joins using **identifiers only**, without loading or validating numeric values.

### Runnable Pipeline

```
extract identifiers
 → join identifiers
 → emit join map
```

### Join Keys

| Key | Purpose |
|-----|---------|
| EIN | Canonical org identifier |
| Tax Year | Temporal alignment |

### Validation Gates

- No numeric fields allowed in core join
- Identifier uniqueness enforced
- Join map completeness verified

### Join Map Schema

```csv
ein,tax_year,index_present,filing_present,eo_bmf_present,state_payee_present
123456789,2024,true,true,true,false
987654321,2024,true,false,true,true
```

### Example Triggers

- Scheduled structural integrity check
- Pre-metric validation job

### Concrete Outputs

| Artifact | Purpose |
|----------|---------|
| `join_map.csv` | Identifier presence matrix |
| `identifier_coverage.json` | Coverage statistics |

### Coverage Metrics

```json
{
  "total_eins": 1234,
  "index_coverage": 1.0,
  "filing_coverage": 0.87,
  "eo_bmf_coverage": 0.95,
  "state_payee_coverage": 0.42,
  "full_coverage": 0.38
}
```

### Next Experiments

- Using join maps to gate metric computation
- Identifier-only monitoring dashboards
- Gap detection from coverage patterns

**Promotion Note:** Not yet promoted. Separates structural validation from value validation.

---

## Pulse 16: Minimal Tooling Contract & Run Guarantees

---
pulse_number: 16
temporal_hash: "#021020262435"
thread_title: "990 Integration — Tooling Contract"
version: 1.0
status: raw
type: cognitive_dump
domain: arkansas_public_finance
operation: nami_clearlane

classification:
  - schema_candidate
  - fis_foundation
  - operational_guide
  - automation_candidate

priority: high
impact: foundational

topics:
  - 990_spine
  - tooling_contract
  - run_guarantees
  - artifact_requirements
  - simplicity

related_pulses:
  - "#021020262430"
  - "#021020262425"
  - "#021020262420"
  - "#021020262415"
  - "#021020262410"
  - "#021020262405"
  - "#021020262400"
fills_gaps:
  - "MISSING_VALIDATION:operational_contract"
strengthens:
  - "key_registry.yaml"

created_at: "2026-02-10T24:35:00Z"
promoted_to: []
---

### Minimal Tooling Contract

| Tool | Purpose |
|------|---------|
| POSIX shell | Orchestration |
| Python (stdlib; pandas optional) | Processing |
| CSV / Parquet / JSON | Data formats |
| Local filesystem only | State storage |

**No services, queues, databases, or hidden state.**

### Guaranteed Artifacts Per Run

Every run produces:

| Artifact Type | Purpose |
|---------------|---------|
| At least one **joined or artifact dataset** | Primary output |
| At least one **validation or accounting artifact** | Quality evidence |
| One **manifest or context file** | Run metadata |
| One **diagnostic (loss, schema, or event) artifact** | Failure analysis |

**Missing artifacts indicate failure.**

### Run Success Criteria

```python
def run_succeeded(run_dir):
    required = [
        "outputs/*.csv" or "outputs/*.json",  # data
        "validations/*.json",                  # quality
        "manifest.json",                       # metadata
        "diagnostics/*.json"                   # analysis
    ]
    return all(glob_matches(run_dir, pattern) for pattern in required)
```

### Principles

The most reliable integrations emerge when:

1. **Indexes and schemas drive scope** — not ad-hoc queries
2. **Joins are loss-accounted, not optimistic** — every row classified
3. **Artifacts define outputs, not ad-hoc tables** — Clearlane shapes first
4. **Runs are isolated and replayable** — state is filesystem
5. **Events are frozen as data** — triggers are inputs
6. **Structure is validated before values** — identifiers first

### Anti-Patterns

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| Implicit scope | Can't reproduce runs |
| Silent drops | Can't audit losses |
| Ad-hoc outputs | Can't validate shape |
| Shared state | Can't isolate runs |
| Ephemeral triggers | Can't replay events |
| Eager value loading | Can't separate concerns |

**Promotion Note:** Not yet promoted. Operational contract for all 990 integration work.

---

## Summary: Integration Patterns Arc

| Pulse | Pattern | Key Capability |
|-------|---------|----------------|
| 9 | Index-Led Orchestration | Scope control via index |
| 10 | Schema-Pinned Inputs | Fail-fast on drift |
| 11 | Join-Loss Accounting | Loss as first-class output |
| 12 | Artifact-First Outputs | Clearlane shapes define output |
| 13 | Run-Scoped Directories | Isolated, reproducible runs |
| 14 | Event Payload as Data | Triggers are inputs |
| 15 | Value-Blind Core Joins | Structure before values |
| 16 | Tooling Contract | Operational guarantees |

**Net Result:** Small, scheduled scripts harden into deterministic, auditable automation without increasing system complexity.
