from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState
from app.graph.nodes import (
    extract_node,
    summarize_node,
    log_interaction_node,
    response_node,
    intent_node,
    resolve_hcp_node
)

def route_intent(state: GraphState) -> str:
    print(f" Returning detected intent to route: {state['intent']}")
    return state["intent"]


builder = StateGraph(GraphState)

builder.add_node("extract", extract_node)
builder.add_node("resolve_hcp", resolve_hcp_node)
builder.add_node("summarize", summarize_node)
builder.add_node("log_interaction", log_interaction_node)
builder.add_node("response", response_node)
builder.add_node("intent", intent_node)


# Graph EDGES:
builder.add_edge(START, "intent")

builder.add_conditional_edges(
    "intent",
    route_intent,
    {
        "LOG_INTERACTION": "extract",
        "EDIT_INTERACTION": "response",
        "GET_INTERACTION": "response",
        "UNKNOWN": "response",
    },
)

builder.add_edge("extract", "resolve_hcp")
builder.add_edge("resolve_hcp", "summarize")
builder.add_edge("summarize", "log_interaction")
builder.add_edge("log_interaction", "response")
builder.add_edge("response", END)

graph = builder.compile()