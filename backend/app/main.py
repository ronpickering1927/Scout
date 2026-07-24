from fastapi import FastAPI

app = FastAPI(title="Scout API")

@app.get("/")
def home():
    return {
        "status": "running",
        "application": "Scout",
        "message": "Scout API Running"
    }
