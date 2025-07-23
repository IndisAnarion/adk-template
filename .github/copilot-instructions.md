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
- **agents/**: Your customized agent implementations (currently empty)

## Key Components

### Core Abstractions

- **Agent**: The blueprint defining an agent's identity, instructions, and tools
- **Tool**: A capability function an agent can call to interact with the world
- **Runner**: The orchestration engine managing the "Reason-Act" loop
- **Session**: Holds conversation state for a single dialogue
- **Memory**: Long-term recall across different sessions

### Canonical Project Structure

```
my_agent/
├── __init__.py   # Must contain: from . import agent
└── agent.py      # Must contain: root_agent = Agent(...)
```

## Development Workflow

### Creating a New Agent

1. Create a directory within `agents/` following the structure above
2. Define your agent in `agent.py` with `root_agent = Agent(...)`
3. Import required tools from `google.adk.tools` or create custom tools

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

### Testing & Debugging

1. **Interactive UI**: Run `adk web` and navigate to the web interface
2. **CLI**: Use `adk run` for quick terminal tests
3. **Programmatic**: Write tests with `pytest` for automated testing

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

## Versioning

The project follows Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH). Breaking changes (requiring a MAJOR version bump) include:
- API signature changes
- Architectural shifts
- Data schema changes
- Tool interface changes
- Configuration changes
- Wire format changes
- Dependency removals

Commit messages follow [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) format with `#breaking` or `#non-breaking` tags.

## Code Generation Guidelines

When suggesting code for this repository:

1. **Reference Official Examples First**: Always base suggestions on patterns found in `adk-python/`, `adk-docs/`, and `adk-samples/` directories.
2. **Maintain Consistency**: Follow established conventions observed in the reference directories.
3. **Agent Design**: When implementing agent logic, structure code according to samples in `adk-samples/python/agents/`.
4. **Tool Creation**: For custom tools, reference implementations in `adk-python/src/google/adk/tools/`.
5. **Documentation**: For docstrings and comments, follow the style in existing ADK code.

Following these patterns will ensure code suggestions align with the project's established architecture and conventions.
