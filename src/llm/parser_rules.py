import re

from src.models.schemas import Requirement


def parse_requirement(text: str) -> Requirement:
    """
    Rule-based fallback parser.

    Used only if Ollama parsing fails.
    """

    text = text.lower()

    # ------------------------
    # CATEGORY
    # ------------------------

    category = "Packaging"

    if "logistic" in text:
        category = "Logistics"

    elif "manufact" in text:
        category = "Manufacturing"

    elif "raw material" in text:
        category = "Raw Material"

    elif "pack" in text:
        category = "Packaging"

    # ------------------------
    # LOCATION
    # ------------------------

    location = ""

    if "tamil nadu" in text or "tamilnadu" in text:
        location = "Tamil Nadu"

    elif "karnataka" in text:
        location = "Karnataka"

    elif "kerala" in text:
        location = "Kerala"

    elif "andhra pradesh" in text:
        location = "Andhra Pradesh"

    elif "telangana" in text:
        location = "Telangana"

    # ------------------------
    # CERTIFICATION
    # ------------------------

    certification = None

    if "food grade" in text:
        certification = "Food Grade"

    elif "biodegradable" in text:
        certification = "Biodegradable"

    elif "fssai" in text:
        certification = "FSSAI"

    # ------------------------
    # CAPACITY
    # ------------------------

    min_capacity = None

    capacity_match = re.search(
        r"capacity\s*(\d+)",
        text
    )

    if capacity_match:
        min_capacity = int(capacity_match.group(1))

    else:

        numbers = re.findall(r"\d+", text)

        if numbers:
            min_capacity = int(numbers[0])

    # ------------------------
    # DELIVERY
    # ------------------------

    max_delivery_days = None

    delivery_match = re.search(
        r"(\d+)\s*day",
        text
    )

    if delivery_match:
        max_delivery_days = int(
            delivery_match.group(1)
        )

    # ------------------------
    # TOP K
    # ------------------------

    top_k = 3

    top_match = re.search(
        r"top\s*(\d+)",
        text
    )

    if top_match:
        top_k = int(top_match.group(1))

    return Requirement(
        category=category,
        location=location,
        certification=certification,
        min_capacity=min_capacity,
        max_delivery_days=max_delivery_days,
        top_k=top_k
    )