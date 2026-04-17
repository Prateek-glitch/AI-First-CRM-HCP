from sqlalchemy import Column, Integer, ForeignKey, String, Text, Date, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class FollowUpTask(Base):
    __tablename__ = "follow_up_tasks"

    id = Column(Integer, primary_key=True, index=True)
    interaction_id = Column(Integer, ForeignKey("interactions.id"), nullable=False)
    due_date = Column(Date, nullable=False)
    owner = Column(String(120), nullable=False)
    note = Column(Text, nullable=True)
    status = Column(String(30), nullable=False, default="Open")
    created_at = Column(DateTime(timezone=True), server_default=func.now())