import os
from dotenv import load_dotenv
import requests

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
COINGECKO_API = os.getenv("COINGECKO_API")

def fetch_crypto_price(coins):
    url = "https://api.coingecko.com/api/v3/simple/price"
    headers = {"x-cg-demo-api-key": f"{COINGECKO_API}"}
    params = {
    "ids": coins,
    "vs_currencies": "usd",
    "include_24hr_change": "true"
    }

    response = requests.get(url, params=params, headers=headers).json()

    print(response)  #{'bitcoin': {'usd': 111615, 'usd_24h_change': 1.3829312001005238}}
    return response

def build_message():
    crypto = fetch_crypto_price("bitcoin")
    for c, info in crypto.items():
        name = c
        price = info["usd"]
        change = info["usd_24h_change"]
    
    message = f"current price for {name} is: {price}, 24 hour change: {change}"
    return message


def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    r = requests.post(url, data=payload, timeout=10)
    print(r.json())
    return r.json()

send_telegram(build_message())

 

