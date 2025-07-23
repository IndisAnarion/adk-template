"""Employee Operations agent implementation."""

from __future__ import annotations

from google.adk.agents import Agent
from agents import prompt

def create_employee_agent() -> Agent:
    """Create an Employee Operations specialized agent.
    
    Returns:
        Agent: Configured Employee agent
    """
    return Agent(
        model="gemini-2.0-flash-001",
        name="employee_agent",
        description="Employee Operations agent for HR and personnel matters",
        instruction=prompt.EMPLOYEE_AGENT_INSTRUCTION,
    )

root_agent = create_employee_agent()
