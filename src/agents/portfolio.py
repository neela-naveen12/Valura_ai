def portfolio_health_agent(context):
    portfolio = context.get("portfolio", [])

    if not portfolio:
        return {
            "observations": [
                {
                    "severity": "info",
                    "text": "You don’t have investments yet. Start with goals and risk level."
                }
            ],
            "disclaimer": "This is not investment advice."
        }

    total = sum(p["value"] for p in portfolio)

    weights = [p["value"] / total for p in portfolio]

    top = max(weights)
    top3 = sum(sorted(weights, reverse=True)[:3])

    observations = []

    if top > 0.5:
        observations.append({
            "severity": "warning",
            "text": "Over 50% in one stock — high concentration risk."
        })

    return {
        "concentration_risk": {
            "top_position_pct": round(top * 100, 2),
            "top_3_positions_pct": round(top3 * 100, 2),
            "flag": "high" if top > 0.5 else "moderate"
        },
        "observations": observations,
        "disclaimer": "This is not investment advice."
    }