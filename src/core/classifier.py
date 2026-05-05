def classify(query: str, history: list):
    q = query.lower()

    if "portfolio" in q or "health" in q or "diversified" in q:
        agent = "portfolio_health"
    elif "invest" in q:
        agent = "investment_strategy"
    elif "stock" in q or "apple" in q:
        agent = "market_research"
    else:
        agent = "support"

    return {
        "intent": agent,
        "agent": agent,
        "entities": extract_entities(query),
        "safety_verdict": "safe"
    }


def extract_entities(query):
    entities = {"tickers": [], "amount": None}

    if "apple" in query.lower():
        entities["tickers"].append("AAPL")

    if "lakh" in query.lower():
        entities["amount"] = 100000

    return entities