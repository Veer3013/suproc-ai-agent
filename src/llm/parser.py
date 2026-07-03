from src.llm.ollama_client import OllamaClient
from src.llm.parser_rules import parse_requirement as rule_parser
from src.models.schemas import Requirement
from src.utils.normalizer import normalize_requirement

ollama = OllamaClient(model="qwen3:4b")

def parse_requirement(text: str) -> Requirement:
    """
    Hybrid parser.

    1. Try Ollama.
    2. If anything fails, automatically use the rule-based parser.
    """

    result = ollama.parse_requirement(text)
    if result:
        result = normalize_requirement(result)

    # Ollama failed
    if result is None:
        print("\nUsing Rule-Based Parser...\n")
        return rule_parser(text)

    try:

        return Requirement(
            category=result.get("category", "Packaging"),
            location=result.get("location", ""),
            certification=result.get("certification"),
            min_capacity=result.get("minimum_capacity"),
            max_delivery_days=result.get("maximum_delivery_days"),
            top_k=result.get("requested_results", 3),
        )

    except Exception:

        print("\nInvalid AI output. Falling back to Rule-Based Parser...\n")

        return rule_parser(text)