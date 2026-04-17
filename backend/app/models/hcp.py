from sqlalchemy import Column, Integer, String
from app.db.session import Base

class HCP(Base):
    __tablename__ = "hcp"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    specialty = Column(String(120), nullable=True)
    hospital = Column(String(150), nullable=True)
    city = Column(String(80), nullable=True)