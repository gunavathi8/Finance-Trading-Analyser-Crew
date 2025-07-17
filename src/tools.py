from crewai.tools import BaseTool
import yfinance as yf

class YFinanceTool(BaseTool):
    name: str = "YFinance Tool"
    description: str = "Fetches detailed financial data (price, range, P/E, volatility, beta, moving averages) for a stock ticker."

    def _run(self, ticker: str) -> dict:
        try:
            stock = yf.Ticker(ticker)
            hist_data = stock.history(period="200d")
            hist_30d = stock.history(period="30d")
            if hist_data.empty or hist_30d.empty:
                raise ValueError("Insufficient historical data")
            return {
                "current_price": stock.history(period="1d")["Close"].iloc[-1],
                "range_52w": stock.info["52_week_range"],
                "pe_ratio": stock.info.get("trailing_pe", "N/A"),
                "volatility_30d": hist_30d["Close"].pct_change().std() * 100,
                "beta": stock.info.get("beta", "N/A"),
                "ma_20d": hist_data["Close"].rolling(window=20).mean().iloc[-1],
                "ma_50d": hist_data["Close"].rolling(window=50).mean().iloc[-1],
                "error": None
            }
        except Exception as e:
            return {"error": f"Failed to fetch data for {ticker}: {str(e)}"}