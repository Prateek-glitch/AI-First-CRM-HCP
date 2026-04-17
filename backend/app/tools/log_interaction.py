from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.models.hcp import HCP
from app.services.llm import summarize_interaction_with_llm  # <- use this function name


def log_interaction_tool(db: Session, payload: dict):
    hcp_id = payload.get("hcp_id")
    interaction_type = payload.get("interaction_type")
    interaction_date = payload.get("interaction_date")
    topics_discussed = payload.get("topics_discussed")
    attendees = payload.get("attendees")

    if not hcp_id:
        raise HTTPException(status_code=400, detail="hcp_id is required")

    hcp = db.query(HCP).filter(HCP.id == hcp_id).first()
    if not hcp:
        raise HTTPException(status_code=400, detail=f"Invalid hcp_id: {hcp_id}")

    # LLM summary (with fallback)
    try:
        ai_summary = summarize_interaction_with_llm({
            "interaction_type": interaction_type,
            "interaction_date": str(interaction_date),
            "topics_discussed": topics_discussed,
            "attendees": attendees,
        })
    except Exception:
        ai_summary = f"{interaction_type} with {attendees}. Topics: {topics_discussed}"

    interaction = Interaction(
        hcp_id=hcp_id,
        interaction_type=interaction_type,
        interaction_date=interaction_date,
        topics_discussed=topics_discussed,
        attendees=attendees,
        ai_summary=ai_summary,
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {
        "tool": "log_interaction",
        "interaction_id": interaction.id,
        "ai_summary": interaction.ai_summary,
    }