import json
import re
import ollama


class OllamaClient:

    def __init__(self, model="qwen3:4b"):
        self.model = model

    def parse_requirement(self, user_request: str):

        prompt = f"""
You are an AI procurement requirement extractor.

Return ONLY ONE valid JSON object.

Schema:

{{
  "category": "Packaging | Logistics | Manufacturing | Raw Material",
  "location": "",
  "certification": "Food Grade | Biodegradable | FSSAI",
  "minimum_capacity": null,
  "maximum_delivery_days": null,
  "requested_results": 3
}}

Rules:

1. category MUST be ONLY one of:
   Packaging
   Logistics
   Manufacturing
   Raw Material

2. NEVER include certification words inside category.

3. If the request contains "Food Grade", put it in certification.

4. Return ONLY JSON.

5. No explanation.

Do not explain.
Do not use markdown.
Do not wrap inside ```.

User Request:
{user_request}
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

            content = response["message"]["content"].strip()

            # Remove <think>...</think>
            content = re.sub(
                r"<think>.*?</think>",
                "",
                content,
                flags=re.DOTALL
            ).strip()

            # Extract JSON block
            match = re.search(r"\{.*\}", content, re.DOTALL)

            if match:
                content = match.group()

            data = json.loads(content)

            return {
                "category": data.get("category", ""),
                "location": data.get("location", ""),
                "certification": data.get("certification"),
                "minimum_capacity": data.get("minimum_capacity"),
                "maximum_delivery_days": data.get("maximum_delivery_days"),
                "requested_results": data.get("requested_results", 3)
            }

        except Exception as e:

            print("\n⚠ Ollama parsing failed.")
            print(e)

            return None