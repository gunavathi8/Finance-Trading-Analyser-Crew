# Financial Trading Analysis Tool

A modular AI-powered tool for generating financial trading analysis reports using CrewAI and Streamlit.

## Features
- Analyzes stock data (price, volatility, moving averages, etc.) for user-selected stocks.
- Develops trading strategies with entry/exit points and risk management.
- Provides a web interface via Streamlit for easy interaction.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-trading-analysis.git
   cd financial-trading-analysis

2. Install dependencies:
   pip install -r requirements.txt

3. Set up environment variables (e.g., OpenAI API key) in a .env file.

4. Run the Streamlit app:
   streamlit run src/app.py

## Usage
- Enter stock symbol, capital, and preferences in the web interface.
- Click "Generate Report" to view the analysis.

## Notes
- API Key: Add your OpenAI API key to a .env file (e.g., OPENAI_API_KEY=your_key) and load it in agents.py if needed.
- Real-Time Data: As of 07:16 PM IST, July 17, 2025, expect GOOGL ~$183.00, XLF ~$52.60 (based on recent trends).
- Debugging: Use verbose=True in crew.py to track issues. If the JSON error persists, check financial_trading_inputs alignment.


