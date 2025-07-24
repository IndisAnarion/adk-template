import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from agents.sub_agents.maps.maps_agent.tools.google_maps_mcp import google_maps_mcp_tools
from agents.sub_agents.maps.maps_agent.prompt import MAPS_AGENT_INSTRUCTION

maps_tools = google_maps_mcp_tools

maps_agent = Agent(
    name="maps_agent",
    model="gemini-2.0-flash-001",
    description="Provides access to Google Maps functionalities.",
    instruction=MAPS_AGENT_INSTRUCTION,
    tools=[maps_tools]
)

root_agent = maps_agent