# Canonical Schema Compatibility (Form 990)

Form 990 data is disclosure-grade evidence, not a new data class. It fits inside the existing structure.

1️⃣ authority_reference

Used when the 990 asserts authority, eligibility, or compliance.

Sources

Schedule A (public charity qualification)

Schedule I (federal pass-through programs)

Part I line 3 (mission-qualified activity)

What it proves

Eligibility status

Federal program participation

Statutory or regulatory standing

2️⃣ money_flow

Used when dollars are reported as routed, granted, or controlled.

Sources

Part IX (functional expenses)

Schedule I (grants and assistance)

Schedule R (related entity transfers)

What it proves

Directionality of funds

Program vs admin routing

Pass-through relationships

3️⃣ evidence_item

Used when the 990 supports a factual claim.

Sources

Part III (program service accomplishments)

Part VI (governance disclosures)

Schedule O (narrative explanations)

What it proves

Program existence

Operational scope

Governance posture

4️⃣ field_validation

Used when the 990 corroborates or falsifies external claims.

Sources

Part VII (officers / directors)

Schedule L (interested persons)

Multi-year comparisons (trend consistency)

What it proves

Independence

Conflict exposure

Stability or volatility over time

🔒 Why No New Schema Is Needed

Form 990 data is:

Historical

Self-reported

Lagged

Legally constrained

That makes it perfect evidence, but never primary authority.

Your schema already encodes that distinction.

🧠 Implementation Rule (Important)

Every 990-derived artifact should carry:

source_class: irs_form_990
temporal_role: historical_baseline
confidence_level: disclosed_not_audited

This prevents authority inflation while preserving analytical value.

🎯 Final Answer

✔ Same schemas
✔ Same join keys
✔ Same validation logic
✔ No exceptions

Form 990s plug directly into Clearlane as evidence-grade artifacts, not a parallel system.
