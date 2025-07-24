# Agent Development Kit (ADK) Instructions

## Primary Reference Sources

When making code suggestions for this repository, prioritize using these directories as primary reference sources:

- **adk-python/**: Core ADK library containing official implementation patterns, abstractions, and utilities
- **adk-docs/**: Comprehensive documentation with usage examples and best practices
- **adk-samples/**: Reference implementations showing correct implementation patterns

Always consult these directories first before suggesting any code implementations or modifications.

## Project Architecture

This repository follows the Agent Development Kit (ADK) structure - a code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents. The repository consists of several key components:

- **adk-python/**: Core ADK library with agent abstractions, tools, and deployment capabilities
- **adk-docs/**: Documentation resources for ADK
- **adk-samples/**: Sample agent implementations using ADK
- **agents/**: Custom agent implementations including:
  - Root orchestrator agent that delegates to specialized sub-agents
  - Sub-agents for various domains (Weather, Maps, Web Search, etc.)
  - Custom tools and utilities

## Key Components

### Core Abstractions

- **Agent**: The blueprint defining an agent's identity, instructions, and tools
- **Tool**: A capability function an agent can call to interact with the world
- **Runner**: The orchestration engine managing the "Reason-Act" loop
- **Session**: Holds conversation state for a single dialogue
- **Memory**: Long-term recall across different sessions

### Project-Specific Implementation

The project uses a multi-agent architecture with:

1. **Root Orchestrator Agent** (`agents/agent.py`): Coordinates between specialized sub-agents
2. **Sub-Agents** (in `agents/sub_agents/`): Domain-specific agents like:
   - Weather Agent: Provides weather information and forecasts
   - Maps Agent: Handles location and mapping requests
   - Web Search Agent: Performs web searches for information retrieval
3. **Custom Tools** (in sub-agent directories): Implementation-specific capabilities

### Canonical Project Structure

```
agents/
├── agent.py              # Root orchestrator agent
├── prompt.py             # Agent instructions
└── sub_agents/           # Domain-specific agents
    ├── weather/
    │   └── weather_agent/
    │       ├── agent.py  # Weather agent definition
    │       ├── prompt.py # Weather-specific instructions
    │       └── tools/    # Weather-specific tools
    ├── maps/
    │   └── maps_agent/
    │       ├── agent.py
    │       └── ...
    └── webSearch/
        └── web_search_agent/
            ├── agent.py
            └── ...
```

## Development Workflow

### Creating a New Agent

1. Create a directory within `agents/sub_agents/` following the structure above
2. Define your agent in `agent.py` with `root_agent = Agent(...)`
3. Import required tools from `google.adk.tools` or create custom tools
4. Add the agent to the root orchestrator in `agents/agent.py`

```python
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search_assistant",
    model="gemini-2.0-flash", 
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search]
)
```

### Model Configuration

The project supports multiple LLM backends:

1. **Google Gemini** (default): 
   ```python
   model="gemini-2.0-flash-001"
   ```

2. **LiteLLM Integration** (for other providers):
   ```python
   from google.adk.models.lite_llm import LiteLlm
   model=LiteLlm(model="azure/gpt-4.1")
   # OR
   model=LiteLlm(model="ollama_chat/llama3.2:3b")
   ```

### Testing & Debugging

1. **Interactive UI**: Run `adk web` and navigate to the web interface
2. **CLI**: Use `adk run` for quick terminal tests
3. **Programmatic**: Write tests with `pytest` for automated testing
4. **FastAPI Server**: Run `python main.py` to start the server at http://localhost:9999

### Deployment

Use `adk deploy` to deploy to Google Vertex Agent Engine, Cloud Run, or GKE.

## Code Style & Conventions

### Imports

- In ADK source: Use relative imports
  ```python
  # DO
  from ..agents.llm_agent import LlmAgent
  # DON'T
  from google.adk.agents.llm_agent import LlmAgent
  ```

- In tests: Use absolute imports
  ```python
  # DO
  from google.adk.agents.llm_agent import LlmAgent
  # DON'T
  from ..agents.llm_agent import LlmAgent
  ```

- Always include `from __future__ import annotations` at the top of files

### Python Style

- Follow Google Python Style Guide
- Indentation: 2 spaces
- Line Length: Maximum 80 characters
- Function/Variable Names: `snake_case`
- Class Names: `CamelCase`
- Constants: `UPPERCASE_SNAKE_CASE`

Run `./autoformat.sh` to apply formatting standards.

Commit messages follow [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) format with `#breaking` or `#non-breaking` tags.

## Project-Specific Patterns

### Agent Instructions

Agent instructions are defined in separate `prompt.py` files to keep the agent implementation clean. Example:

```python
# agents/prompt.py
ROOT_AGENT_INSTRUCTION = """
You are the System Assistant - a sophisticated AI coordinator that manages 
specialized sub-agents for different domains.

Your role is to:
1. Understand user requests and determine which domain(s) they relate to
2. Delegate to the appropriate sub-agent(s)
3. Coordinate multi-domain tasks that require multiple agents
4. Provide unified responses that synthesize information from multiple sources
"""
```

### Custom Tools

Custom tools are implemented in the `tools` directory within each agent's folder:

```python
# Example of a custom tool
from google.adk.tools import Tool

def get_weather(location: str) -> dict:
    """Get current weather for a location.
    
    Args:
        location: City name or coordinates
        
    Returns:
        Weather data including temperature, conditions, etc.
    """
    # Implementation
    return {"temperature": 25, "conditions": "sunny"}

# Register as an ADK tool
get_weather_tool = Tool(
    function=get_weather,
    description="Get current weather conditions for a location"
)
```

## Code Generation Guidelines

When suggesting code for this repository:

1. **Reference Official Examples First**: Always base suggestions on patterns found in `adk-python/`, `adk-docs/`, and `adk-samples/` directories.
2. **Maintain Consistency**: Follow established conventions observed in the reference directories.
3. **Agent Design**: When implementing agent logic, structure code according to samples in `adk-samples/python/agents/` and existing agents in this project.
4. **Tool Creation**: For custom tools, reference implementations in `adk-python/src/google/adk/tools/` and existing tools in this project.
5. **Documentation**: For docstrings and comments, follow the style in existing ADK code.
6. **Multi-Agent Patterns**: When working with multiple agents, follow the orchestration patterns established in the project.

Following these patterns will ensure code suggestions align with the project's established architecture and conventions.
