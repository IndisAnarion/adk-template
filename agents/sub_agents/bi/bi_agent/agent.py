"""Business Intelligence agent implementation."""

from google.adk.agents import Agent
from agents import prompt

def create_bi_agent() -> Agent:
    """Create a Business Intelligence specialized agent.
    
    Returns:
        Agent: Configured BI agent
    """
    return Agent(
        model="gemini-2.0-flash-001",
        name="bi_agent",
        description="Business Intelligence agent for analytics and reporting",
        instruction=prompt.BI_AGENT_INSTRUCTION,
    )

root_agent = create_bi_agent()
