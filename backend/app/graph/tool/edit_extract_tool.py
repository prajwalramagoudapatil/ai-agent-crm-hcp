from app.graph.state import GraphState

from app.ai.llm_service import extract_edit_details
from app.repositories.interaction_repository import get_interaction_by_id
from app.schemas.interaction_schema import InteractionCreate

def edit_extract_tool(state: GraphState, db):
    user_input = state.get("user_input", "").strip()
    interaction_id = state.get("interaction_id", None)

    if not user_input:
        state["extracted_data"] = {}
        return state

    prompt = "You are editing an existing HCP interaction."

    try:
        if interaction_id is not None:
            interaction = get_interaction_by_id(db=db, interaction_id=interaction_id)

            if interaction is not None:
                interaction_schema = InteractionCreate.model_validate(interaction)
                interaction_json = interaction_schema.model_dump_json(indent=2)

                prompt += f"Current Interaction: {interaction_json} "
    except Exception as e:
        print(F"Error in getting interaction JSON")
        raise


    prompt += (
        "User Request:"
        f"{user_input}"
        "Return only the fields that need to be updated."
    )

    extracted_data = extract_edit_details(prompt)

    # Remove empty values returned by the LLM
    update_data = {
        key: value
        for key, value in extracted_data.items()
        if value is not None and value != ""
    }

    state["extracted_data"] = update_data

    # Nothing to update
    if not update_data:
        return {
            "success": False,
            "message": "No valid fields found to update.",
            "interaction": None,
        }