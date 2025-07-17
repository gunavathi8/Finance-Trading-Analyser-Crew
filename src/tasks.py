from crewai import Task

def create_tasks(agents, tools):
    data_analysis_task = Task(
        description=(
            "Analyze market data for {stock_selection} by collecting: "
            "1) Current price, 2) 52-week high/low, 3) P/E ratio, 4) 30-day volatility, 5) 20-day and 50-day moving averages via YFinance Tool, "
            "6) News summary via SerperDevTool."
        ),
        expected_output=(
            "JSON object with: 1) current_price (USD), 2) range_52w (USD), 3) pe_ratio, 4) volatility_30d (%), "
            "5) ma_20d and ma_50d (USD), 6) news_summary (list of 3-5 key points)."
        ),
        agent=agents["data_analyst"],
        tools=tools
    )

    strategy_development_task = Task(
        description=(
            "Develop 3 trading strategies for {stock_selection} using Data Analyst’s report, "
            "aligning with {risk_tolerance} and {trading_strategy_preference}. "
            "Use current price, 20-day, 50-day moving averages, and 30-day volatility to set entry/exit points."
        ),
        expected_output="3 strategies with specific entry/exit points (e.g., $185/$180), position sizing (e.g., 30% of $100,000), and stop-loss %.",
        agent=agents["trading_strategy"],
        context=[data_analysis_task]
    )

    execution_planning_task = Task(
        description=(
            "Plan execution for {stock_selection} strategies, specifying timing (e.g., 9:30 AM EST market open, post-earnings), "
            "pricing (e.g., limit orders 2% above current price), and order types (e.g., limit, market, stop-limit)."
        ),
        expected_output="Execution plans with specific timing, order types, and pricing for each strategy.",
        agent=agents["execution"],
        context=[strategy_development_task]
    )

    risk_assessment_task = Task(
        description=(
            "Evaluate risks for {stock_selection} using aggregated data. Calculate beta and 1-day VaR (95% confidence) via YFinance Tool. "
            "Provide inputs for the report generator."
        ),
        expected_output="Report with: 1) Risks (including beta and VaR), 2) Mitigation (specific actions).",
        agent=agents["risk_management"],
        context=[data_analysis_task, strategy_development_task, execution_planning_task]
    )

    report_generation_task = Task(
        description=(
            "Compile a comprehensive 'Financial Trading Analysis Report for {stock_selection}' using inputs from all agents. "
            "Include: 1) Executive Summary, 2) Market and Company Overview, 3) Risks, 4) Trading Strategies, 5) Execution Plans, 6) Mitigation."
        ),
        expected_output="Full text of 'Financial Trading Analysis Report for {stock_selection}' with all sections.",
        agent=agents["report_generator"],
        context=[data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task]
    )

    return [
        data_analysis_task,
        strategy_development_task,
        execution_planning_task,
        risk_assessment_task,
        report_generation_task
    ]