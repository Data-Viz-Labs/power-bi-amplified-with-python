import pandas as pd
from datetime import datetime, timedelta, timezone
import yfinance as yf

# --- Parámetros (puedes convertirlos a Parámetros de Power BI si quieres) ---
symbol = "NVDA"            # Cambia por el ticker que necesites o pásalo como parámetro
years_back = 5             # Ventana temporal

# --- Fechas ---
end_date = datetime.now(timezone.utc)
start_date = end_date - timedelta(days=years_back * 365)

# --- Descarga de datos (yfinance) ---
# progress=False evita la barra, que a veces molesta al host de ejecución
data = yf.download(
    symbol,
    start=start_date.date(),
    end=end_date.date(),
    auto_adjust=False,
    progress=False
)

# --- Preparación del DataFrame ---
data = data.reset_index()

# Aplanar columnas si vinieran en MultiIndex (algunas versiones/activos devuelven esto)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = ['_'.join([str(x) for x in col if x]).strip('_') for col in data.columns]

# Normalizar nombres clave y añadir el símbolo
rename_map = {
    'Date': 'date',
    'Open': 'open',
    'High': 'high',
    'Low': 'low',
    'Close': 'close',
    'Adj Close': 'adj_close',
    'Volume': 'volume'
}
data = data.rename(columns=rename_map)

# Asegurar columna de fecha sin tz (Power BI prefiere naive datetimes)
data['date'] = pd.to_datetime(data['date']).dt.tz_localize(None)

# Añadir el símbolo como columna (muy útil si luego concatenas varios)
data.insert(0, 'symbol', symbol)

# Opcional: ordenar columnas
col_order = ['symbol', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']
data = data[[c for c in col_order if c in data.columns] + [c for c in data.columns if c not in col_order]]

# --- IMPORTANTÍSIMO: Power BI usa la variable 'dataset' ---
dataset = data
