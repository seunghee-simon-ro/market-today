import yfinance as yf
import pandas as pd


FX_PAIRS = {
    "AUD/USD": "AUDUSD=X",
    "AUD/KRW": "KRWAUD=X",
    "AUD/CNY": "CNYAUD=X",
    "AUD/JPY": "JPYAUD=X"
}


def get_fx_data(pair, symbol):
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

    # Convert inverse quotes to "1 AUD = X"
    if pair == "AUD/KRW":
        rate = 1 / latest_close
        previous_rate = 1 / previous_close

    elif pair == "AUD/CNY":
        rate = 1 / latest_close
        previous_rate = 1 / previous_close

    elif pair == "AUD/JPY":
        rate = 1 / latest_close
        previous_rate = 1 / previous_close

    else:
        rate = latest_close
        previous_rate = previous_close

    change_percent = (
        (rate - previous_rate)
        / previous_rate
        * 100
    )

    latest_date = data.index[-1].strftime("%Y-%m-%d")

    return {
        "Date": latest_date,
        "Rate": rate,
        "Daily Change (%)": change_percent
    }


results = []

for pair, symbol in FX_PAIRS.items():
    data = get_fx_data(pair, symbol)

    if data:
        results.append({
            "Currency Pair": pair,
            "Date": data["Date"],
            "Rate": data["Rate"],
            "Daily Change (%)": round(
                data["Daily Change (%)"], 2
            )
        })


fx_df = pd.DataFrame(results)

# Display rates with appropriate precision
fx_df["Rate"] = fx_df.apply(
    lambda row: (
        round(row["Rate"], 4)
        if row["Currency Pair"] == "AUD/USD"
        else round(row["Rate"], 2)
    ),
    axis=1
)


print("\n==============================")
print("        FX MARKET")
print("==============================\n")

print(fx_df.to_string(index=False))


fx_df.to_csv(
    "data/fx_snapshot.csv",
    index=False
)

print("\nSaved:")
print("data/fx_snapshot.csv")