from langchain_openai import ChatOpenAI
from crewai import Agent

def create_agents():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    tools = []

    data_analyst_agent = Agent(
        role="Data Analyst",
        goal="Analyze financial data for the selected stock",
        backstory="A skilled data analyst with expertise in financial markets, capable of extracting and interpreting stock data.",
        llm=llm,
        tools=tools
    )

    trading_strategy_agent = Agent(
        role="Trading Strategy Developer",
        goal="Develop trading strategies based on analyzed data",
        backstory="An experienced trader who designs effective strategies using technical indicators and market trends.",
        llm=llm
    )

    execution_agent = Agent(
        role="Execution Planner",
        goal="Plan the execution of trading strategies",
        backstory="A meticulous planner who optimizes trade execution timing and pricing.",
        llm=llm
    )

    risk_management_agent = Agent(
        role="Risk Manager",
        goal="Assess and mitigate risks for the trading strategies",
        backstory="A risk expert who evaluates market risks and develops mitigation strategies.",
        llm=llm
    )

    report_generator_agent = Agent(
        role="Report Generator",
        goal="Compile a comprehensive financial trading analysis report",
        backstory="A detail-oriented report writer who synthesizes data, strategies, plans, and risks into a structured document.",
        llm=llm
    )

    return {
        "data_analyst": data_analyst_agent,
        "trading_strategy": trading_strategy_agent,
        "execution": execution_agent,
        "risk_management": risk_management_agent,
        "report_generator": report_generator_agent
    }