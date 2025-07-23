# ADK Template Project

This repository is a template for creating agent applications using Google's Agent Development Kit (ADK).

## Quick Start Guide

Follow these steps to set up and run your agent application:

### 1. Install Dependencies

Follow these steps to set up the project:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/adk-template.git
cd adk-template

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# 4. Install requirements
pip install -r requirements.txt
```

This will install:
- google-adk: The Agent Development Kit
- litellm: Library for working with multiple LLM providers

### 2. Project Structure

The project follows the ADK canonical project structure:

```
adk-template/
├── agents/
│   ├── agent.py          # Main orchestrator agent
│   ├── prompt.py         # Agent prompts and instructions
│   └── sub_agents/       # Specialized sub-agents
│       ├── bi/           # Business Intelligence agent
│       └── employee/     # Employee operations agent
```

### 3. Agent Implementation

The main agent is defined in `agents/agent.py` and orchestrates multiple specialized sub-agents:

```python
from google.adk.agents import Agent
from agents import prompt
from agents.sub_agents.bi import root_agent as bi_agent
from agents.sub_agents.employee import root_agent as employee_agent

def create_orchestrator() -> Agent:
    """Create the main orchestrator agent with BI and Employee sub-agents."""
    return Agent(
        model="gemini-2.0-flash-001",
        name="root_agent",
        description="System orchestrator managing BI and Employee operations through specialized sub-agents",
        instruction=prompt.ROOT_AGENT_INSTRUCTION,
        sub_agents=[
            bi_agent,
            employee_agent,
        ],
    )

root_agent = create_orchestrator()
```

### 4. Interactive Development

Use the interactive web UI for development:

```bash
# Start the ADK web server
adk web

# Then open your browser at http://localhost:8080
```

This provides a chat interface, function call visualization, and event tracing for debugging.


## Development Resources

- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Python GitHub](https://github.com/google/adk-python)
- [ADK Samples](https://github.com/google/adk-samples)

For AI development guidelines, refer to `.github/copilot-instructions.md`
