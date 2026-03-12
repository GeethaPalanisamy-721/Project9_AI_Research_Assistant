# app/extractor.py
"""Purpose: Extract readable text from web pages.
Responsibility: URL → download HTML → extract article text
Tools used: requests, BeautifulSoup
Concept:Web scraping and data ingestion
"""

import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts and styles
        for script in soup(["script", "style"]):
            script.extract()

        # Get visible text
        text = soup.get_text(separator=" ")

        # Clean whitespace
        text = " ".join(text.split())

        return text

    except Exception as e:
        print(f"Error extracting {url}: {e}")
        return ""