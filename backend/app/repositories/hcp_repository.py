from typing import cast

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.models import HCP
from app.models.hcp import HCP


def create_hcp(db: Session, hcp: HCP) -> HCP:
    db.add(hcp)
    db.commit()
    db.refresh(hcp)
    return hcp

def get_all_hcps(db: Session) -> list[HCP]:
    return cast(list[HCP], db.query(HCP).all())

def get_hcp_by_id(db: Session, hcp_id: int) -> HCP | None:
    return db.get(HCP, hcp_id)

def update_hcp(db: Session, hcp: HCP) -> HCP:
    try:
        db.commit()
        db.refresh(hcp)
        return hcp

    except SQLAlchemyError:
        db.rollback()
        raise

def delete_hcp(db: Session, hcp: HCP) -> None:
    db.delete(hcp)
    db.commit()