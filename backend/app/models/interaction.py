from sqlalchemy import Column, Integer, String, Text, Date, Time, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer, ForeignKey("hcp.id"), nullable=False)
    interaction_type = Column(String(50), nullable=False, default="Meeting")
    interaction_date = Column(Date, nullable=False)
    interaction_time = Column(Time, nullable=True)
    attendees = Column(Text, nullable=True)
    topics_discussed = Column(Text, nullable=True)
    materials_shared = Column(Text, nullable=True)
    samples_distributed = Column(Text, nullable=True)
    sentiment = Column(String(20), nullable=True)
    outcomes = Column(Text, nullable=True)
    follow_up_actions = Column(Text, nullable=True)
    ai_summary = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())