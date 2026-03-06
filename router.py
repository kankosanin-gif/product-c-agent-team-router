#!/usr/bin/env python3
"""Simple policy router for SubAgent vs Agent Team mode."""

from dataclasses import dataclass


@dataclass
class TaskSignal:
    ambiguity_after_first_cycle: bool = False
    cross_functional_risk_high: bool = False
    gate_impact: bool = False


def route(signal: TaskSignal):
    reasons = []
    if signal.ambiguity_after_first_cycle:
        reasons.append("ambiguity_after_first_cycle")
    if signal.cross_functional_risk_high:
        reasons.append("cross_functional_risk_high")
    if signal.gate_impact:
        reasons.append("gate_impact")

    if reasons:
        return {
            "mode": "agent_team",
            "reasons": reasons,
            "risk": "high",
            "next_owner": "Manager + Kuro",
        }

    return {
        "mode": "subagent",
        "reasons": ["default_minimal_mode"],
        "risk": "low",
        "next_owner": "Manager",
    }


if __name__ == "__main__":
    # demo
    print(route(TaskSignal()))
