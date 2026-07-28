from pydantic import BaseModel


class Opportunity(BaseModel):
    id: int
    title: str
    company: str
    location: str
    status: str
    notes: str