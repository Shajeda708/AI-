from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from tools import search_tool, wiki_tool, save_tool

from langgraph.graph import StateGraph, END
from typing import TypedDict, List

load_dotenv()

# -----------------------------
# Pydantic output
# -----------------------------
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: List[str]
    tools_used: List[str]


class AgentState(TypedDict):
    query: str
    result: str


# -----------------------------
# LLM
# -----------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Supported Groq model
    temperature=0.2,
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         """
You are a highly knowledgeable research agent designed to gather, analyze, and summarize information in a clear, detailed, and accurate way.

Your goals:
1. Fully understand the user's query.
2. Use tools to gather data when helpful (Wikipedia, search, etc.).
3. Combine tool data with your reasoning to produce a rich, detailed research summary.
4. Provide ONLY a JSON output that matches the specified Pydantic schema exactly.

Your research summary MUST:
- Explain the topic in depth.
- Include background information, key concepts, examples.
- Add important facts, statistics, or historical information.
- Describe benefits, limitations, and modern relevance.
- Cite every source URL or tool result used.
- Ensure the final output is valid JSON and contains no text outside JSON.

STRICTLY follow this JSON structure (escaped so it's treated as literal text):

{{
    "topic": "...",
    "summary": "...",
    "sources": ["...", "..."],
    "tools_used": ["...", "..."]
}}

{format_instructions}
         """
        ),
        ("human", "{query}"),
    ]
).partial(format_instructions=parser.get_format_instructions())



# -----------------------------
# Node: LLM reasoning with real tools
# -----------------------------
def llm_node(state: AgentState):
    query = state["query"]

    # Real tools usage
    wiki_summary = wiki_tool(query)
    search_result = search_tool(query)

    tools_used = ["Wikipedia Lookup", "Web Search"]
    sources = [
        f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}",
        f"Search: {query}"
    ]

    # Prepare prompt for LLM with retrieved tool data
    formatted = prompt.invoke({
        "query": f"{query}\n\nWikipedia Summary: {wiki_summary}\nSearch Result: {search_result}"
    })

    # LLM generates final response
    response = llm.invoke(formatted)

    return {"result": response.content}


# -----------------------------
# Graph
# -----------------------------
workflow = StateGraph(AgentState)
workflow.add_node("llm", llm_node)
workflow.set_entry_point("llm")
workflow.add_edge("llm", END)
app = workflow.compile()


# -----------------------------
# Run agent
# -----------------------------
query = input("What can I help you research? ")

out = app.invoke({"query": query})

try:
    # Parse LLM JSON output
    formatted = parser.parse(out["result"])
    print("\n✔ FINAL STRUCTURED OUTPUT:\n", formatted)

    # Save output to file
    save_tool(str(formatted), filename="researchoutput.txt")
    print("\n✅ Research output saved to researchoutput.txt")

except Exception as e:
    print("❌ Could not parse output:", e)
    print("RAW:", out["result"])