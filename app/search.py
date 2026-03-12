#app/search.py
"""
Purpose: Handles web search using Tavily API.
Responsibility: User Query → Tavily API → return URLs
Example output:
[
 "https://site1.com/article",
 "https://site2.com/article"
]
Concept: API-based retrieval
"""

import os
from tavily import TavilyClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Initialize Tavily client
client = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query, max_results=5):
    """
    Search the web using Tavily API.

    Parameters
    ----------
    query : str
        User research question
    max_results : int
        Number of URLs to return

    Returns
    -------
    list
        List of article URLs
    """

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=max_results
    )

    urls = []

    for result in response["results"]:
        urls.append(result["url"])

    return urls