-- DDL Schema for NIFTY 50 Historical Forecast Storage
CREATE TABLE IF NOT EXISTS nifty_forecasts (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(15) NOT NULL,
    ds TIMESTAMP NOT NULL,
    yhat DOUBLE PRECISION NOT NULL,
    yhat_lower DOUBLE PRECISION NOT NULL,
    yhat_upper DOUBLE PRECISION NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_ticker_ds ON nifty_forecasts(ticker, ds);
