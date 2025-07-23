from json import tool
from google.adk.agents import Agent
from agents import prompt
# from agents.sub_agents.bi import root_agent as bi_agent
# from agents.sub_agents.employee import root_agent as employee_agent
from agents.sub_agents.weather.weather_agent.agent import weather_agent

def create_orchestrator() -> Agent:
    """Create the main KAI orchestrator agent with BI and Employee sub-agents.
    
    This follows ADK multi-agent patterns from travel-concierge sample where
    a root agent coordinates multiple specialized sub-agents.
    
    Returns:
        Agent: Configured KAI orchestrator agent with sub-agents
    """
    
    return Agent(
        model="gemini-2.0-flash-001",
        name="root_agent",
        description="System orchestrator managing BI and Employee operations through specialized sub-agents",
        instruction=prompt.ROOT_AGENT_INSTRUCTION,
        sub_agents=[
            # bi_agent,
            # employee_agent,
            weather_agent,
        ],
    )

root_agent = create_orchestrator()