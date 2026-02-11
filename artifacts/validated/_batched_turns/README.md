# Batched Turns

**Part of:** Operation NAMI Clearlane / VECTOR 1  
**Last Updated:** 2026-02-10

---

## Purpose

This folder stores batched conversation turns from LLM sessions that generated artifacts. Each turn captures the prompt and response for audit trail purposes.

## Structure

Turn files are organized by session:
```
_batched_turns/
├── session_20260210_001/
│   ├── turn_001.json
│   ├── turn_002.json
│   └── manifest.json
└── session_20260210_002/
    └── ...
```

## Turn Format

```json
{
  "turn_number": 1,
  "timestamp": "2026-02-10T12:00:00Z",
  "model": "claude-opus-4",
  "prompt_tokens": 5000,
  "response_tokens": 2000,
  "artifacts_generated": ["AUTH-AR-ACA-20-77-107", "MF-AR-MEDICAID-001"],
  "prompt_hash": "abc123...",
  "response_hash": "def456..."
}
```

## Usage

Batched turns support:
- Reproducibility of artifact generation
- Cost tracking for LLM usage
- Quality analysis of prompt effectiveness
- Audit trail for compliance
