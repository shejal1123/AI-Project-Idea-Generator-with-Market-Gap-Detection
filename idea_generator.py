def generate_project_idea(domain: str):
    ideas = {
        "AI": "AI Resume Builder",
        "Healthcare": "AI Disease Prediction System",
        "Education": "AI Smart Learning Assistant",
        "Business": "AI Startup Validator"
    }

    return ideas.get(
        domain,
        "AI Project Idea Generator"
    )
