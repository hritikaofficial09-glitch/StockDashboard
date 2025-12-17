# Stock Data Intelligence Dashboard

## Tech Stack
- Python
- FastAPI
- Pandas
- SQLite

## Features
- Stock data collection and cleaning
- Daily return and volatility calculation
- REST APIs with FastAPI
- Swagger documentation

## Run
pip install -r requirements.txt  
uvicorn app.main:app --reload

## Key Challenges & Solutions
- Handled JSON serialization issues caused by Pandas and NumPy data types
- Implemented manual data normalization to ensure API stability
- Designed APIs to gracefully handle missing or unavailable market data

  
## Key Challenges & Solutions
- Faced JSON serialization issues due to Pandas/NumPy data types
- Solved by normalizing API responses into plain Python objects
- Designed APIs to gracefully handle missing or unavailable market data

