from datetime import datetime

from app.ai.llm_service import extract_interaction_details
from app.graph.state import GraphState
from app.graph.tool.extract_util import normalize_date, normalize_time, normalize_list_field, LIST_FIELDS


def extract_tool(state: GraphState) -> GraphState:
    """
    Extract structured CRM information from the user's interaction.
    """

    user_input = state.get("user_input", "").strip()

    if not user_input:
        state["extracted_data"] = {}
        return state

    try:
        extracted_data: dict = extract_interaction_details(user_input)

        extracted_data["interaction_date"] = normalize_date(extracted_data.get("interaction_date")) or datetime.now().date()
        extracted_data["interaction_time"] = normalize_time(extracted_data.get("interaction_time"))

        for field in LIST_FIELDS:
            extracted_data[field] = normalize_list_field(extracted_data.get(field))

        # try:
        #     extracted_data["hcp_id"] = state["selected_hcp_id"]
        #     extracted_data["notes"] = user_input
        #     state["extracted_data"] = InteractionCreate(**extracted_data).model_dump()
        # except ValidationError as e:
        #     state["extracted_data"] = {}
        #     print(f"Schema validation failed: {e}\nRaw data: {extracted_data!r}")
        #     raise

        state["extracted_data"] = extracted_data

        # Convenience fields for later nodes
        # state["sentiment"] = extracted_data.get("sentiment", "")
        # state["follow_up_actions"] = extracted_data.get(
        #     "follow_up_actions", []
        # )
        print("Returning from extract_tool")
    except Exception as e:
        state["extracted_data"] = {}
        state["response"] = f"Failed to extract interaction details: {str(e)}"
        print("Failed to Extract data")

    return state