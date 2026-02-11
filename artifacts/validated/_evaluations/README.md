# Evaluations

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10

---

## Purpose

This folder stores quality evaluation results from artifact validation runs. Evaluations assess accuracy, completeness, and linkage correctness.

## Types of Evaluations

- **Schema Compliance** - Field presence and type validation
- **Linkage Integrity** - Reference target existence
- **Citation Accuracy** - Source URL validity
- **Content Quality** - LLM-assessed relevance and accuracy

## Output Format

Evaluation results are typically JSON with:
```json
{
  "evaluation_id": "EVAL-2026-02-10-001",
  "run_at": "2026-02-10T12:00:00Z",
  "scope": "full_repository",
  "results": {
    "passed": 850,
    "failed": 87,
    "warnings": 45
  },
  "details": [...]
}
```

## Usage

Evaluations are triggered by:
- CI/CD pipeline runs
- Manual validation scripts
- Pre-promotion checks
