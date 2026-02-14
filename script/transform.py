import pandas as pd

def transform_data(raw_json):
    # Extract the time series data from the raw JSON
    time_series = raw_json.get("Monthly Time Series", {})
    
    # Convert the time series data into a DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    
    # Rename columns for better readability
    df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    }, inplace=True)
    
    # Convert the index to datetime
    df.index = pd.to_datetime(df.index)
    
    
    for column in df.columns:
        df[column] = pd.to_numeric(df[column])
    
    return df