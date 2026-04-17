from sqlalchemy.orm import Session
from app.models.interaction import Interaction

def edit_interaction_tool(db: Session, interaction_id: int, updates: dict):
    row = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if not row:
        return {"error": "Interaction not found"}

    for k, v in updates.items():
        setattr(row, k, v)

    db.commit()
    db.refresh(row)

    return {
        "tool": "edit_interaction",
        "interaction_id": row.id,
        "updated_fields": list(updates.keys())
    }