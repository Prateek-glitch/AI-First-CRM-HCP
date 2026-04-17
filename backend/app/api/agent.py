from typing import TypedDict, Dict, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from langgraph.graph import StateGraph, END

from app.db.session import get_db
from app.tools.log_interaction import log_interaction_tool
from app.tools.edit_interaction import edit_interaction_tool
from app.tools.fetch_hcp import fetch_hcp_tool
from app.tools.suggest_nba import suggest_nba_tool
from app.tools.schedule_followup import schedule_followup_tool

router = APIRouter(prefix="/api/agent", tags=["Agent"])


class AgentState(TypedDict):
    intent: str
    payload: Dict[str, Any]
    db: Session
    result: Dict[str, Any]


def route_intent(state: AgentState) -> AgentState:
    intent = state["intent"]
    payload = state["payload"]
    db = state["db"]

    if intent == "log_interaction":
        result = log_interaction_tool(db, payload)
    elif intent == "edit_interaction":
        result = edit_interaction_tool(db, payload)
    elif intent == "fetch_hcp_profile":
        result = fetch_hcp_tool(db, payload)
    elif intent == "suggest_next_best_action":
        result = suggest_nba_tool(db, payload)
    elif intent == "schedule_followup":
        result = schedule_followup_tool(db, payload)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported intent: {intent}")

    return {**state, "result": result}


graph_builder = StateGraph(AgentState)
graph_builder.add_node("route_intent", route_intent)
graph_builder.set_entry_point("route_intent")
graph_builder.add_edge("route_intent", END)
agent_graph = graph_builder.compile()


@router.post("/chat")
def agent_chat(body: Dict[str, Any], db: Session = Depends(get_db)):
    intent = body.get("intent")
    payload = body.get("payload", {})

    if not intent:
        raise HTTPException(status_code=400, detail="intent is required")

    initial_state: AgentState = {
        "intent": intent,
        "payload": payload,
        "db": db,
        "result": {}
    }

    out = agent_graph.invoke(initial_state)
    return out["result"]