from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="web_search_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions using Google Search.",
    instruction="""Answer the questions by searching the internet with using google_search.
    
    Always include the source links from your search results to support your answers. Each claim or piece of information 
    should be properly attributed to its source with a link. Format citations as [Source: title (link)] at the end of each 
    relevant statement.

    Never provide information without corresponding citation links, as this ensures users can verify the information and 
    explore topics further. Organize your response with clear attribution to maintain credibility.""",
    tools=[google_search]
)