from fastapi import FastAPI
from backend.app.models import Opportunity

app = FastAPI(title="Scout API")

@app.get("/")
def home():
    return {
        "status": "running",
        "application": "Scout",
        "message": "Scout API Running"
    }
@app.get("/health")
def health():
    return {
    "status": "healthy"
}
@app.get("/opportunities")
def get_opportunities() -> list[Opportunity]:
    
    return [
        {
            "id": 1,
            "title": "Software Engineer",
            "company": "OpenAI",
            "location": "London"
        }
    ]

