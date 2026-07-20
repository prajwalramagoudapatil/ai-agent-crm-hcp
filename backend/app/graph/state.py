# backend/app/graph/state.py

from typing import TypedDict, Optional, List, Dict, Any


class GraphState(TypedDict, total=False):
    """
    Shared state that flows through the LangGraph workflow.
    Each node can read and update these fields.
    """

    interaction_id: int | None

    # from frontend
    selected_hcp_id: int | None

    # extracted by LLM
    extracted_hcp_name: str | None

    selected_hcp_name: str | None

    # resolved after validation
    resolved_hcp_id: int | None

    hcp_conflict: bool

    # User's raw chat input
    user_input: str

    # Detected intent (log, edit, retrieve, etc.)
    intent: str

    # Interaction ID (used for edit operations)
    interaction_id: Optional[int]

    # AI-generated summary
    summary: str

    # Structured data extracted from the conversation
    extracted_data: Dict[str, Any]

    # Detected sentiment
    sentiment: str

    # AI-generated follow-up recommendations
    follow_up_actions: List[str]

    # Result returned by a tool (database response, etc.)
    tool_result: Dict[str, Any]

    # Final response sent back to the frontend
    response: str