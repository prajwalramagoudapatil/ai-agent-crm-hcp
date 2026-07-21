from datetime import date, time
from typing import Optional, List
from pydantic import BaseModel, Field


class InteractionCreate(BaseModel):
    hcp_id: int

    interaction_type: str

    interaction_date: date = Field(default_factory=date.today)
    interaction_time: Optional[time]

    notes: Optional[str]

    attendees: List[str] = Field(default_factory=list())

    topics_discussed: List[str] = Field(default_factory=[""])

    summary: Optional[str] = None

    materials_shared: List[str] = Field(default_factory=[""])
    samples_distributed: List[str] = Field(default_factory=[""])

    sentiment: Optional[str] = None

    outcomes: Optional[str] = None

    follow_up_actions: List[str] = Field(default_factory=[''])