from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from typing import List
from pprint import pprint
from app.models.interaction import Interaction
from app.schemas.interaction_schema import InteractionCreate



def create_interaction(
    db: Session,
    interaction: InteractionCreate
) -> Interaction:
    """
    Create a new interaction.
    """
    pprint(f" *************** \n ******************* \n Creating the interaction record")
    try:
        db_interaction = Interaction(**interaction.model_dump())
        db.add(db_interaction)
        db.commit()
        db.refresh(db_interaction)
        print(f"  >><< Interaction created with id: {db_interaction.id}")

        return db_interaction
    except SQLAlchemyError:
        db.rollback()
        raise


def get_all_interactions(
    db: Session
) -> List[Interaction]:
    """
    Retrieve all interactions.
    """

    return db.query(Interaction).all()


def get_interaction_by_id(
    db: Session,
    interaction_id: int
) -> Interaction | None:
    """
    Retrieve an interaction by its ID.
    """

    return (
        db.get(Interaction, interaction_id)
    )


def get_interactions_by_hcp_id(
    db: Session,
    hcp_id: int
) -> List[Interaction]:
    """
    Retrieve all interactions for a specific HCP.
    """

    return (
        db.query(Interaction).filter(Interaction.hcp_id == hcp_id).all()
    )


def update_interaction(
    db: Session,
    interaction: Interaction
) -> Interaction:
    """
    Update an existing interaction.
    """

    db.commit()
    db.refresh(interaction)

    return interaction


def delete_interaction(
    db: Session,
    interaction: Interaction
) -> None:
    """
    Delete an interaction.
    """

    db.delete(interaction)
    db.commit()