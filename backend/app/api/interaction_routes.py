from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import Interaction
from app.services import interaction_service

router = APIRouter(
    prefix="/interactions",
    tags=["Interaction"]
)


@router.get("/")
def get_all_interactions(
    db: Session = Depends(get_db)
):
    """
    Retrieve all interactions.
    """

    return interaction_service.get_all_interactions(db)


@router.get("/{interaction_id}")
def get_interaction_by_id(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve an interaction by ID.
    """

    interaction = interaction_service.get_interaction_by_id(
        db,
        interaction_id
    )

    if interaction is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found"
        )

    return interaction


@router.post("/")
def create_interaction(
    interaction_data: dict,
    db: Session = Depends(get_db)
):
    """
    Create a new interaction.
    """
    interaction = Interaction(**interaction_data)

    return interaction_service.create_interaction(
        db,
        interaction
    )


@router.put("/{interaction_id}")
def update_interaction(
    interaction_id: int,
    interaction_data: dict,
    db: Session = Depends(get_db)
):
    """
    Update an interaction.
    """

    updated_interaction = interaction_service.update_interaction(
        db=db,
        interaction_id=interaction_id,
        interaction_data=interaction_data
    )

    if updated_interaction is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found"
        )

    return updated_interaction


@router.delete("/{interaction_id}")
def delete_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an interaction.
    """

    deleted = interaction_service.delete_interaction(
        db,
        interaction_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found"
        )

    return {
        "message": "Interaction deleted successfully"
    }