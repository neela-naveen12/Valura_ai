from src.agents.portfolio import portfolio_health_agent
from src.agents.stub import stub_agent

def route(agent_name, context):
    if agent_name == "portfolio_health":
        return portfolio_health_agent(context)

    return stub_agent(agent_name, context)