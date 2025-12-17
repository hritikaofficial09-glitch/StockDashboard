import yfinance as yf


def fetch_stock(symbol: str):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1y")

    if df is None or df.empty:
        return []

    df = df.reset_index()

    results = []

    for _, row in df.tail(30).iterrows():
        results.append({
            "date": str(row["Date"]),
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })

    return results


def summary_metrics(symbol: str):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1y")

    if df is None or df.empty:
        return {
            "52_week_high": 0,
            "52_week_low": 0,
            "avg_close": 0
        }

    return {
        "52_week_high": float(df["High"].max()),
        "52_week_low": float(df["Low"].min()),
        "avg_close": float(df["Close"].mean()),
    }
