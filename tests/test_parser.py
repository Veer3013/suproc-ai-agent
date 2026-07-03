from src.llm.parser import parse_requirement


def test_parser():

    text = "Need food grade packaging supplier in Tamil Nadu with capacity 10000 delivery in 30 days"

    result = parse_requirement(text)

    assert result.category == "Packaging"
    assert result.location == "Tamil Nadu"
    assert result.certification == "Food Grade"
    assert result.min_capacity == 10000
    assert result.max_delivery_days == 30