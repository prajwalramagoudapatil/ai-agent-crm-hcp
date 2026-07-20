from app.ai.llm_service import extract_interaction_details
from app.graph.state import GraphState


def extract_tool(state: GraphState) -> GraphState:
    """
    Extract structured CRM information from the user's interaction.
    """

    user_input = state.get("user_input", "").strip()

    if not user_input:
        state["extracted_data"] = {}
        return state
    print("Ram Sita Hanuman 18 18 18 18 18 18 18 108 1008 100008 \n \n ")
    try:
        extracted_data = extract_interaction_details(user_input)

        state["extracted_data"] = extracted_data

        # Convenience fields for later nodes
        state["sentiment"] = extracted_data.get("sentiment", "")
        state["follow_up_actions"] = extracted_data.get(
            "follow_up_actions", []
        )
        print("Returning from extract_tool")
    except Exception as e:
        state["extracted_data"] = {}
        state["response"] = f"Failed to extract interaction details: {str(e)}"
        print("Failed to Extract data")

    return state