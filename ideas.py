from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_ideas():
    return {
        "ideas": [
            {
                "title": "AI Career Roadmap Generator",
                "category": "Education",
                "description": "Generates personalized career roadmaps",
                "market_gap": "Students lack clear guidance"
            },
            {
                "title": "AI Startup Validator",
                "category": "Business",
                "description": "Checks startup potential using trends",
                "market_gap": "Founders struggle to validate ideas"
            },
            {
                "title": "AI Content Repurposer",
                "category": "Creator Economy",
                "description": "Turns one content into multiple formats",
                "market_gap": "Creators waste time repurposing content"
            }
        ]
    }
