from sqlalchemy.orm import Session

from app.models.hcp import HCP
from app.repositories import hcp_repository


from sqlalchemy.exc import SQLAlchemyError

def create_hcp(
    db: Session,
    hcp: HCP
) -> HCP:
    try:
        return hcp_repository.create_hcp(db, hcp)
    except SQLAlchemyError:
        db.rollback()
        raise


def get_all_hcps(
    db: Session
) -> list[HCP]:
    return hcp_repository.get_all_hcps(db)


def get_hcp_by_id(
    db: Session,
    hcp_id: int
) -> HCP | None:
    """
    Retrieve an HCP by its ID.
    """

    return hcp_repository.get_hcp_by_id(db, hcp_id)


def update_hcp(
    db: Session,
    hcp_id: int,
    hcp_data: dict
) -> HCP | None:

    hcp = hcp_repository.get_hcp_by_id(db, hcp_id)

    if hcp is None:
        return None

    for key, value in hcp_data.items():
        setattr(hcp, key, value)

    return hcp_repository.update_hcp(
        db=db,
        hcp=hcp
    )


def delete_hcp(
    db: Session,
    hcp_id: int
) -> bool:

    hcp = hcp_repository.get_hcp_by_id(db, hcp_id)

    if hcp is None:
        return False

    hcp_repository.delete_hcp(db, hcp)

    return True