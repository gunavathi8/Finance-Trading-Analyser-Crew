from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from time import sleep
from openai import RateLimitError
from .tools import YFinanceTool
from .agents import create_agents
from .tasks import create_tasks

def create_crew(inputs):
    agents = create_agents()
    tools = [YFinanceTool()]
    tasks = create_tasks(agents, tools)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
        process=Process.hierarchical,
        verbose=True,
        max_rpm=5,
        max_iterations=10
    )

    # Execute with retry logic
    max_retries = 5
    for attempt in range(max_retries):
        try:
            result = crew.kickoff(inputs=inputs)
            return result
        except RateLimitError:
            wait_time = 2 ** attempt
            print(f"Rate limit hit. Retrying in {wait_time} seconds... (Attempt {attempt + 1}/{max_retries})")
            sleep(wait_time)
        except Exception as e:
            print(f"Error occurred: {str(e)}. Retrying in {wait_time} seconds... (Attempt {attempt + 1}/{max_retries})")
            sleep(wait_time)
    else:
        raise Exception("Max retries reached. Check API quota or contact OpenAI support.")