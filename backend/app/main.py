from fastapi import FastAPI
from backend.app.models import Opportunity, OpportunityCreate

app = FastAPI(title="Scout API")
@app.post("/opportunities")
def create_opportunity(opportunity: OpportunityCreate):
    new_opportunity = Opportunity(
        id=2,
        title=opportunity.title,
        company=opportunity.company,
        location=opportunity.location,
        salary=opportunity.salary,
        url=opportunity.url,
    )

    return new_opportunity
def get_opportunities() -> list[Opportunity]:
    opportunities = [
        Opportunity(
            id=1,
            title="Software Engineer",
            company="OpenAI",
            location="London",
            salary="£70,000",
            url="https://openai.com/careers",
        )
    ]

    return opportunities