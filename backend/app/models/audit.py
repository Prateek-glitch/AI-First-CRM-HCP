from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, String
from sqlalchemy.sql import func
from app.db.session import Base

class InteractionAudit(Base):
    __tablename__ = "interaction_audit"

    id = Column(Integer, primary_key=True, index=True)
    interaction_id = Column(Integer, ForeignKey("interactions.id"), nullable=False)
    before_json = Column(Text, nullable=True)
    after_json = Column(Text, nullable=True)
    edited_by = Column(String(100), nullable=True, default="system")
    edited_at = Column(DateTime(timezone=True), server_default=func.now())