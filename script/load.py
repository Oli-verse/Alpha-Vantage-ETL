import pandas as pd

def load_data(df, file_path):
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=True, index_label='Date')
    print(f"Data loaded successfully to {file_path}")