from pydantic import BaseModel


class Opportunity(BaseModel):
    id: int
    title: str
    company: str
    location: str
    salary: str
    url: str


class OpportunityCreate(BaseModel):
    title: str
    company: str
    location: str
    salary: str
    url: str