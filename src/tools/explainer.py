def explain_match(requirement, supplier):

    matched = []
    missed = []

    # Category
    if supplier.category.lower() == requirement.category.lower():
        matched.append("Category")
    else:
        missed.append(f"Category ({supplier.category})")

    # Location
    if supplier.location.lower() == requirement.location.lower():
        matched.append("Location")
    else:
        missed.append(f"Location ({supplier.location})")

    # Certification
    if requirement.certification:

        if supplier.certification.lower() == requirement.certification.lower():
            matched.append("Certification")
        else:
            missed.append(f"Certification ({supplier.certification})")

    # Capacity
    if requirement.min_capacity:

        if supplier.capacity >= requirement.min_capacity:
            matched.append("Capacity")
        else:
            missed.append(f"Capacity ({supplier.capacity})")

    # Delivery

    if requirement.max_delivery_days:

        if supplier.delivery_days <= requirement.max_delivery_days:
            matched.append("Delivery")
        else:
            missed.append(f"Delivery ({supplier.delivery_days} days)")

    return matched, missed