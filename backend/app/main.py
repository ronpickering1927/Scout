from fastapi import FastAPI
from backend.app.models import Opportunity

app = FastAPI(title="Scout API")
@app.get("/opportunities")
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