import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

# ==========================================
# Market Today
# Global Stock Market Snapshot
# ==========================================

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

# Major global indices (ETF used where index API is unavailable)
MARKETS = {
    "S&P 500": "SPY",
    "NASDAQ 100": "QQQ",
    "ASX 200": "EWA",
    "Nikkei 225": "EWJ",
    "KOSPI": "EWY",
    "Hang Seng": "EWH"
}


def get_market_data(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Global Quote" not in data or not data["Global Quote"]:
        return None

    quote = data["Global Quote"]

    return {
        "Price": float(quote["05. price"]),
        "Change (%)": float(quote["10. change percent"].replace("%", ""))
    }


results = []

for market, symbol in MARKETS.items():

    data = get_market_data(symbol)

    if data:
        results.append({
            "Market": market,
            "Price": round(data["Price"], 2),
            "Daily Change (%)": round(data["Change (%)"], 2)
        })

    time.sleep(12)      # Free API limit (5 requests/minute)

market_df = pd.DataFrame(results)

print("\n==============================")
print("      MARKET TODAY")
print("==============================\n")

print(market_df)

market_df.to_csv("data/global_market_snapshot.csv", index=False)

print("\nSaved:")
print("data/global_market_snapshot.csv")