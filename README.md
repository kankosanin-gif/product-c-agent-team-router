# Product C — Agent Team Router

A lightweight policy router to decide:
- Run as **SubAgent** (single delegate)
- Escalate to **Agent Team** (multi-agent collaboration)

## Decision Heuristic
Escalate to Agent Team only when one or more is true:
1. ambiguity remains after one SubAgent cycle
2. cross-functional risk is high
3. decision impacts release/security/compliance gates

Otherwise keep SubAgent mode to reduce context and token overhead.

## Output Contract
Router output must include:
- selected mode
- reason codes
- risk level
- next owner

## Governance templates
- Gate Decision Log: \n- Escalation SLA: \n- Proof-of-Work template: \n
## Operational records
- Work-item log: `records/work-item-log.md`
- Weekly review: `reviews/WEEKLY_REVIEW.md`

## Symphony runbook
- Work-item / Proof-of-Work flow: `orchestration/SYMPHONY_RUNBOOK.md`

## KPI tracking
- KPI snapshot: `metrics/KPI_SNAPSHOT.md`
- Blocker aging metric: `metrics/BLOCKER_AGING.md`
