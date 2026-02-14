from extract import get_data
from transform import transform_data
from load import load_data

def run_pipeline(ticker):
    print(f"Starting ETL for {ticker}...")
    
    # Step 1: Extract
    raw_json = get_data(ticker)
    
    # Step 2: Transform
    # Passing the JSON from extract into the transform function
    clean_df = transform_data(raw_json)
    
    # Step 3: Load
    # Saving the resulting DataFrame to a CSV
    filename = f"{ticker}_monthly_data.csv"
    load_data(clean_df, filename)
    
    print("ETL Job Finished Successfully!")

if __name__ == "__main__":
    run_pipeline("IBM")

    