# Agent Run Logs

Track completed agent runs, batches ingested, and results.

## Log Format

Each run gets a log file: `YYYY-MM-DD_HH-MM_<INSTRUCTION_SET>.md`

```markdown
# Run Log: <instruction set name>
- **Started:** 2026-02-06 08:00
- **Completed:** 2026-02-06 09:30
- **Agent:** ChatGPT/Claude/Codex
- **Mode:** Deep Research / Agent Mode / Schema Cycling

## Input
- Instruction file: `AGENT_RUN_XXX.md`
- Seeds/targets: (list what was processed)

## Output
- Batch file: `batch_xxx.json`
- Artifacts created: X
- Categories: X MF, X AUTH, X EVID, X FV

## Notes
(any issues, quality observations, follow-ups needed)

## Next Steps
(what should come after this run)
```

## Quick Log Template

Copy this for new runs:

```markdown
# Run Log: 
- **Started:** 
- **Completed:** 
- **Agent:** 
- **Mode:** 

## Input
- Instruction file: 
- Seeds/targets: 

## Output
- Batch file: 
- Artifacts created: 
- Categories: 

## Notes

## Next Steps
```
