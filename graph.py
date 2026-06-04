from nodes import research_node, decide_node, answer_node
from state import ResearchState
from langgraph.graph import StateGraph, END

def can_continue(state: ResearchState):
    if state["stop"] == True or state["iterations"] >= 2:
        return "answer_node"
    else:
        return "research_node"

graph = StateGraph(ResearchState)

graph.add_node("research_node", research_node)
graph.add_node("decide_node", decide_node)
graph.add_node("answer_node", answer_node)

graph.set_entry_point("research_node")

graph.add_edge("research_node", "decide_node")
graph.add_conditional_edges("decide_node", can_continue)
graph.add_edge("answer_node", END)

research_app = graph.compile()