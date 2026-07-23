# backend/app/api/agent_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.agent_schema import ChatRequest, ChatResponse
from app.graph.agent import graph
from app.db.database import get_db

router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"]
)

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """
    Entry point for conversational interaction logging.
    """
    print("Received request on /chat")
    try:
        print(request)
        result = graph.invoke(
            {
                "user_input": request.message,
                "selected_hcp_id": request.hcp_id,
                "interaction_id": request.interaction_id
            },
            config={"configurable": {"db": db}}
        )

        return ChatResponse(
            response=result.get("response", "NO_RESPONSE_GENERATED"),
            extracted_data=result.get("extracted_data", {}),
            summary=result.get("summary"),
            interaction_id=result.get("interaction_id", "NO_ID_FOUND"),
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )