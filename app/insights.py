#app/insights.py
"""
Purpose:Convert the summary into structured insights.
Responsibility: summary → key points (bullets, highligts, recommendations)
Concept: post processed AI output
"""

def generate_insights(summary):
    """
    Convert a summary into structured insights.
    """

    # Split summary into sentences
    sentences = summary.split(".")

    insights = []

    for s in sentences:
        s = s.strip()

        if len(s) > 20:
            insights.append("• " + s)

    return "\n".join(insights[:5])