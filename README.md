# AI Multi-Agent Research Assistant

A lightweight **Multi-Agent AI System** built in Python using the **Groq API**. The project demonstrates how multiple AI agents can collaborate to solve a user query through **planning**, **research**, and **summarization**, while optimizing **token usage**, **execution time**, and **API cost**.

---

## Features

- Multi-Agent Architecture
- Planner Agent for task decomposition
- Research Agent for detailed information gathering
- Summary Agent for concise final output
- Prompt Engineering
- Context Compression for token optimization
- Token Usage Tracking
- API Cost Estimation
- Execution Time Monitoring
- Robust Error Handling
- Logging
- Unit Testing with Pytest
- GitHub Actions CI/CD Pipeline

---

## Project Structure

```
AI-Agent-Assignment/
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── planner_agent.py
│   ├── research_agent.py
│   └── summary_agent.py
│
├── llm/
│   ├── __init__.py
│   └── groq_client.py
│
├── prompts/
│   ├── planner_prompt.txt
│   ├── research_prompt.txt
│   └── summary_prompt.txt
│
├── utils/
│   ├── __init__.py
│   ├── context_optimizer.py
│   ├── helpers.py
│   ├── logger.py
│   ├── parser.py
│   └── token_counter.py
│
├── tests/
│   ├── __init__.py
│   ├── test_context_optimizer.py
│   ├── test_parser.py
│   └── test_token_counter.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── test_pipeline.py
├── .gitignore
├── .env
└── README.md
```

---

# Architecture

```
                 User Query
                      │
                      ▼
             Planner Agent
                      │
          Generates Execution Plan
                      │
                      ▼
          Context Optimization
                      │
                      ▼
             Research Agent
                      │
        Detailed Research Output
                      │
                      ▼
          Context Optimization
                      │
                      ▼
             Summary Agent
                      │
                      ▼
             Final Summary
```

---

# Technologies Used

- Python 3.10+
- Groq API
- python-dotenv
- tiktoken
- Pytest
- GitHub Actions

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move inside the project

```bash
cd AI-Agent-Assignment
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

---

# Running the Project

Execute the complete pipeline

```bash
python test_pipeline.py
```

---

# Running Unit Tests

```bash
pytest
```

Expected output

```
==========================
7 passed
==========================
```

---

# Multi-Agent Workflow

### Planner Agent

- Understands the user's request.
- Breaks it into logical tasks.
- Returns structured JSON.

### Research Agent

- Receives optimized tasks.
- Performs detailed research.
- Generates comprehensive information.

### Summary Agent

- Produces a concise summary.
- Preserves the important information.
- Minimizes unnecessary tokens.

---

# Token Optimization Strategy

The project minimizes API cost by:

- Restricting the planner to exactly five tasks.
- Compressing execution plans before research.
- Compressing research output before summarization.
- Reducing redundant context passed between agents.
- Tracking token usage for every API call.

---

# Debugging Methodology

The project includes robust error handling:

- Empty prompt validation
- Invalid JSON detection
- API exception handling
- Graceful failure handling
- Structured logging
- Parser validation

---

# Logging

Execution logs include:

- Agent Name
- Input Tokens
- Output Tokens
- Execution Time
- Success/Error Status

---

# Cost Estimation

The system estimates API usage cost using:

- Input Tokens
- Output Tokens
- Model Pricing

This helps monitor and optimize API expenses.

---

# Testing

Unit tests cover:

- JSON Parser
- Context Optimizer
- Token Counter

All tests pass successfully using Pytest.

---

# CI/CD

GitHub Actions automatically:

- Installs project dependencies
- Executes all unit tests
- Verifies every push and pull request

---

# Sample Output

```
STEP 1 : PLANNING
✔ Execution Plan Generated

STEP 2 : RESEARCH
✔ Detailed Research Completed

STEP 3 : SUMMARY
✔ Final Summary Generated

TOTAL TOKEN USAGE
Input Tokens : 609
Output Tokens : 1014
Grand Total : 1623

COST ESTIMATION
Total Cost : £0.00011157

EXECUTION TIME
Total Time : 3.81 sec
```

---

# Future Enhancements

- Add Web Search Integration
- Introduce Additional Specialized Agents
- Memory-Based Context Retention
- Parallel Agent Execution
- Interactive Web Interface
- Support for Multiple LLM Providers

---

# Author

**Abhay Bhadauria**

B.Tech Graduate | Software Developer | AI & Full Stack Enthusiast
