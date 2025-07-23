from google.adk.agents import Agent
from .prompt import WEATHER_AGENT_INSTRUCTION
from .tools.function_tools import get_weather
from google.adk.models.lite_llm import LiteLlm

weather_agent = Agent(
    name="weather_agent",
    # model="gemini-2.0-flash-lite",
    model="gemini-2.0-flash-001",
    # model=LiteLlm(model="ollama_chat/llama3.2:3b"),
    description="Provides weather information for specific cities.",
    instruction=WEATHER_AGENT_INSTRUCTION,
    tools=[get_weather], 
)

root_agent = weather_agent