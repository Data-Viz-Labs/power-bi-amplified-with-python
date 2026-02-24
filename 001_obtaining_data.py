import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

symbol = "NVDA"

end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)

data = yf.download(symbol, start=start_date, end=end_date)

# Reset index para que Date sea columna
data = data.reset_index()

# Aplanar columnas si son MultiIndex
if isinstance(data.columns, pd.MultiIndex):
    data.columns = [col[0] for col in data.columns]

dataset = data
