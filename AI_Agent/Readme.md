## AI Research Agent
An intelligent research assistant is built by using LangGraph and Groq's LLaMA 3.3 that give answer to the user query and automatically gathers information from Wikipedia and web search, then generates structured research summaries.
## Overview
This AI Research Agent is an autonomous system that:

- Takes a research topic from the user
- Fetches information from Wikipedia
- Performs web searches (simulated for demo)
- Uses Groq's LLaMA 3.3 70B model to synthesize findings
- Outputs structured JSON results with sources
- Saves the research to a text file

The agent uses LangGraph for workflow orchestration, LangChain for LLM interaction, and Pydantic for data validation.
## Features

- Multi-Source Research: Combines Wikipedia and web search results
- Structured Output: Returns validated JSON with topic, summary, sources, and tools used
- Error Handling: Gracefully handles API failures and network issues
- Automatic Saving: Saves research output to a text file
- Type Safety: Uses Pydantic models for data validation
- Workflow Management: LangGraph orchestrates the research pipeline
- Fast Inference: Powered by Groq's optimized LLM infrastructure
## Installation & Setup
- Install Python version 3.8+ (3.12 recommended)
- Create Virtual Environment in your project folder
- Activate the virtual environment
- when virtual environment is activated install all the requirements(pip install -r requirements.txt)
- create a .env file
- get your api key from groq and place it in .env file(GROQ_API_KEY=your_groq_api_key_here
)
## How to Run the Agent
- simply run your main.py file(python main.py)
## How It Works

- User Input
    User enters a research topic via command line
    Example: "Artificial Intelligence"

- State Initialization
    LangGraph creates initial state: {"query": "Artificial Intelligence", "result": ""}

- Tool Execution (llm_node)
    Wikipedia Lookup: Fetches summary from Wikipedia REST API
    Web Search: Returns search results (currently simulated)
    Metadata collected: tools used, source URLs

- Prompt Construction
    Combines user query + Wikipedia summary + search results
    Adds JSON schema instructions for structured output
    Creates formatted prompt for LLM

- LLM Processing
    Sends prompt to Groq's LLaMA 3.3 70B model
    Temperature set to 0.2 for focused, factual responses
    LLM generates structured JSON response

- Output Parsing
    Pydantic parser validates JSON structure
    Ensures all required fields present (topic, summary, sources, tools_used)
    Converts to ResearchResponse object

- Output Delivery
    Displays structured output to console
    Saves to researchoutput.txt file
    User receives confirmation
[Ai_Agent_output](https://github.com/Shajeda708/AI-/blob/main/AI_Agent/Images/Screenshot1.png)
## screenshots
[AI_Agent](./Images/screenshot1.png)
[AI_Agent](./Images/screenshot2.png)
