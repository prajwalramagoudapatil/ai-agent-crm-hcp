import json
from datetime import datetime
from app.graph.state import GraphState

from app.ai.llm_service import extract_edit_details
from app.repositories.interaction_repository import get_interaction_by_id
from app.schemas.interaction_schema import InteractionCreate
from app.graph.tool.extract_util import normalize_date, normalize_time, normalize_list_field, LIST_FIELDS

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
            print(f"Received interaction. interaction_id: {interaction.id}")
            if interaction is not None:

                interaction_dict = {
                    "id": interaction.id,
                    "hcp_id": interaction.hcp_id,
                    "interaction_type": interaction.interaction_type,
                    "interaction_date": str(interaction.interaction_date),
                    "interaction_time": str(interaction.interaction_time),
                    "attendees": interaction.attendees,
                    "topics_discussed": interaction.topics_discussed,
                    "notes": interaction.notes,
                    "summary": interaction.summary,
                    "sentiment": interaction.sentiment,
                    "outcomes": interaction.outcomes,
                    "follow_up_actions": interaction.follow_up_actions,
                    "materials_shared": interaction.materials_shared,
                    "samples_distributed": interaction.samples_distributed,
                }

                print("  #### Got interaction dict")
                interaction_json = json.dumps(interaction_dict, indent=2)


                # prompt += f"Current Interaction: {interaction_json} "
    except Exception as e:
        print(F"Error in getting interaction JSON")
        raise


    prompt += (
        "User Request:"
        f"{user_input}"
        "Return only the fields that need to be updated."
    )

    print("Calling llm service to extract edit data")

    extracted_data = extract_edit_details(prompt)

    extracted_data["interaction_date"] = normalize_date(extracted_data.get("interaction_date")) or datetime.now().date()
    extracted_data["interaction_time"] = normalize_time(extracted_data.get("interaction_time"))

    for field in LIST_FIELDS:
        extracted_data[field] = normalize_list_field(extracted_data.get(field))

    # Remove empty values returned by the LLM
    update_data = {
        key: value
        for key, value in extracted_data.items()
        if value is not None and value != "" and value != []
    }

    print("Got updated data: ", update_data)

    state["extracted_data"] = update_data
    state["hcp_conflict"] = False

    # Nothing to update
    if not update_data:
        return {
            "success": False,
            "message": "No valid fields found to update.",
            "interaction": None,
        }

    return {
        "success": True,
        "message": f"Updating {update_data}",
        "interaction": interaction_id,
    }