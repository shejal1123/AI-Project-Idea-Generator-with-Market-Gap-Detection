```python id="9jxtzv"
from fastapi import FastAPI
from app.api.api import router

app = FastAPI(
    title="AI Project Idea Generator",
    description="AI-powered project idea generator with market gap detection",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Backend is running successfully"}
