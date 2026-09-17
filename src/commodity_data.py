import yfinance as yf
import pandas as pd


COMMODITIES = {
    "Gold": "GC=F",
    "Crude Oil": "CL=F",
    "Copper": "HG=F",
    "Iron Ore": "TIO=F"
}


def get_commodity_data(symbol):
    data = yf.download(
        symbol,
        period="5d",
        progress=False,
        auto_adjust=False
    )

    if data.empty:
        return None

    close_data = data["Close"]

    if isinstance(close_data, pd.DataFrame):
        close_data = close_data.iloc[:, 0]

    close_data = close_data.dropna()

    if len(close_data) < 2:
        return None

    latest_price = float(close_data.iloc[-1])
    previous_price = float(close_data.iloc[-2])

    change_percent = (
        (latest_price - previous_price)
        / previous_price
        * 100
    )

    latest_date = close_data.index[-1].strftime("%Y-%m-%d")

    return {
        "Date": latest_date,
        "Price": latest_price,
        "Daily Change (%)": change_percent
    }


results = []

for commodity, symbol in COMMODITIES.items():

    data = get_commodity_data(symbol)

    if data:
        results.append({
            "Commodity": commodity,
            "Date": data["Date"],
            "Price": data["Price"],
            "Daily Change (%)": round(
                data["Daily Change (%)"], 2
            )
        })


commodity_df = pd.DataFrame(results)


print("\n==============================")
print("       COMMODITY MARKET")
print("==============================\n")

print(
    commodity_df.to_string(index=False)
)


commodity_df.to_csv(
    "data/commodity_snapshot.csv",
    index=False
)


print("\nSaved:")
print("data/commodity_snapshot.csv")