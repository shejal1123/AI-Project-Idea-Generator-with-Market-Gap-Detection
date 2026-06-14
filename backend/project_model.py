from sqlalchemy import Column, Integer, String
from app.core.database import Base


class ProjectIdea(Base):
    __tablename__ = "project_ideas"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    category = Column(String, nullable=False)

    description = Column(String, nullable=False)

    market_gap = Column(String, nullable=True)
