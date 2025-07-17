# 💹 Financial Trading Analysis Crew 🚀

A modular, AI-powered multi-agent tool that delivers **real-time trading insights and strategic reports** using **CrewAI**, **OpenAI**, **yFinance**, and **Streamlit**.
---

## 📈 Stock Analysis ![stock-icon](G:\My_GitHub_Projects\CrewAI_Projects\Multi_Agent_Financial_Trading_Analysis\diagram.png)
Our crew-based system analyzes real-time stock data using `yFinance` and provides strategic trading decisions via multiple AI agents.

---

## ⚙️ Features
- 🔍 Analyze stock data: price, volatility, moving averages, RSI, etc.
- 📊 Generate trade strategies: entry/exit points, stop-loss, and risk profiling.
- 👥 Multi-agent architecture: Data Analyst, Trading Strategist, Risk Manager, Execution Planner, and Report Generator.
- 🌐 Intuitive UI: Built with Streamlit for ease of use and accessibility.
- 🧠 Powered by OpenAI and CrewAI for LLM-based reasoning and task delegation.

---


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gunavathi8/Finance-Trading-Analyser-Crew.git
   cd Finance-Trading-Analyser-Crew

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Set up environment variables (e.g., OpenAI API key) in a .env file.
   ```bash
   OPENAI_API_KEY="your_openai_key_here"

4. Run the Streamlit app:
   ```bash
   streamlit run src/app.py

---   

## 🧪 Usage
- 📥 Enter stock symbol (e.g., AAPL, GOOGL) and capital in the Streamlit UI.

- ⚙️ Agents will analyze the stock and generate a detailed trading report.

- 📤 Click "Generate Report" to view insights, risk scores, and strategy.

---

## 🧠 Architecture Overview
- Frontend: Streamlit (user inputs)

- Backend CrewAI Agents:

  - 👩‍💼 Data Analyst

  - 📈 Trading Strategist

  - 📉 Risk Manager

  - 🤖 Execution Planner

  - 📄 Report Generator

- Tooling: yFinance for real-time stock data, OpenAI for LLM reasoning

## 📝 Notes
- 🔑 API Key: Required in .env file → OPENAI_API_KEY=your_key_here

- 📆 Real-Time Tip (as of July 17, 2025):

  - GOOGL ≈ $183.00

  - XLF ≈ $52.60

- 🐛 Debugging:

  - Set verbose=True in src/crew.py for logs

  - Check structure of financial_trading_inputs if JSON parsing fails

## 🤝 Contributions & Future Ideas
- Add backtesting engine

- Integrate more data sources (e.g., news sentiment)

- Add visualization charts in reports

- Improve agent reasoning trace

## 📄 License
MIT


