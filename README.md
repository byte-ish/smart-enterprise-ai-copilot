# Smart Enterprise AI Copilot

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.110.0-green.svg)](https://fastapi.tiangolo.com/)  
[![Poetry](https://img.shields.io/badge/Poetry-v1.8.2-purple.svg)](https://python-poetry.org/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Overview

**Smart Enterprise AI Copilot** is a modular, production-grade AI agent orchestration platform designed to streamline complex enterprise workflows.  
It leverages modern Python tooling, LangGraph orchestration, memory systems, and tool integrations to enable intelligent, multi-agent collaboration.

---

## Architecture

```mermaid
graph TD
  User[User Input]
  UserProxyAgent[User Proxy Agent]
  TaskPlanner[Task Planner Agent]
  Retriever[Retriever Agent (RAG)]
  ToolExecutor[Tool Executor Agent]
  MemoryManager[Memory Manager]
  LLMRouter[LLM Router]
  ExternalTools[External APIs (Jira, Outlook, etc.)]

  User --> UserProxyAgent
  UserProxyAgent --> TaskPlanner
  TaskPlanner --> Retriever
  Retriever --> MemoryManager
  Retriever --> LLMRouter
  LLMRouter --> ToolExecutor
  ToolExecutor --> ExternalTools
  MemoryManager --> UserProxyAgent
```
## Key Features

- Multi-Agent Architecture: Decompose workflows into specialized AI agents  
- Retrieval-Augmented Generation (RAG): Contextual knowledge search using vector DBs  
- Memory Management: Persistent and session memory with Redis and Chroma  
- Tool Integrations: Native connectors for Jira, Outlook, and enterprise APIs  
- Production-Ready API: FastAPI service with structured logging, error handling, and observability  
- Configurable & Extensible: YAML-based agent configs and pluggable components  

---

## Technology Stack

| Component            | Technology                   |
|----------------------|-----------------------------|
| Programming Language  | Python 3.12                 |
| API Framework        | FastAPI                    |
| Dependency Manager    | Poetry                     |
| Orchestration         | LangGraph                  |
| Memory Storage        | Redis, ChromaDB            |
| Vector Search         | Chroma / Weaviate          |
| LLM Providers         | OpenAI, Ollama, HuggingFace |
| Logging               | Loguru                     |
| Configuration         | Pydantic, python-dotenv    |
| Testing               | Pytest, httpx              |
| Containerization      | Docker, Kubernetes (Helm)  |

---

## Getting Started

### Prerequisites

- Python 3.12  
- Poetry  
- Redis (if running memory locally)  
- Docker (optional)  

### Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/smart-enterprise-ai-copilot.git
cd smart-enterprise-ai-copilot
```

⸻

	2.	Install dependencies with Poetry

poetry install

	3.	Activate the Poetry virtual environment

poetry shell

	4.	Run the FastAPI server

uvicorn smart_enterprise_ai_copilot.api.main:app --reload

	5.	Access the health check endpoint

http://localhost:8000/health


⸻

## Development

- Add agents inside `smart_enterprise_ai_copilot/agents/`
- Add tool integrations inside `smart_enterprise_ai_copilot/tools/`
- Define orchestration graphs in `smart_enterprise_ai_copilot/graph/`
- Configuration managed via `smart_enterprise_ai_copilot/config/settings.py` and `.env` files
- Unit and integration tests live in `smart_enterprise_ai_copilot/tests/`

## Contributing

Contributions are welcome! Please open issues and pull requests for bug fixes, features, or documentation improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

