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
