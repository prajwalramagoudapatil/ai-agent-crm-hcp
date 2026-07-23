from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.repositories import interaction_repository
from app.schemas.interaction_schema import InteractionCreate


def create_interaction(
    db: Session,
    interaction: InteractionCreate
) -> Interaction:
    """
    Create a new interaction.
    """
    print(" Calling repository to create record ")
    return interaction_repository.create_interaction(
        db=db,
        interaction=interaction
    )


def get_all_interactions(
    db: Session
) -> list[Interaction]:
    """
    Retrieve all interactions.
    """

    return interaction_repository.get_all_interactions(db)


def get_interaction_by_id(
    db: Session,
    interaction_id: int
) -> Interaction | None:
    """
    Retrieve an interaction by its ID.
    """

    return interaction_repository.get_interaction_by_id(
        db=db,
        interaction_id=interaction_id
    )


def update_interaction(
    db: Session,
    interaction_id: int,
    interaction_data: dict
) -> Interaction | None:
    """
    Update an existing interaction.
    """

    ALLOWED_UPDATE_FIELDS = {
        "interaction_type",
        "interaction_date",
        "interaction_time",
        "attendees",
        "topics_discussed",
        # "notes",
        "summary",
        "materials_shared",
        "samples_distributed",
        "sentiment",
        "outcomes",
        "follow_up_actions",
    }

    interaction = interaction_repository.get_interaction_by_id(db ,interaction_id)

    if interaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interaction data not found"
        )

    for key, val in interaction_data.items():
        if key in ALLOWED_UPDATE_FIELDS:
            setattr(interaction, key, val)

    return interaction_repository.update_interaction(
        db=db,
        interaction=interaction
    )


def delete_interaction(
    db: Session,
    interaction: Interaction
) :
    """
    Delete an interaction.
    """

    try:
        interaction_repository.delete_interaction(
            db=db,
            interaction=interaction
        )
    except Exception as e:
        print("Error in Deleting Interaction; interaction_id:", interaction.id, "Error:", e)
