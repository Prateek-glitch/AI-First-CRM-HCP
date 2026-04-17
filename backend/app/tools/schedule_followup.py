from sqlalchemy.orm import Session
from datetime import date
from app.models.followup import FollowUpTask

def schedule_followup_tool(db: Session, interaction_id: int, due_date: str, owner: str, note: str = ""):
    task = FollowUpTask(
        interaction_id=interaction_id,
        due_date=date.fromisoformat(due_date),
        owner=owner,
        note=note,
        status="Open"
    )
    db.add(task)
    db.commit()
    db.refresh(task)

    return {
        "tool": "schedule_followup",
        "task_id": task.id,
        "interaction_id": task.interaction_id,
        "due_date": str(task.due_date),
        "owner": task.owner,
        "status": task.status
    }