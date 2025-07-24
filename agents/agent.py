from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool
import litellm
from agents import prompt
from google.adk.tools import google_search
# from agents.sub_agents.bi import root_agent as bi_agent
# from agents.sub_agents.employee import root_agent as employee_agent
from agents.sub_agents.weather.weather_agent.agent import weather_agent
from agents.sub_agents.webSearch.web_search_agent.agent import root_agent as web_search_agent
from agents.sub_agents.maps.maps_agent.agent import maps_agent

def create_orchestrator() -> Agent:
    """Create the main orchestrator agent with BI and Employee sub-agents.
    
    This follows ADK multi-agent patterns from travel-concierge sample where
    a root agent coordinates multiple specialized sub-agents.
    
    Returns:
        Agent: Configured orchestrator agent with sub-agents
    """
    
    return Agent(
        # model="gemini-2.0-flash-001",
        # model=LiteLlm(model="ollama_chat/llama3.2:3b"),
        model=LiteLlm(model="azure/gpt-4.1"),
        name="root_agent",
        description="Root orchestrator agent that coordinates multiple specialized sub-agents.",
        instruction=prompt.ROOT_AGENT_INSTRUCTION,
        sub_agents=[
            # bi_agent,
            # employee_agent,
            weather_agent,
            maps_agent
            # web_search_agent
        ],
        tools=[AgentTool(agent=web_search_agent)],
    )

root_agent = create_orchestrator()