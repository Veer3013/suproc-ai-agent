from src.database.models import Supplier


def validate_suppliers(suppliers):
    """
    Validate supplier records before returning them.
    """

    valid_suppliers = []
    seen_ids = set()

    for supplier in suppliers:

        # Duplicate check
        if supplier.id in seen_ids:
            continue

        seen_ids.add(supplier.id)

        # Required fields
        if not supplier.name:
            continue

        if supplier.rating is None:
            continue

        if supplier.capacity is None:
            continue

        if supplier.delivery_days is None:
            continue

        if not supplier.available:
            continue

        valid_suppliers.append(supplier)

    return valid_suppliers