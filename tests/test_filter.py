from src.tools.filter import filter_suppliers
from src.models.schemas import Requirement


class DummySupplier:

    def __init__(self):
        self.available = True
        self.category = "Packaging"
        self.location = "Tamil Nadu"
        self.certification = "Food Grade"
        self.capacity = 15000
        self.delivery_days = 20


def test_filter():

    supplier = DummySupplier()

    requirement = Requirement(
        category="Packaging",
        location="Tamil Nadu",
        certification="Food Grade",
        min_capacity=10000,
        max_delivery_days=30
    )

    result = filter_suppliers(
        [supplier],
        requirement,
        strict=True
    )

    assert len(result) == 1