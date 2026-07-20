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
    print(" Calling repository to create record \n ################## \n \n ******** ")
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

    interaction = interaction_repository.get_interaction_by_id(db ,interaction_id)

    if interaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interaction data not found"
        )

    for key, val in interaction_data.items():
        setattr(interaction, key, val)

    return interaction_repository.update_interaction(
        db=db,
        interaction=interaction
    )


def delete_interaction(
    db: Session,
    interaction_id: int
) -> bool:
    """
    Delete an interaction.
    """

    return interaction_repository.delete_interaction(
        db=db,
        interaction_id=interaction_id
    )