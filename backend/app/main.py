from fastapi import FastAPI
from backend.app.models import Opportunity, OpportunityCreate

app = FastAPI(title="Scout API")
@app.get("/opportunities")
@app.post("/opportunities")
def create_opportunity(opportunity: OpportunityCreate):
    return opportunity
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