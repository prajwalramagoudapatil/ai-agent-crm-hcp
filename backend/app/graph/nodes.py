from app.graph.state import GraphState
from langchain_core.runnables import RunnableConfig
from sqlalchemy.orm import Session

from app.graph.tool.extract_tool import extract_tool
from app.graph.tool.summarize_tool import summarize_tool
from app.graph.tool.log_interaction_tool import log_interaction_tool
from app.ai.llm_service import detect_intent
from app.graph.tool.hcp_resolver_tool import resolve_hcp
from app.db.database import SessionLocal

def extract_node(state: GraphState) -> GraphState:
    extracted = extract_tool(state)

    state = extracted

    return state

def summarize_node(state: GraphState) -> GraphState:
    summary = summarize_tool(state)
    print("Ram Sita ....")
    state = summary

    return state

def log_interaction_node(state: GraphState, config: RunnableConfig) -> GraphState:

    db = config.get("configurable", {}).get("db")
    print("Krishna Rukmini ...")
    result = log_interaction_tool(
        state, db
    )
    print("Krishna Rukmini ...")
    state = result

    return state

def response_node(state: GraphState) -> GraphState:
    print("In response_node")
    try:
        interaction_id = state.get("tool_result", {}).get("interaction_id", "NO_DATA")
        tool_result_message = state.get("tool_result", {}).get("message", "Agent Failed")

        if state["hcp_conflict"]:
            result = state["tool_result"]

            state["response"] = (
                f"Interaction logged successfully for "
                f"{state['selected_hcp_name']}.\n\n"
                f"Note: Your message mentioned "
                f"'{state['extracted_hcp_name']}', "
                f"which doesn't match the selected HCP, "
                f"so the interaction was logged using the HCP selected in the form."
            )
        else:
            state["response"] = (
                f"Interaction ID: {interaction_id} message: {tool_result_message}."
            )
    except Exception as e:
        print(" Exception in response node. e:", e)
    finally:
        return state

#
def intent_node(state: GraphState) -> GraphState:
    """
    Detect the user's intent and store it in the graph state.
    """
    print("In intent_node")
    user_input = state["user_input"]

    intent = detect_intent(user_input)

    state["intent"] = intent
    state["tool_result"] = {
        "tool": "extract_intent",
        "status": "success",
        "message": f"Intent detected: {intent}",
    }
    return state

def resolve_hcp_node(state: GraphState):
    """
    Validates whether the selected HCP matches
    the HCP mentioned in the conversation.
    """
    db = SessionLocal()
    print('')
    try:
        result = resolve_hcp(
            db=db,
            selected_hcp_id=state.get("selected_hcp_id"),
            extracted_name=state["extracted_data"].get("doctor_name"),
        )
        print(" resolve_hcp result: ", result)
        state["tool_result"] = result
        state["resolved_hcp_id"] = state["selected_hcp_id"]
        if result["status"] == "conflict":
            state["hcp_conflict"] = True
            state["selected_hcp_name"] = result.get("selected_hcp_name", "NAME_NOT_RESOLVED")
            state["extracted_hcp_name"] = result.get("mentioned_hcp_name", "NO_NAME_EXTRACTED")
        else:
            state["hcp_conflict"] = False

        print("HCP Resolver:", result)

        return state
    except Exception as e:
        print("Failed to resolve_hcp data. e:", e)
    finally:
        db.close()
