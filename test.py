import yfinance as yf

stock = yf.Ticker('STXRES.JO').info

for key, val in stock.items():
    print(key, ": ", val)
