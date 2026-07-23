from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    Date,
    Time,
    DateTime,
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Relationship with HCP
    # hcp_id = Column(Integer, ForeignKey("hcps.id"), nullable=False)
    hcp_id = Column(Integer)

    # hcp_name = Column(Text)

    # Meeting / Call / Email / Conference
    interaction_type = Column(String(50), nullable=False)

    # Actual meeting date & time
    interaction_date = Column(Date, nullable=True)
    interaction_time = Column(Time, nullable=True)

    # Optional attendees
    attendees = Column(Text, nullable=True)

    # Raw notes entered by user/chat transcript
    notes = Column(Text, nullable=False)

    # Topics discussed during interaction
    topics_discussed = Column(Text, nullable=True)

    # ---------- AI Generated Fields ----------
    summary = Column(Text, nullable=True)

    sentiment = Column(String(20), nullable=True)

    outcomes = Column(Text, nullable=True)

    follow_up_actions = Column(Text, nullable=True)

    materials_shared = Column(Text, nullable=True)

    samples_distributed = Column(Text, nullable=True)
    # -----------------------------------------

    created_at = Column(DateTime, default=datetime.now)

    # hcp = relationship(
    #     "HCP",
    #     back_populates="interactions",
    # )