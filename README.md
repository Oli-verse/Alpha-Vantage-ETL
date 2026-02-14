A Python-based ETL (Extract, Transform, Load) pipeline that automates the collection of financial market data from Alpha Vantage, cleans it for analysis, and explores correlations for Machine Learning readiness.

# Features
- **Extract**: Automated fetching of Monthly Time Series data via Alpha Vantage API.
- **Transform**: Data cleaning using Pandas, including datetime conversion, numeric casting, and percentage return calculation.
- **Load**: Structured storage into CSV format with proper indexing.
- **Analysis**: Correlation studies and data visualization to identify predictive signals.

## Project Structure
```text
ETL Project/
├── script/
│   ├── main.py          # Orchestrator (Runs the full pipeline)
│   ├── extract.py       # API Acquisition logic
│   ├── transform.py     # Data cleaning and feature engineering
│   ├── load.py          # CSV/Database export logic
│   └── model.py         # Analysis and Visualization
├── .env                 # API Keys (Excluded from Git)
├── requirements.txt     # Project dependencies
├── IBM_monthly_data.csv # Final output data
└── volume_vs_returns_scatter.csv # Visualized Final output data


## Installation and Setup

1. Clone repository:

2. Install dependencies: 
    - pip install -r requirements.txt

3. Configure Environment Variables:
    - API_KEY=your_alpha_vantage_key_here

4. Run the Pipeline:
    - python script/main.py

5. Run the Analysis:
    - python model.py