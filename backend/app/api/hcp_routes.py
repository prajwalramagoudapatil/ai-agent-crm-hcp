from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services import hcp_service
from app.models.hcp import HCP

router = APIRouter(
    prefix="/hcps",
    tags=["HCP"]
)

@router.get("/")
def get_all_hcps(
    db: Session = Depends(get_db)
):
    """
    Retrieve all HCPs.
    """
    return hcp_service.get_all_hcps(db)


@router.get("/{hcp_id}")
def get_hcp_by_id(
    hcp_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve an HCP by ID.
    """

    hcp = hcp_service.get_hcp_by_id(db, hcp_id)

    if hcp is None:
        raise HTTPException(
            status_code=404,
            detail="HCP not found"
        )

    return hcp


@router.post("/")
def create_hcp(
    hcp_data: dict,
    db: Session = Depends(get_db)
):
    """
    Create a new HCP.
    """
    hcp = HCP(**hcp_data)

    return hcp_service.create_hcp(db, hcp)


@router.put("/{hcp_id}")
def update_hcp(
    hcp_id: int,
    hcp_data: dict,
    db: Session = Depends(get_db)
):
    """
    Update an existing HCP.
    """

    updated_hcp = hcp_service.update_hcp(
        db=db,
        hcp_id=hcp_id,
        hcp_data=hcp_data
    )

    if updated_hcp is None:
        raise HTTPException(
            status_code=404,
            detail="HCP not found"
        )

    return updated_hcp


@router.delete("/{hcp_id}")
def delete_hcp(
    hcp_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an HCP.
    """

    deleted = hcp_service.delete_hcp(db, hcp_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="HCP not found"
        )

    return {
        "message": "HCP deleted successfully"
    }