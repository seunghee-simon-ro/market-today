import yfinance as yf
import pandas as pd

# ==========================================
# Market Today
# Global Stock Market Snapshot
# ==========================================

MARKETS = {
    "S&P 500": "^GSPC",
    "NASDAQ 100": "^NDX",
    "ASX 200": "^AXJO",
    "Nikkei 225": "^N225",
    "KOSPI": "^KS11",
    "Hang Seng": "^HSI"
}


def get_market_data(symbol):

    data = yf.download(
        symbol,
        period="5d",
        progress=False,
        auto_adjust=False
    )

    if data.empty:
        return None

    latest_close = float(data["Close"].iloc[-1].iloc[0])
    previous_close = float(data["Close"].iloc[-2].iloc[0])

    change_percent = (
        (latest_close - previous_close)
        / previous_close
        * 100
    )

    return {
        "Price": round(latest_close, 2),
        "Daily Change (%)": round(change_percent, 2)
    }


results = []

for market, symbol in MARKETS.items():

    data = get_market_data(symbol)

    if data:
        results.append({
            "Market": market,
            "Price": data["Price"],
            "Daily Change (%)": data["Daily Change (%)"]
        })


market_df = pd.DataFrame(results)

print("\n==============================")
print("      MARKET TODAY")
print("==============================\n")

print(market_df.to_string(index=False))

market_df.to_csv(
    "data/global_market_snapshot.csv",
    index=False
)

print("\nSaved:")
print("data/global_market_snapshot.csv")