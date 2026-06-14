from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def market_gap_analysis():
    return {
        "market_gap": {
            "problem": "Students struggle to find unique and practical project ideas.",
            "opportunity": "AI-powered project recommendation platform",
            "competition_level": "Medium",
            "difficulty": "Intermediate",
            "potential_score": 8.7
        }
    }
