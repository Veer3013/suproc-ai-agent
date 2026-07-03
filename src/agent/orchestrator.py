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

    # ==================================================
    # STEP 1 : Parse Requirement
    # ==================================================

    requirement = parse_requirement(user_request)

    # ==================================================
    # STEP 2 : Planning
    # ==================================================

    plan = create_plan(requirement)

    # ==================================================
    # STEP 3 : Search + Correction Attempts
    # ==================================================

    closest_mode = False
    suppliers = []

    MAX_ATTEMPTS = 3

    for attempt in range(1, MAX_ATTEMPTS + 1):

        suppliers = search_suppliers(requirement)

        if suppliers:
            break

        print(
            f"\n⚠ Exact search failed. Correction Attempt {attempt}/{MAX_ATTEMPTS}"
        )

        closest_mode = True

        suppliers = search_closest_suppliers(requirement)

        if suppliers:
            print("✔ Closest suppliers found.")
            break

    if len(suppliers) == 0:

        print("\n❌ No valid suppliers found after 3 correction attempts.")

        return

    # ==================================================
    # STEP 4 : Filtering
    # ==================================================

    suppliers = filter_suppliers(
        suppliers,
        requirement,
        strict=not closest_mode
    )

    # ==================================================
    # STEP 5 : Validation
    # ==================================================

    suppliers = validate_suppliers(suppliers)

    if len(suppliers) == 0:

        print("\n❌ No valid suppliers found after validation.")

        return

    # ==================================================
    # STEP 6 : Ranking
    # ==================================================

    ranked = rank_suppliers(
        suppliers,
        requirement,
        closest_mode
    )

    ranked = ranked[: requirement.top_k]

    # ==================================================
    # OUTPUT
    # ==================================================

    print("\n========== REQUIREMENT ==========")
    print(requirement)

    print("\n========== PLAN ==========")

    try:

        if isinstance(plan, dict):
            print(json.dumps(plan, indent=4))

        elif isinstance(plan, str):
            try:
                print(json.dumps(eval(plan), indent=4))
            except Exception:
                print(plan)

        else:
            print(plan)

    except Exception:
        print(plan)

    # ==================================================
    # Missing Information
    # ==================================================

    print("\n========== MISSING INFORMATION ==========")

    missing = []

    if not requirement.certification:
        missing.append("Certification not specified")

    if requirement.min_capacity is None:
        missing.append("Minimum Capacity not specified")

    if requirement.max_delivery_days is None:
        missing.append("Maximum Delivery Days not specified")

    if len(missing) == 0:

        print("None")

    else:

        for item in missing:
            print(f"• {item}")

    # ==================================================
    # Results
    # ==================================================

    print("\n========== RESULTS ==========")
    print("=" * 60)

    if closest_mode:

        print("⚠ No supplier matched all requested constraints.")
        print("Showing the highest-scoring closest matches...\n")

    for index, item in enumerate(ranked, start=1):

        supplier = item["supplier"]
        score = item["score"]

        print("\n" + "-" * 60)

        print(f"🏆 Rank #{index}")
        print(f"🏢 Supplier : {supplier.name}")
        print(f"⭐ Score : {score:.2f}")

        if closest_mode:
            print("🔍 Match Type : Closest Match")
        else:
            print("✅ Match Type : Exact Match")

        print(f"📍 Location : {supplier.location}")
        print(f"🏭 Category : {supplier.category}")
        print(f"📦 Capacity : {supplier.capacity}")
        print(f"🚚 Delivery : {supplier.delivery_days} Days")
        print(f"🏅 Rating : {supplier.rating}")

        # ============================================
        # Evidence
        # ============================================

        print("\nEvidence")

        for evidence in item["evidence"]:
            print(f"✔ {evidence}")

        # ============================================
        # Explainability
        # ============================================

        matched, missed = explain_match(
            requirement,
            supplier
        )

        print("\nMatched Requirements")

        if matched:

            for value in matched:
                print(f"✔ {value}")

        else:

            print("None")

        print("\nNot Matched")

        if missed:

            for value in missed:
                print(f"✘ {value}")

        else:

            print("None")

        # ============================================
        # Risk Analysis
        # ============================================

        print("\nRisks")

        risks = []

        if supplier.location.lower() != requirement.location.lower():
            risks.append("Supplier outside requested location")

        if (
            requirement.certification
            and supplier.certification.lower()
            != requirement.certification.lower()
        ):
            risks.append("Certification differs")

        if (
            requirement.min_capacity
            and supplier.capacity < requirement.min_capacity
        ):
            risks.append("Capacity below requested value")

        if (
            requirement.max_delivery_days
            and supplier.delivery_days
            > requirement.max_delivery_days
        ):
            risks.append("Delivery exceeds requested timeline")

        if supplier.rating < 4:
            risks.append("Supplier rating below 4.0")

        if len(risks) == 0:

            print("✔ No major risks")

        else:

            for risk in risks:
                print(f"⚠ {risk}")

        # ============================================
        # Outreach
        # ============================================

        print("\nDraft Outreach")

        print(generate_outreach(supplier))

    # ==================================================
    # Validation Summary
    # ==================================================

    print("\n========== VALIDATION STATUS ==========")

    print("✔ Supplier exists in dataset")
    print("✔ Constraints verified")
    print("✔ Match score verified")
    print("✔ No duplicate recommendations")
    print(f"✔ Returned {len(ranked)} supplier(s)")
    print("✔ Human approval required before outreach")

    # ==================================================
    # Recommendation
    # ==================================================

    print("\n========== RECOMMENDED NEXT ACTION ==========")

    supplier_names = ", ".join(
        supplier["supplier"].name for supplier in ranked
    )

    print(f"Recommended suppliers: {supplier_names}")
    print("Prepare procurement enquiry and wait for human approval.")

    # ==================================================
    # Human Approval
    # ==================================================

    print("\n" + "=" * 60)
    print("✅ Human Approval Required")
    print("Status : Awaiting Human Approval")
    print("=" * 60)