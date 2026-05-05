from src.core.classifier import classify

def test_portfolio_route():
    res = classify("check my portfolio", [])
    assert res["agent"] == "portfolio_health"