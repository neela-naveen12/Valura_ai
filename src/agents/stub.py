def stub_agent(agent_name, context):
    return {
        "agent": agent_name,
        "intent": context.get("intent"),
        "entities": context.get("entities"),
        "message": f"{agent_name} agent is not implemented."
    }