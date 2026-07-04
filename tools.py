from dotenv import load_dotenv
from tavily import TavilyClient
import os
import re

# ----------------------------
# LOAD ENVIRONMENT VARIABLES
# ----------------------------
load_dotenv()

# ----------------------------
# TAVILY CLIENT
# ----------------------------
tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

# ----------------------------
# LIVE TREND SEARCH
# ----------------------------
def trend_search(query):

    # Extract topic from the user's query
    match = re.search(r"trending\s+in\s+(.+)", query, re.IGNORECASE)

    if match:
        topic = match.group(1).strip()
    else:
        topic = query.strip()

    try:

        response = tavily.search(
            query=f"Latest research trends in {topic}",
            search_depth="advanced",
            max_results=5
        )

        output = f"\n🌐 Latest Research Trends in {topic.upper()}\n\n"

        for i, result in enumerate(response["results"], 1):

            output += f"{i}. {result['title']}\n"
            output += f"   {result['url']}\n\n"

        return output

    except Exception as e:
        return f"❌ Error while fetching trends:\n{e}"