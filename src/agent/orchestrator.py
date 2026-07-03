import json

from src.llm.parser import parse_requirement
from src.llm.planner import create_plan

from src.tools.search import (
    search_suppliers,
    search_closest_suppliers
)

from src.tools.filter import filter_suppliers
from src.tools.validation import validate_suppliers
from src.tools.scoring import rank_suppliers
from src.tools.explainer import explain_match

from src.llm.outreach import generate_outreach


def run_agent(user_request: str):

    # ----------------------------------
    # STEP 1 : Parse Requirement
    # ----------------------------------

    requirement = parse_requirement(user_request)

    # ----------------------------------
    # STEP 2 : Create Plan
    # ----------------------------------

    plan = create_plan(requirement)

    # ----------------------------------
    # STEP 3 : Exact Search
    # ----------------------------------

    suppliers = search_suppliers(requirement)

    closest_mode = False

    # ----------------------------------
    # STEP 4 : Closest Search
    # ----------------------------------

    if len(suppliers) == 0:

        closest_mode = True

        suppliers = search_closest_suppliers(requirement)

        suppliers = filter_suppliers(
            suppliers,
            requirement,
            strict=False
        )

    else:

        suppliers = filter_suppliers(
            suppliers,
            requirement,
            strict=True
        )

    # ----------------------------------
    # STEP 5 : Validation
    # ----------------------------------

    suppliers = validate_suppliers(suppliers)

    # ----------------------------------
    # STEP 6 : Ranking
    # ----------------------------------

    ranked = rank_suppliers(
        suppliers,
        requirement,
        closest_mode
    )

    ranked = ranked[: requirement.top_k]

    # ----------------------------------
    # OUTPUT
    # ----------------------------------

    print("\n========== REQUIREMENT ==========")
    print(requirement)

    print("\n========== PLAN ==========")

    try:
        if isinstance(plan, str):
            print(json.dumps(eval(plan), indent=4))
        else:
            print(json.dumps(plan, indent=4))
    except Exception:
        print(plan)

    print("\n========== RESULTS ==========")
    print("=" * 60)

    if closest_mode:
        print("⚠ No supplier matched all requested constraints.")
        print("Showing the highest-scoring closest matches...\n")

    if len(ranked) == 0:
        print("No suppliers found.")
        return

    for index, item in enumerate(ranked, start=1):

        supplier = item["supplier"]
        score = item["score"]

        print("\n" + "-" * 60)

        print(f"🏆 Rank #{index}")
        print(f"🏢 Supplier : {supplier.name}")
        print(f"⭐ Score : {score}")

        if closest_mode:
            print("🔍 Match Type : Closest Match")
        else:
            print("✅ Match Type : Exact Match")

        print(f"📍 Location : {supplier.location}")
        print(f"🏭 Category : {supplier.category}")
        print(f"📦 Capacity : {supplier.capacity}")
        print(f"🚚 Delivery : {supplier.delivery_days} Days")
        print(f"🏅 Rating : {supplier.rating}")

        print("\nEvidence")

        for evidence in item["evidence"]:
            print(f"✔ {evidence}")

        matched, missed = explain_match(
            requirement,
            supplier
        )

        print("\nMatched Requirements")

        if matched:
            for value in matched:
                print(f"✔ {value}")

        if missed:
            print("\nNot Matched")

            for value in missed:
                print(f"✘ {value}")

        print("\nDraft Outreach")
        print(generate_outreach(supplier))

    print("\n" + "=" * 60)
    print("✅ Human Approval Required")
    print("Status : Awaiting Human Approval")
    print("=" * 60)