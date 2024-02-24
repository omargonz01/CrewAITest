from crewai import Agent, Task, Crew, Process
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

researcher = Agent(
    role='Researcher',
    goal="Research new crypto games",
    backstory='You are an AI crypto gaming research assistant.',
    verbose=True,
    allow_delegation=False
)

investor = Agent(
    role="Investor",
    goal="Invest based on the research",
    backstory="You are an AI investor who specializes in crypto gaming investments",
    verbose=True,
    allow_delegation=False
)

task1 = Task(description='Investigate the latest crypto games', agent=researcher)
task2 = Task(description='Invest based on the research', agent=investor)

crew = Crew(
    agents=[researcher, investor],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

results = crew.kickoff()
