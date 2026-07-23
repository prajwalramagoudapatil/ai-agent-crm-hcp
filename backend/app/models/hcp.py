from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


# Health Care Professional
class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String, nullable=False)
    email = Column(String)
    specialization = Column(String)

    hospital = Column(String)

    city = Column(String)
    
    interactions = relationship(
        "Interaction",
        back_populates="hcp",
        cascade="all, delete-orphan"
    )
