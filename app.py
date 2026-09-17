import streamlit as st
import pandas as pd
import yfinance as yf

# ==========================================
# Market Today
# Global markets, explained simply.
# ==========================================

st.set_page_config(
    page_title="Market Today",
    page_icon="📈",
    layout="wide"
)

MARKETS = {
    "S&P 500": "^GSPC",
    "NASDAQ 100": "^NDX",
    "ASX 200": "^AXJO",
    "Nikkei 225": "^N225",
    "KOSPI": "^KS11",
    "Hang Seng": "^HSI"
}

# ==========================================
# Load Current Market Data
# ==========================================

market_df = pd.read_csv(
    "data/global_market_snapshot.csv"
)

# ==========================================
# Load Interest Rate Data
# ==========================================

interest_df = pd.read_csv(
    "data/us_interest_rate.csv"
)

latest_rate = interest_df.iloc[-1]

# ==========================================
# Header
# ==========================================

st.title("📈 Market Today")

st.caption("Global markets, explained simply.")

st.divider()

# ==========================================
# Global Markets
# ==========================================

st.header("Global Markets")

columns = st.columns(3)

for i, row in market_df.iterrows():

    column = columns[i % 3]

    change = row["Daily Change (%)"]

    with column:

        st.metric(
            label=row["Market"],
            value=f"{row['Price']:,.2f}",
            delta=f"{change:+.2f}%"
        )

        st.caption(
            f"Last updated: {row['Date']}"
        )

# ==========================================
# Market Chart
# ==========================================

st.divider()

st.header("Market Performance")

selected_market = st.selectbox(
    "Select a market",
    list(MARKETS.keys())
)

selected_symbol = MARKETS[selected_market]

period_options = {
    "1 Month": "1mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "5 Years": "5y",
    "10 Years": "10y"
}

selected_period = st.selectbox(
    "Time period",
    list(period_options.keys()),
    index=4
)

period = period_options[selected_period]

chart_data = yf.download(
    selected_symbol,
    period=period,
    progress=False,
    auto_adjust=False
)

if not chart_data.empty:

    import altair as alt

    close_data = chart_data["Close"]

    if isinstance(close_data, pd.DataFrame):
        close_data = close_data.iloc[:, 0]

    chart_df = close_data.reset_index()

    chart_df.columns = ["Date", "Price"]

    chart_df["Date"] = pd.to_datetime(chart_df["Date"])

    chart = (
        alt.Chart(chart_df)
        .mark_line()
        .encode(
            x=alt.X(
                "Date:T",
                title="Date",
                axis=alt.Axis(
                    format="%b %Y"
                )
            ),
            y=alt.Y(
                "Price:Q",
                title="Index Level",
                axis=alt.Axis(
                    format=",.2f"
                )
            ),
            tooltip=[
                alt.Tooltip(
                    "Date:T",
                    title="Date",
                    format="%d %b %Y"
                ),
                alt.Tooltip(
                    "Price:Q",
                    title=selected_market,
                    format=",.2f"
                )
            ]
        )
        .properties(
            height=450
        )
        .interactive()
    )

    st.altair_chart(
        chart,
        use_container_width=True
    )

    st.caption(
        f"{selected_market} — {selected_period} price movement"
    )

# ==========================================
# Interest Rates
# ==========================================

st.divider()

st.header("Interest Rates")

st.metric(
    label="🇺🇸 US Federal Funds Target Rate",
    value=(
        f"{latest_rate['Lower Rate (%)']:.2f}% – "
        f"{latest_rate['Upper Rate (%)']:.2f}%"
    )
)

st.caption(
    f"Latest FRED observation: {latest_rate['Date']}"
)

# ==========================================
# Footer
# ==========================================

st.divider()

st.caption(
    "Market data: Yahoo Finance · "
    "Interest rate data: Federal Reserve Economic Data (FRED)"
)