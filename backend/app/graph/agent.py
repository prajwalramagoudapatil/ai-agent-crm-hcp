from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState
from app.graph.nodes import (
    extract_node,
    summarize_node,
    log_interaction_node,
    response_node,
    intent_node,
    resolve_hcp_node,
    edit_interaction_node,
    edit_extract_node
)

def route_intent(state: GraphState) -> str:
    print(f" Returning detected intent to route: {state['intent']}")
    return state["intent"]

def interaction_router(state: GraphState) -> str:
    """
    Decide whether to create a new interaction
    or edit an existing one.
    """

    if state.get("interaction_id") is not None:
        return "edit"

    return "log"

builder = StateGraph(GraphState)

builder.add_node("log_extract", extract_node)
builder.add_node("resolve_hcp", resolve_hcp_node)
builder.add_node("summarize", summarize_node)
builder.add_node("log_interaction", log_interaction_node)
builder.add_node("edit_interaction", edit_interaction_node)
builder.add_node("response", response_node)
builder.add_node("intent", intent_node)
builder.add_node("edit_extract", edit_extract_node)


# Graph EDGES:
# Decide whether this is a new interaction or an edit
builder.add_conditional_edges(
    START,
    interaction_router,
    {
        "log": "log_extract",
        "edit": "edit_extract",
    },
)

# ---------- Log Flow ----------

builder.add_edge("log_extract", "resolve_hcp")

builder.add_edge("resolve_hcp", "log_interaction")

builder.add_edge("log_interaction", "summarize")

# ---------- Edit Flow ----------

builder.add_edge("edit_extract", "edit_interaction")

builder.add_edge("edit_interaction", "summarize")

# ---------- Common Flow ----------

builder.add_edge("summarize", "response")

builder.add_edge("response", END)

graph = builder.compile()