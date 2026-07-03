from sqlalchemy import select, and_, or_

from src.database.database import SessionLocal
from src.database.models import Supplier
from src.models.schemas import Requirement


def search_suppliers(requirement: Requirement):
    """
    Exact search using all hard constraints.
    """

    db = SessionLocal()

    try:

        query = select(Supplier)

        filters = []

        if requirement.category:
            filters.append(
                Supplier.category.ilike(requirement.category)
            )

        if requirement.location:
            filters.append(
                Supplier.location.ilike(requirement.location)
            )

        if requirement.certification:
            filters.append(
                Supplier.certification.ilike(requirement.certification)
            )

        if requirement.min_capacity is not None:
            filters.append(
                Supplier.capacity >= requirement.min_capacity
            )

        if requirement.max_delivery_days is not None:
            filters.append(
                Supplier.delivery_days <= requirement.max_delivery_days
            )

        filters.append(Supplier.available.is_(True))

        query = query.where(and_(*filters))

        return db.execute(query).scalars().all()

    finally:
        db.close()


def search_closest_suppliers(requirement: Requirement):
    """
    Relaxed search.

    Returns suppliers matching ANY important requirement.
    Final ranking is handled in scoring.py.
    """

    db = SessionLocal()

    try:

        conditions = []

        if requirement.category:
            conditions.append(
                Supplier.category.ilike(requirement.category)
            )

        if requirement.location:
            conditions.append(
                Supplier.location.ilike(requirement.location)
            )

        if requirement.certification:
            conditions.append(
                Supplier.certification.ilike(requirement.certification)
            )

        if requirement.min_capacity is not None:
            conditions.append(
                Supplier.capacity >= requirement.min_capacity
            )

        if requirement.max_delivery_days is not None:
            conditions.append(
                Supplier.delivery_days <= requirement.max_delivery_days
            )

        query = (
            select(Supplier)
            .where(
                Supplier.available.is_(True),
                or_(*conditions)
            )
        )

        return db.execute(query).scalars().all()

    finally:
        db.close()