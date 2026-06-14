from pydantic import BaseModel


class ProjectIdeaSchema(BaseModel):
    title: str
    category: str
    description: str
    market_gap: str

    class Config:
        from_attributes = True
