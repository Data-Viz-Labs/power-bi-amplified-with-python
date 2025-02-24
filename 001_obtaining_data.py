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
