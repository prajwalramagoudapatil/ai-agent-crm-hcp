from sqlalchemy.orm import Session

from app.graph.state import GraphState
from app.schemas.interaction_schema import InteractionCreate
from app.services.interaction_service import create_interaction


def log_interaction_tool(
    state: GraphState,
    db: Session,
) -> GraphState:
    """
    Persist a new interaction into the database.
    """


    extracted = state.get("extracted_data", {})

    if not extracted:
        state["tool_result"] = {
            "success": False,
            "message": "No extracted interaction data found.",
        }
        return state
    print("Narayana Lakshmi")
    try:
        print("Narayana Lakshmi")

        interaction = InteractionCreate(


            hcp_id=state["resolved_hcp_id"],

            interaction_type=extracted["interaction_type"],

            interaction_date=extracted["interaction_date"],
            interaction_time=extracted["interaction_time"],

            attendees=extracted.get("attendees"),

            notes=state["user_input"],

            topics_discussed=extracted.get("topics_discussed"),

            summary=state.get("summary", ""),

            materials_shared=extracted.get("materials_shared"),
            samples_distributed=extracted.get("samples_distributed"),

            sentiment=extracted.get("sentiment"),

            outcomes=extracted.get("outcomes"),

            follow_up_actions=extracted.get("follow_up_actions"),
        )

        print(" Ram Sita Hanuman. ")

        saved_interaction = create_interaction(
            db=db,
            interaction=interaction,
        )

        state["tool_result"] = {
            "success": True,
            "interaction_id": saved_interaction.id,
            "message": "Interaction logged successfully.",
        }
        state["interaction_id"] = saved_interaction.id

        print(" ## tool result:", state["tool_result"])

    except Exception as e:
        state["tool_result"] = {
            "success": False,
            "message": str(e),
        }

        print("Narayan: error:", e)

    print("  ### returning state from log_interaction_tool")
    return state