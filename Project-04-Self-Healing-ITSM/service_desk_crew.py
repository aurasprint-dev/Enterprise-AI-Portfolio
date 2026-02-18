import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()

# 1. Define Agents
triager = Agent(
  role='Senior IT Support Triage',
  goal='Correctly identify the technical issue from a user ticket',
  backstory='You are an expert at understanding technical complaints and categorizing them.',
  verbose=True,
  allow_delegation=False
)

engineer = Agent(
  role='Automation Engineer',
  goal='Write a safe Python script to resolve the identified IT issue',
  backstory='You are a master of Python and PowerShell automation with a focus on system safety.',
  verbose=True,
  allow_delegation=False
)

# 2. Define Tasks
triage_task = Task(
  description='Analyze this ticket: "My computer is running slow and the C: drive is almost full."',
  agent=triager,
  expected_output='A clear identification of the technical problem.'
)

repair_task = Task(
  description='Based on the triage, write a Python script to clean up temporary files safely.',
  agent=engineer,
  expected_output='A functional Python script that identifies and deletes temporary files.'
)

# 3. Form the Crew
it_crew = Crew(
  agents=[triager, engineer],
  tasks=[triage_task, repair_task],
  process=Process.sequential # Task 1 must finish before Task 2 starts
)

# 4. Execute
if __name__ == "__main__":
    result = it_crew.kickoff()
    print("\n\n########################")
    print("## RESOLUTION PLAN ##")
    print("########################\n")
    print(result)
