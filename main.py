import os
from dotenv import load_dotenv
import json
from utils import send_telegram, build_message

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
COINGECKO_API = os.getenv("COINGECKO_API")

with open('assets_to_get.json', 'r') as f:
    assets = json.load(f)






send_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, build_message(COINGECKO_API, assets))




"""
To do
update yfinance to potentially use info isntead of history - may be more simple
update yfinance to use name isntead of ticker
add good morning message at begining with datetime
"""


 

