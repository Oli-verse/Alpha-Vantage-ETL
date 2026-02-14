import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    return r.json()