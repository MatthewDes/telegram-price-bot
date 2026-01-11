# Telegram Price Bot

This project is a simple Python bot that sends daily price updates for a portfolio of crypto, stocks, and commodities to a specified Telegram chat.

## How It Works

The bot fetches price data from two main sources:
-   **CoinGecko API**: For cryptocurrency prices.
-   **yfinance**: For stock and commodity prices.

The main script (`main.py`) reads a list of assets from `assets_to_get.json`, fetches the latest prices and 24-hour percentage changes, formats them into a message, and sends it to your Telegram chat.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/telegram-price-bot.git
    cd telegram-price-bot
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file:**
    Create a `.env` file in the root of the project and add the following environment variables:

    ```
    TELEGRAM_TOKEN=your_telegram_bot_token
    TELEGRAM_CHAT_ID=your_telegram_chat_id
    COINGECKO_API=your_coingecko_api_key
    ```

    -   `TELEGRAM_TOKEN`: Your Telegram bot token from BotFather.
    -   `TELEGRAM_CHAT_ID`: The ID of the chat where you want to receive notifications.
    -   `COINGECKO_API`: Your API key from CoinGecko.

## Configuration

To specify which assets to track, edit the `assets_to_get.json` file. The assets are categorized into `crypto`, `stocks`, and `commodities`.

-   For `crypto`, use the CoinGecko API ID (e.g., "bitcoin", "ethereum").
-   For `stocks` and `commodities`, use the Yahoo Finance ticker symbol (e.g., "AAPL", "GC=F").

Example `assets_to_get.json`:
```json
{
   "crypto": ["bitcoin", "ethereum"],
   "stocks": ["AAPL", "STXRES.JO"],
   "commodities": ["GC=F"]
}
```

## Usage

To run the bot manually, execute the `main.py` script:
```bash
python main.py
```

## Automation

This project includes a GitHub Actions workflow in `.github/workflows/price_bot_daily_run.yml` that automatically runs the bot every morning at 05:00 UTC (07:00 SAST).

For the workflow to function correctly, you need to add the same environment variables (`TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID`, `COINGECKO_API`) as secrets in your GitHub repository settings under `Settings > Secrets and variables > Actions`.
