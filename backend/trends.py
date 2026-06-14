from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_trends():
    return {
        "trending_topics": [
            "AI Automation",
            "Healthcare AI",
            "EdTech",
            "Creator Economy",
            "Cybersecurity",
            "FinTech",
            "Climate Tech"
        ]
    }
