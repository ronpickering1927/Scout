from fastapi import FastAPI, HTTPException

from backend.app.models import Opportunity, OpportunityCreate
from backend.app.database import (
    add_opportunity,
    get_all_opportunities,
    get_opportunity_by_id,
    update_opportunity as db_update_opportunity,
    delete_opportunity as db_delete_opportunity,
)
app = FastAPI(
    title="Scout API",
    version="0.1.0",
    description="Scout job opportunity API",
)

opportunities = [
    Opportunity(
        id=1,
        title="Software Engineer",
        company="OpenAI",
        location="London",
        salary="£70,000",
        url="https://openai.com/careers",
    ),
    Opportunity(
        id=2,
        title="Python Developer",
        company="Scout Ltd",
        location="Remote",
        salary="£60,000",
        url="https://example.com/job",
    ),
]


@app.get("/opportunities")
def get_opportunities() -> list[Opportunity]:
    return get_all_opportunities()


@app.get("/opportunities/{opportunity_id}")
def get_opportunity(opportunity_id: int):
    opportunity = get_opportunity_by_id(opportunity_id)

    if opportunity is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")

    return opportunity

   


@app.post("/opportunities")
def create_opportunity(opportunity: OpportunityCreate):
    new_id = 0

    new_opportunity = Opportunity(
        id=new_id,
        title=opportunity.title,
        company=opportunity.company,
        location=opportunity.location,
        salary=opportunity.salary,
        url=opportunity.url,
    )

    opportunities.append(new_opportunity)
    new_opportunity.id = add_opportunity(new_opportunity)
    return new_opportunity


@app.put("/opportunities/{opportunity_id}")
def update_opportunity(opportunity_id: int, updated: OpportunityCreate):
    existing = get_opportunity_by_id(opportunity_id)

    if existing is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")

    updated_opportunity = Opportunity(
        id=opportunity_id,
        title=updated.title,
        company=updated.company,
        location=updated.location,
        salary=updated.salary,
        url=updated.url,
    )

    db_update_opportunity(updated_opportunity)

    return updated_opportunity


@app.delete("/opportunities/{opportunity_id}")
def delete_opportunity(opportunity_id: int):
    existing = get_opportunity_by_id(opportunity_id)

    if existing is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")

    db_delete_opportunity(opportunity_id)

    return existing