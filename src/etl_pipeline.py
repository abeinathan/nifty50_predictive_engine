import concurrent.futures
import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from prophet import Prophet

# Target DB Connection String (Adjust credentials as required for deployment)
DATABASE_URL = "postgresql://postgres:password@localhost:5432/nifty50_db"

def run_predictive_pipeline(ticker: str):
    """Executes multi-threaded data ingestion, transformation, and Bayesian prediction."""
    print(f"Executing pipeline for: {ticker}")
    try:
        # Extraction
        raw_data = yf.download(ticker, start="2021-01-01", end="2026-06-01")
        if raw_data.empty:
            return f"Skipped {ticker}: No data returned."
            
        # Transformation
        df = raw_data[['Close']].reset_index()
        df.columns = ['ds', 'y']
        df['ds'] = df['ds'].dt.tz_localize(None)
        
        # Bayesian Forecasting Setup
        model = Prophet(daily_seasonality=False, weekly_seasonality=True, yearly_seasonality=True)
        model.fit(df)
        
        # Generate 90-Day Trajectory Window
        future = model.make_future_dataframe(periods=90)
        forecast = model.predict(future)
        
        # Isolate Metrics & Export
        output = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
        output['ticker'] = ticker
        
        engine = create_engine(DATABASE_URL)
        output.to_sql('nifty_forecasts', con=engine, if_exists='append', index=False)
        return f"Successfully updated database records for {ticker}"
        
    except Exception as e:
        return f"Pipeline execution failed for {ticker}: {str(e)}"

if __name__ == "__main__":
    # Top NIFTY 50 heavyweights by index allocation
    target_tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS"]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        execution_logs = list(executor.map(run_predictive_pipeline, target_tickers))
        
    for log in execution_logs:
        print(log)
