import ollama


class Planner:

    def __init__(self, model="qwen3:4b"):
        self.model = model

    def create_plan(self, requirement):

        prompt = f"""
You are an AI planning assistant.

Create a short execution plan for this procurement request.

Requirement:

Category: {requirement.category}
Location: {requirement.location}
Certification: {requirement.certification}
Minimum Capacity: {requirement.min_capacity}
Maximum Delivery Days: {requirement.max_delivery_days}

Return ONLY a Python-style dictionary.

Example:

{{
    "goal":"Find suppliers",
    "steps":[
        "Search suppliers",
        "Apply filters",
        "Validate",
        "Score",
        "Rank",
        "Generate outreach"
    ]
}}
"""

        try:

            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception:

            return {
                "goal": "Find suppliers",
                "steps": [
                    "Search suppliers",
                    "Apply filters",
                    "Validate suppliers",
                    "Calculate scores",
                    "Rank suppliers",
                    "Generate outreach"
                ]
            }


planner = Planner()


def create_plan(requirement):
    return planner.create_plan(requirement)