import requests
import yfinance as yf


def fetch_crypto_price(COINGECKO_API: str, ids: list) -> dict:
    """
     uses CoinGecko api key to get the most recent price of bitcoin and the 24 hour change
    """
    ids_str = ",".join(ids)

    url = "https://api.coingecko.com/api/v3/simple/price"
    headers = {"x-cg-demo-api-key": f"{COINGECKO_API}"}
    params = {
    "ids": ids_str,       #requires input like: "id1,id2"
    "vs_currencies": "usd",
    "include_24hr_change": "true"
    }

    response = requests.get(url, params=params, headers=headers).json()
    return response

def fetch_yfinance(ticker: str) -> tuple[float, float]:

    stock = yf.Ticker(ticker)
    info = stock.history(period="2d", interval="1d")

    last = info['Close'].iloc[-1]
    if len(info) > 1:
        prev = info['Close'].iloc[-2]
        pct = (last - prev) / prev * 100 if prev != 0 else 0.0
    else:
        pct = 0.0

    return float(last), float(pct)

def build_message(COINGECKO_API: str, assets: dict) -> str: 
    lines = []

    if assets.get("crypto"):
        crypto = fetch_crypto_price(COINGECKO_API, assets["crypto"])

        for coin in assets["crypto"]:
            details = crypto.get(coin, {})
            price = details.get("usd")
            change = details.get("usd_24h_change")
            if price is None:
                lines.append(f"• {c}: data unavailable")
            else:
                sign = "🟩" if change is not None and change >= 0 else "🟥"
                lines.append(f"• {coin.capitalize()}: ${price:,.2f} {sign}{abs(change):.2f}%")

    if assets.get("stocks"):
        for s in assets["stocks"]:
            price, pct = fetch_yfinance(s)
            if price is None:
                lines.append(f"• {s}: data unavailable")
            else:
                sign = "🟩" if pct >= 0 else "🟥"
                lines.append(f"• {s}: ${price:,.2f} {sign}{abs(pct):.2f}%")

    if assets.get("commodities"):
        for c in assets["commodities"]:
            price, pct = fetch_yfinance(c)
            if price is None:
                lines.append(f"• {c}: data unavailable")
            else:
                sign = "🟩" if pct >= 0 else "🟥"
                lines.append(f"• {c}: ${price:,.2f} {sign}{abs(pct):.2f}%")

    return "\n".join(lines)
    
def send_telegram(TELEGRAM_TOKEN: str, TELEGRAM_CHAT_ID: str, text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    r = requests.post(url, data=payload, timeout=10)
    print(r.json())
    return r.json()