from tools.collect_facts import (
    collect_facts,
)
from tools.reason_engine import (
    reason,
)
from tools.summary_generator import (
    generate_summary,
)
from tools.insight_generator import (
    generate_insight,
)

def render(node_id):

    facts = collect_facts(node_id)
   
    reasoning = reason(facts)
    
    summary = generate_summary(facts)

    insight = generate_insight(reasoning)

    return {
        "facts": facts,
        "reasoning": reasoning,
        "summary": summary,
        "insight": insight,
    }