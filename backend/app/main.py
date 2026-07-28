from fastapi import FastAPI

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
