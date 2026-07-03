from src.models.schemas import Requirement
from src.tools.search import search_suppliers


def test_search():

    requirement = Requirement(
        category="Packaging",
        location="Tamil Nadu",
        certification="Food Grade"
    )

    result = search_suppliers(requirement)

    assert isinstance(result, list)