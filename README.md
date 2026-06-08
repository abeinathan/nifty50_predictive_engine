# NIFTY 50: Predictive Equity & Risk Engine

An end-to-end quantitative analytics engine engineered to extract, pipeline, and forecast 90-day forward-looking equity price trajectories and structural uncertainty risk bands for NIFTY 50 constituents.

📊 **Live Interactive Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/abei.nathan1154/viz/NIFTY50PredictiveEquityRiskAnalytics/NIFTY50PredictiveEquityRiskAnalytics)

## Technical Architecture & Design Pattern
- **Infrastructure Context:** Engineered natively within a Zorin OS desktop environment mapped to local database clusters.
- **Data Ingestion Layer (ETL):** Multi-threaded Python workflows utilizing `concurrent.futures` to execute asynchronous API queries across multiple index tickers, cutting processing constraints down significantly.
- **Data Warehousing:** Relational schema design implemented via a PostgreSQL backend utilizing optimized indexing patterns for historical tracking and cross-validation storage.
- **Predictive Modeling Layer:** Bayesian Time-Series Inference using additive regressive formulations via the **Prophet** framework to map structural trends, yearly cycles, and volatility constraints.
- **Downstream Visualization:** High-performance Tableau Public dashboard layout tracing expected price paths along with shaded uncertainty boundaries (`yhat_lower` to `yhat_upper`).

## Repository Blueprint
- `src/etl_pipeline.py`: Production-ready pipeline engine driving extraction, statistical model mapping, and automated database compilation.
- `database/schema.sql`: Relational database layouts optimized for high-performance indexing across temporal datasets.
- `templates/equity-analytics.html`: Standalone UI dashboard shell carrying responsive embedding code tailored for personal portfolio integrations.

## Execution Framework
```bash
# Initialize Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Apply explicit dependencies
pip install -r requirements.txt

# Trigger the multi-threaded ETL pipeline
python src/etl_pipeline.py
