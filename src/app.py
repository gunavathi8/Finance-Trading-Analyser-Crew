import streamlit as st
from .crew import create_crew

st.title("Financial Trading Analysis Tool")

# Input form
with st.form(key="trading_inputs"):
    stock_selection = st.text_input("Stock Symbol (e.g., AAPL, XLF)", value="GOOGL")
    initial_capital = st.number_input("Initial Capital ($)", value=100000, step=1000)
    risk_tolerance = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"], index=1)
    trading_strategy_preference = st.selectbox("Trading Strategy Preference", ["Day Trading", "Swing Trading", "Sector Rotation"], index=1)
    news_impact_consideration = st.checkbox("Consider News Impact", value=True)
    time_horizon = st.number_input("Time Horizon (days)", value=60, step=30)
    portfolio_size = st.number_input("Portfolio Size ($)", value=750000, step=10000)
    submit_button = st.form_submit_button(label="Generate Report")

# Generate report
if submit_button:
    inputs = {
        'stock_selection': stock_selection,
        'initial_capital': str(initial_capital),
        'risk_tolerance': risk_tolerance,
        'trading_strategy_preference': trading_strategy_preference,
        'news_impact_consideration': news_impact_consideration,
        'time_horizon': str(time_horizon),
        'portfolio_size': str(portfolio_size)
    }
    with st.spinner("Generating report..."):
        result = create_crew(inputs)
        st.success("Report generated successfully!")
        st.text(result)