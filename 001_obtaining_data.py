"""
Downloads NVIDIA (NVDA) stock data for the last 5 years using yfinance.
For Power BI: Ensure yfinance is installed in the Python environment configured in Power BI.
Input: None
Output: DataFrame with columns [Date, Open, High, Low, Close, Adj Close, Volume]
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

symbol = "NVDA"

end_date = datetime.now()
start_date = end_date - timedelta(days=5*365) # 5YTD

data = yf.download(symbol, start=start_date, end=end_date)

# Reset index in order to turn date onto a column
data = data.reset_index()

print(data)
