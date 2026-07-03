from src.models.schemas import Requirement


def filter_suppliers(
    suppliers,
    requirement: Requirement,
    strict: bool = True
):
    """
    Filters supplier list.

    strict=True
        Exact search (all constraints required)

    strict=False
        Closest search (only availability check)
    """

    filtered = []

    for supplier in suppliers:

        # Must always be available
        if not supplier.available:
            continue

        # Closest search
        if not strict:
            filtered.append(supplier)
            continue

        # -------------------------
        # Exact Search
        # -------------------------

        if requirement.certification:

            if (
                supplier.certification.lower()
                != requirement.certification.lower()
            ):
                continue

        if requirement.min_capacity is not None:

            if supplier.capacity < requirement.min_capacity:
                continue

        if requirement.max_delivery_days is not None:

            if supplier.delivery_days > requirement.max_delivery_days:
                continue

        filtered.append(supplier)

    return filtered