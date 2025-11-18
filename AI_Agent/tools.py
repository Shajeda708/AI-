# tools.py
import requests

def search_tool(query: str) -> str:
    """
    Simulated web search tool.
    Currently returns a placeholder result for demonstration.
    Later, you can integrate real Google/Bing API.
    """
    # For now, just return a placeholder snippet
    return f"Top search result for '{query}' (simulated)"

def wiki_tool(topic: str) -> str:
    """
    Fetch summary from Wikipedia for the given topic.
    Uses Wikipedia REST API.
    """
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            return data.get("extract", "No summary found")
        return "Wikipedia page not found"
    except Exception as e:
        return f"Error fetching Wikipedia: {e}"

def save_tool(data: str, filename="researchoutput.txt") -> None:
    """
    Save research output to a text file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)
    except Exception as e:
        print(f"Error saving file '{filename}': {e}")
