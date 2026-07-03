from src.database.models import Supplier
from src.models.schemas import Requirement


def calculate_score(
    supplier: Supplier,
    requirement: Requirement,
    closest_mode: bool = False
):
    """
    Requirement-aware scoring.

    Exact Search:
        Quality based scoring

    Closest Search:
        Requirement matching gets highest priority.
    """

    score = 0
    evidence = []

    # ----------------------------------
# CATEGORY
# ----------------------------------

    if (
    requirement.category
    and supplier.category.lower()
    == requirement.category.lower()
    ):

        score += 30
        evidence.append("Category Match")

# ----------------------------------
# LOCATION
# ----------------------------------

    if (
    requirement.location
    and supplier.location.lower()
    == requirement.location.lower()
    ):

        score += 30
        evidence.append("Location Match")

# ----------------------------------
# CERTIFICATION
# ----------------------------------

    if requirement.certification:

        if (
        supplier.certification.lower()
        == requirement.certification.lower()
        ):

            score += 15
            evidence.append("Certification Match")

    # ----------------------------------
    # CAPACITY
    # ----------------------------------

    if requirement.min_capacity is not None:

        if supplier.capacity >= requirement.min_capacity:

            score += 10
            evidence.append("Capacity OK")

            extra = supplier.capacity - requirement.min_capacity

            score += min(extra / 10000, 5)

    # ----------------------------------
    # DELIVERY
    # ----------------------------------

    if requirement.max_delivery_days is not None:

        if supplier.delivery_days <= requirement.max_delivery_days:

            score += 10
            evidence.append("Delivery OK")

            bonus = (
                requirement.max_delivery_days
                - supplier.delivery_days
            ) / 5

            score += min(bonus, 5)

    # ----------------------------------
    # RATING
    # ----------------------------------

    rating_score = (supplier.rating / 5) * 10

    score += rating_score

    evidence.append(f"Rating {supplier.rating}/5")

    # ----------------------------------
    # SUSTAINABILITY
    # ----------------------------------

    if supplier.sustainability_score:

        sustain = (
            supplier.sustainability_score / 100
        ) * 5

        score += sustain

        evidence.append(
            f"Sustainability {supplier.sustainability_score}"
        )

    # ----------------------------------
    # AVAILABLE
    # ----------------------------------

    if supplier.available:

        score += 5

        evidence.append("Available")

    return round(score, 2), evidence


def rank_suppliers(
    suppliers,
    requirement: Requirement,
    closest_mode: bool = False
):

    ranked = []

    for supplier in suppliers:

        score, evidence = calculate_score(
            supplier,
            requirement,
            closest_mode
        )

        ranked.append({

            "supplier": supplier,

            "score": score,

            "evidence": evidence

        })

    ranked.sort(

        key=lambda item: item["score"],

        reverse=True

    )

    return ranked