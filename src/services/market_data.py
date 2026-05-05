import yfinance as yf
from datetime import datetime, timedelta


def get_portfolio_performance(portfolio):
    """
    Calculates portfolio return based on historical price data.
    Assumes 'value' is current investment amount.
    """

    if not portfolio:
        return {
            "total_return_pct": 0.0,
            "annualized_return_pct": 0.0
        }

    total_current_value = sum(p["value"] for p in portfolio)

    total_past_value = 0

    for p in portfolio:
        ticker = p["ticker"]
        current_value = p["value"]

        try:
            stock = yf.Ticker(ticker)

            hist = stock.history(period="1y")

            if hist.empty:
                continue

            start_price = hist["Close"].iloc[0]
            end_price = hist["Close"].iloc[-1]

            return_ratio = end_price / start_price

            past_value = current_value / return_ratio
            total_past_value += past_value

        except Exception:
            continue

    if total_past_value == 0:
        return {
            "total_return_pct": 0.0,
            "annualized_return_pct": 0.0
        }

    total_return = ((total_current_value - total_past_value) / total_past_value) * 100

    # Approximate annualized return
    annualized_return = total_return  # since 1-year period

    return {
        "total_return_pct": round(total_return, 2),
        "annualized_return_pct": round(annualized_return, 2)
    }


def get_benchmark_performance(benchmark="^GSPC"):
    """
    Default: S&P 500
    """

    try:
        index = yf.Ticker(benchmark)
        hist = index.history(period="1y")

        if hist.empty:
            return 0.0

        start_price = hist["Close"].iloc[0]
        end_price = hist["Close"].iloc[-1]

        return_pct = ((end_price - start_price) / start_price) * 100

        return round(return_pct, 2)

    except Exception:
        return 0.0


def choose_benchmark(portfolio):
    """
    Simple logic:
    If majority US stocks → S&P 500
    (You can improve later)
    """
    return "^GSPC"  # S&P 500