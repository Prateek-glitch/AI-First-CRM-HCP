from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.interaction import Interaction
from app.models.audit import InteractionAudit
from app.schemas.interaction import InteractionCreate, InteractionUpdate, InteractionOut
import json

router = APIRouter(prefix="/api/interactions", tags=["interactions"])

@router.post("/log", response_model=InteractionOut)
def log_interaction(payload: InteractionCreate, db: Session = Depends(get_db)):
    row = Interaction(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

@router.get("/{interaction_id}", response_model=InteractionOut)
def get_interaction(interaction_id: int, db: Session = Depends(get_db)):
    row = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return row

@router.put("/{interaction_id}", response_model=InteractionOut)
def edit_interaction(interaction_id: int, payload: InteractionUpdate, db: Session = Depends(get_db)):
    row = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Interaction not found")

    before = {
        "interaction_type": row.interaction_type,
        "interaction_date": str(row.interaction_date) if row.interaction_date else None,
        "interaction_time": str(row.interaction_time) if row.interaction_time else None,
        "attendees": row.attendees,
        "topics_discussed": row.topics_discussed,
        "materials_shared": row.materials_shared,
        "samples_distributed": row.samples_distributed,
        "sentiment": row.sentiment,
        "outcomes": row.outcomes,
        "follow_up_actions": row.follow_up_actions,
        "ai_summary": row.ai_summary,
    }

    updates = payload.model_dump(exclude_unset=True)
    for k, v in updates.items():
        setattr(row, k, v)

    db.commit()
    db.refresh(row)

    after = {
        "interaction_type": row.interaction_type,
        "interaction_date": str(row.interaction_date) if row.interaction_date else None,
        "interaction_time": str(row.interaction_time) if row.interaction_time else None,
        "attendees": row.attendees,
        "topics_discussed": row.topics_discussed,
        "materials_shared": row.materials_shared,
        "samples_distributed": row.samples_distributed,
        "sentiment": row.sentiment,
        "outcomes": row.outcomes,
        "follow_up_actions": row.follow_up_actions,
        "ai_summary": row.ai_summary,
    }

    audit = InteractionAudit(
        interaction_id=row.id,
        before_json=json.dumps(before),
        after_json=json.dumps(after),
        edited_by="Prateek-glitch"
    )
    db.add(audit)
    db.commit()

    return row