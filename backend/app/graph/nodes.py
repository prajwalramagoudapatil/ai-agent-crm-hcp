from app.graph.state import GraphState
from langchain_core.runnables import RunnableConfig

from app.graph.tool.extract_tool import extract_tool
from app.graph.tool.summarize_tool import summarize_tool
from app.graph.tool.log_interaction_tool import log_interaction_tool
from app.graph.tool.update_interaction_tool import update_interaction_tool
from app.ai.llm_service import detect_intent
from app.graph.tool.hcp_resolver_tool import resolve_hcp
from app.graph.tool.edit_extract_tool import edit_extract_tool

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
        interaction_id = state["interaction_id"]
        tool_result_message = state.get("tool_result", {}).get("message", "Agent Failed")

        if state["hcp_conflict"]:

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

def resolve_hcp_node(state: GraphState, config: RunnableConfig):
    """
    Validates whether the selected HCP matches
    the HCP mentioned in the conversation.
    """
    db = config.get("configurable", {}).get("db")
    print('')
    try:
        result = resolve_hcp(
            db=db,
            selected_hcp_id=state["selected_hcp_id"],
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

def edit_interaction_node(state: GraphState, config: RunnableConfig) -> GraphState:
    """
    Update an existing interaction.
    """
    print("  ******  In edit interaction node")
    db = config.get("configurable", {}).get("db")
    result = update_interaction_tool(
        db=db,
        interaction_id=state["interaction_id"],
        state=state,
    )

    state["tool_result"] = result

    return state

def edit_extract_node(state: GraphState, config: RunnableConfig):
    db = config.get("configurable", {}).get("db")
    extracted = edit_extract_tool(state, db)
    print(f"  >>>>>>> tool res: {extracted}  extracted data:")
    print(state["extracted_data"])

    state["tool_result"] = extracted

    return state