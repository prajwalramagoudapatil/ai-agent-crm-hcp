from sqlalchemy.orm import Session

from app.graph.state import GraphState
from app.services import interaction_service



def update_interaction_tool(
    db: Session,
    interaction_id: int,
    state: GraphState,
) -> dict:
    """
    Update an existing interaction using only the fields
    extracted by the LLM.
    """

    if interaction_id is None:
        raise ValueError("interaction_id is required for editing.")

    update_data = state["extracted_data"]


    updated_interaction = interaction_service.update_interaction(
        db=db,
        interaction_id=interaction_id,
        interaction_data=update_data,
    )

    state["interaction_id"] = updated_interaction.id

    return {
        "success": True,
        "message": "Interaction updated successfully.",
        "interaction": updated_interaction,
    }