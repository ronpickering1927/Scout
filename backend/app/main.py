from fastapi import FastAPI, HTTPException
from backend.app.models import Opportunity, OpportunityCreate

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
    return opportunities


@app.get("/opportunities/{opportunity_id}")
def get_opportunity(opportunity_id: int):
    for opportunity in opportunities:
        if opportunity.id == opportunity_id:
            return opportunity

    raise HTTPException(status_code=404, detail="Opportunity not found")


@app.post("/opportunities")
def create_opportunity(opportunity: OpportunityCreate):
    new_opportunity = Opportunity(
        id=3,
        title=opportunity.title,
        company=opportunity.company,
        location=opportunity.location,
        salary=opportunity.salary,
        url=opportunity.url,
    )

    return new_opportunity
