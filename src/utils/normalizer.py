def normalize_requirement(data: dict) -> dict:
    """
    Normalize LLM output into values used by the database.
    """

    # ---------- CATEGORY ----------
    category = (data.get("category") or "").lower()

    if "pack" in category or "container" in category:
        data["category"] = "Packaging"

    elif "logistic" in category:
        data["category"] = "Logistics"

    elif "manufact" in category:
        data["category"] = "Manufacturing"

    elif "raw" in category:
        data["category"] = "Raw Material"

    # Recover certification if LLM merged it into category
    original_category = (data.get("category") or "").lower()

    if "food" in original_category and not data.get("certification"):
        data["certification"] = "Food Grade"

    elif "bio" in original_category and not data.get("certification"):
        data["certification"] = "Biodegradable"

    # ---------- LOCATION ----------
    location = (data.get("location") or "").lower().strip()

    location_map = {
        "tn": "Tamil Nadu",
        "tamilnadu": "Tamil Nadu",
        "tamil nadu": "Tamil Nadu",

        "ka": "Karnataka",
        "karnataka": "Karnataka",

        "kerala": "Kerala",

        "ap": "Andhra Pradesh",
        "andhra": "Andhra Pradesh",
        "andhra pradesh": "Andhra Pradesh",

        "ts": "Telangana",
        "telangana": "Telangana",
    }

    if location in location_map:
        data["location"] = location_map[location]

    # ---------- CERTIFICATION ----------
    cert = (data.get("certification") or "").lower()

    if "food" in cert:
        data["certification"] = "Food Grade"

    elif "bio" in cert:
        data["certification"] = "Biodegradable"

    elif "fssai" in cert:
        data["certification"] = "FSSAI"

    return data