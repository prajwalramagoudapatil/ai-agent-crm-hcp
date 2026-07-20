# backend/app/graph/tools/summarize_tool.py

from app.ai.llm_service import generate_summary
from app.graph.state import GraphState


def summarize_tool(state: GraphState) -> GraphState:
    """
    Summarize the user's interaction into a concise CRM note.

    Reads:
        state["user_input"]

    Writes:
        state["summary"]
    """

    user_input = state.get("user_input", "").strip()

    if not user_input:
        state["summary"] = ""
        return state

    try:
        summary = generate_summary(user_input)
        state["summary"] = summary

    except Exception as e:
        state["summary"] = ""
        state["response"] = f"Failed to generate summary: {str(e)}"

    return state









"""
What this tool will do

Input: I met Dr. Smith today. We discussed Product X. He was happy with the efficacy results but wanted more liver safety data. I promised to send the latest clinical study.

    ↓

Calls: generate_summary()

    ↓

Output: Met with Dr. Smith to discuss Product X. The HCP responded positively, requested additional liver safety data, and will receive the latest clinical study.

    ↓

Updates GraphState: state["summary"] = summary

That's all.
"""


