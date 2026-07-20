from typing import Optional, Dict, Any

from pydantic import BaseModel


class ChatRequest(BaseModel):
    hcp_id: int | None = None
    message: str
    interaction_id: int | None = None


class ChatResponse(BaseModel):
    response: str
    summary: Optional[str] = None
    interaction_id: Optional[int] = None
    extracted_data: Optional[Dict[str, Any]] = None