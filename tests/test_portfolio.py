from src.agents.portfolio import portfolio_health_agent

def test_empty_portfolio():
    res = portfolio_health_agent({"portfolio": []})
    assert "observations" in res