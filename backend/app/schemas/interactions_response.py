from pydantic import BaseModel
from datetime import date, time

class InteractionResponse(BaseModel):
    id: int
    hcp_id: int
    hcp_name: str

    interaction_type: str
    interaction_date: date
    interaction_time: time

    attendees: list[str]
    topics_discussed: list[str]
    materials_shared: list[str]
    samples_distributed: list[str]

    sentiment: str
    outcomes: str
    follow_up_actions: list[str]

    class Config:
        from_attributes = True