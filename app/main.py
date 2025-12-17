from fastapi import FastAPI
from app.utils import fetch_stock, summary_metrics
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from app.utils import fetch_stock, summary_metrics

app = FastAPI(title="Stock Data Intelligence API")

COMPANIES = ["INFY.NS", "TCS.NS", "RELIANCE.NS"]

@app.get("/")
def home():
    return {"message": "Stock Data Intelligence Dashboard API"}

@app.get("/companies")
def get_companies():
    return COMPANIES

@app.get("/data/{symbol}")
def get_stock_data(symbol: str):
    data = fetch_stock(symbol)

    if not data:
        return {"error": "No data found for this symbol"}

    return data


@app.get("/summary/{symbol}")
def get_summary(symbol: str):
    return summary_metrics(symbol)


@app.get("/compare")
def compare(symbol1: str, symbol2: str):
    df1 = fetch_stock(symbol1)
    df2 = fetch_stock(symbol2)

    return {
        symbol1: summary_metrics(df1),
        symbol2: summary_metrics(df2)
    }
