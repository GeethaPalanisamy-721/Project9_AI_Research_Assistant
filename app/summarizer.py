# app/summarizer.py
"""
Purpose: Use a Hugging Face transformer model to summarize content.
Responsibility: long article text → short summary (2000 word article into 4-5 lines summary)
Concept: NLP inference pipeline
"""

from transformers import pipeline

# Load summarization model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def summarize_text(text, max_length=150):

    """
    Summarize long text using a transformer model.

    Parameters
    ----------
    text : str
        Article content

    max_length : int
        Maximum summary length

    Returns
    -------
    str
        AI-generated summary
    """

    # Transformers cannot handle extremely long text
    text = text[:4000]

    summary = summarizer(
        text,
        max_length=max_length,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]