from tools.collect_facts import (
    collect_facts,
)

from tools.reason_engine import (
    reason,
)

from tools.inference_engine import (
    infer,
)

from tools.impact_analysis import (
    analyze,
)

from tools.decision_engine import (
    decide,
)

from tools.action_planner import (
    plan,
)


def run(node_id):

    facts = collect_facts(node_id)

    reasoning = reason(facts)

    knowledge = infer(
        facts,
        reasoning,
    )

    impact = analyze(
        knowledge,
    )

    decision = decide(
        impact,
    )

    action = plan(
        decision,
    )

    return {
        "facts": facts,
        "reasoning": reasoning,
        "knowledge": knowledge,
        "impact": impact,
        "decision": decision,
        "action": action,
    }