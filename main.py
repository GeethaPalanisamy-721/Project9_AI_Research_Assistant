# main.py
"""
Orchestration layer
Streamlit interface which take user input, trigger the pipeline,display results
So workflow inside main.py
User query- search- extract- summarize-insights-output display
"""
import streamlit as st

from app.search import search_web
from app.extractor import extract_text_from_url
from app.summarizer import summarize_text
from app.insights import generate_insights


st.title("AI Research Assistant")

st.write("Ask a research question and get summarized insights from multiple web sources.")

query = st.text_input("Enter your research question:")

if st.button("Run Research"):

    if query:

        # Pipeline status display
        st.subheader("Pipeline Status")
        status = st.empty()

        # Step 1 — Search
        status.write("Step 1: Searching the web...")
        urls = search_web(query)

        # Source citation
        st.subheader("Sources")
        for i, url in enumerate(urls[:3], start=1):
            st.markdown(f"{i}. [{url}]({url})")

        # Step 2 — Extraction
        status.write("Step 2: Extracting article content...")

        combined_text = ""

        for i, url in enumerate(urls[:3], start=1):

            try:
                article_text = extract_text_from_url(url)

                combined_text += f"\n\nARTICLE {i} SOURCE: {url}\n"
                combined_text += article_text

            except Exception as e:
                st.warning(f"Could not extract content from {url}")

        # Step 3 — Summarization
        status.write("Step 3: Generating summary...")
        summary = summarize_text(combined_text)

        st.subheader("Summary")
        st.write(summary)

        # Step 4 — Insights
        status.write("Step 4: Extracting key insights...")
        insights = generate_insights(summary)

        st.subheader("Key Insights")
        st.write(insights)

        # Completion
        status.success("Research completed.")

    else:
        st.warning("Please enter a research question.")