import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize Tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# 2. Define Agents
researcher = Agent(
    role='Lead Research Analyst',
    goal='Find recent news and professional achievements for {prospect_name} at {company_name}',
    backstory='You are an expert at finding deep insights from LinkedIn and company blogs.',
    tools=[search_tool, scrape_tool],
    verbose=True
)

writer = Agent(
    role='Sales Personalization Expert',
    goal='Draft a short, 3-sentence LinkedIn message that mentions a specific research insight',
    backstory='You hate spam. You write messages that feel human, professional, and high-value.',
    verbose=True
)

# 3. Define Tasks
research_task = Task(
    description='Search for {prospect_name} from {company_name}. Find one specific recent achievement or company milestone.',
    agent=researcher,
    expected_output='A summary of one key professional insight about the prospect.'
)

outreach_task = Task(
    description='Using the research, draft a LinkedIn connection request. Do NOT use "I hope this finds you well".',
    agent=writer,
    expected_output='A personalized 3-sentence outreach message.'
)

# 4. Assemble the Crew
sdr_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, outreach_task]
)

# 5. Kickoff
if __name__ == "__main__":
    result = sdr_crew.kickoff(inputs={'prospect_name': 'Satya Nadella', 'company_name': 'Microsoft'})
    print("\n\n########################")
    print("## PERSONALIZED MESSAGE ##")
    print("########################\n")
    print(result)
