def check_safety(query: str):
    q = query.lower()

    if "insider" in q or "inside info" in q:
        return _block("insider_trading")

    if "guaranteed profit" in q or "100% return" in q:
        return _block("guaranteed_returns")

    if "pump" in q or "manipulate" in q:
        return _block("market_manipulation")

    if "all in" in q or "borrow money" in q:
        return _block("reckless_behavior")

    return {"blocked": False}


def _block(reason):
    messages = {
        "insider_trading": "I can’t assist with insider or non-public information.",
        "guaranteed_returns": "No investment can guarantee returns.",
        "market_manipulation": "I cannot help with manipulating markets.",
        "reckless_behavior": "This approach is financially risky."
    }

    return {
        "blocked": True,
        "reason": reason,
        "message": messages[reason]
    }