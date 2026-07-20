from pprint import pprint
from app.db.database import Base, engine

from app.graph.agent import graph
from app.graph.state import GraphState
from app.db.database import SessionLocal
from app.models.interaction import Interaction

Base.metadata.create_all(bind=engine)


def run_test(message: str):
    state: GraphState = {
        "hcp_id": 1,
        "interaction_id": None,
        "user_input": message,
        "intent": "",
        "summary": "",
        "extracted_data": {},
        "sentiment": "",
        "follow_up_actions": [],
        "tool_result": {},
        "response": "",
    }

    db = SessionLocal()

    result = graph.invoke(
        state,
        config={"configurable": {"db": db}}
    )

    print("\n========== FINAL STATE ==========\n")
    pprint(result)

    print("\n========== RESPONSE ==========\n")
    print(result["response"])


if __name__ == "__main__":

    run_test(
        """
        Today I met Dr. Smith.

        We discussed our new diabetes medicine.

        Doctor liked the clinical trial data.

        I shared product brochure.

        Doctor requested another meeting after two weeks.

        He seemed positive.
        """
    )