from fredapi import Fred
from dotenv import load_dotenv
import os
import pandas as pd

# ==========================================
# Market Today
# US Federal Funds Target Rate
# ==========================================

load_dotenv()

API_KEY = os.getenv("FRED_API_KEY")

fred = Fred(api_key=API_KEY)

# Historical Federal Funds Target Range
lower_rate = fred.get_series("DFEDTARL")
upper_rate = fred.get_series("DFEDTARU")

interest_rate_df = pd.concat(
    [lower_rate, upper_rate],
    axis=1
)

interest_rate_df.columns = [
    "Lower Rate (%)",
    "Upper Rate (%)"
]

interest_rate_df = interest_rate_df.dropna()

interest_rate_df.index.name = "Date"

# Save historical data
interest_rate_df.to_csv(
    "data/us_interest_rate.csv"
)

# Latest FRED observation
latest = interest_rate_df.iloc[-1]

print("\n==============================")
print("      US FEDERAL FUNDS")
print("==============================\n")

print(
    f"Latest FRED Target Range: "
    f"{latest['Lower Rate (%)']:.2f}% - "
    f"{latest['Upper Rate (%)']:.2f}%"
)

print("\nSaved:")
print("data/us_interest_rate.csv")