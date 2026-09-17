import streamlit as st
import pandas as pd
import yfinance as yf


st.set_page_config(
    page_title="Market Today",
    page_icon="📈",
    layout="wide"
)


st.title("📈 Market Today")
st.caption("Global markets, explained simply.")


# ==============================
# Load data
# ==============================

market_df = pd.read_csv(
    "data/global_market_snapshot.csv"
)

fx_df = pd.read_csv(
    "data/fx_snapshot.csv"
)

commodity_df = pd.read_csv(
    "data/commodity_snapshot.csv"
)

rate_df = pd.read_csv(
    "data/us_interest_rate.csv"
)

news_df = pd.read_csv(
    "data/news_snapshot.csv"
)


# ==============================
# Tabs
# ==============================

market_tab, fx_tab, commodity_tab, rate_tab, news_tab = st.tabs(
    [
        "📊 Markets",
        "💱 FX",
        "🪨 Commodities",
        "💰 Rates",
        "📰 News"
    ]
)


# ==============================
# Markets
# ==============================

with market_tab:

    st.subheader("Global Markets")

    market_cols = st.columns(3)

    for col, (_, row) in zip(
        market_cols,
        market_df.iterrows()
    ):

        market = row["Market"]
        price = row["Price"]
        change = row["Daily Change (%)"]
        date = row["Date"]

        col.metric(
            market,
            f"{price:,.2f}",
            f"{change:+.2f}%"
        )

        col.caption(
            f"Last updated: {date}"
        )

    st.divider()

    st.subheader("Market Performance")

    market_options = market_df["Market"].tolist()

    selected_market = st.selectbox(
        "Select market",
        market_options
    )

    symbol_map = {
        "S&P 500": "^GSPC",
        "NASDAQ 100": "^NDX",
        "ASX 200": "^AXJO",
        "Nikkei 225": "^N225",
        "KOSPI": "^KS11",
        "Hang Seng": "^HSI"
    }

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
        symbol_map[selected_market],
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

        chart_df.columns = [
            "Date",
            "Price"
        ]

        chart_df["Date"] = pd.to_datetime(
            chart_df["Date"]
        )

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
            f"{selected_market} — "
            f"{selected_period} price movement"
        )


# ==============================
# FX
# ==============================

with fx_tab:

    st.subheader("Foreign Exchange")

    fx_cols = st.columns(4)

    for col, (_, row) in zip(
        fx_cols,
        fx_df.iterrows()
    ):

        pair = row["Currency Pair"]
        rate = row["Rate"]
        change = row["Daily Change (%)"]
        date = row["Date"]

        if pair == "AUD/USD":
            rate_text = f"{rate:.4f}"
        else:
            rate_text = f"{rate:.2f}"

        col.metric(
            pair,
            rate_text,
            f"{change:+.2f}%"
        )

        col.caption(
            f"Last updated: {date}"
        )


# ==============================
# Commodities
# ==============================

with commodity_tab:

    st.subheader("Commodities")

    commodity_cols = st.columns(4)

    for col, (_, row) in zip(
        commodity_cols,
        commodity_df.iterrows()
    ):

        commodity = row["Commodity"]
        price = row["Price"]
        change = row["Daily Change (%)"]
        date = row["Date"]

        if commodity == "Copper":
            price_text = f"{price:.2f}"
        else:
            price_text = f"{price:,.2f}"

        col.metric(
            commodity,
            price_text,
            f"{change:+.2f}%"
        )

        col.caption(
            f"Last updated: {date}"
        )


# ==============================
# Interest Rates
# ==============================

with rate_tab:

    st.subheader("US Federal Funds")

    latest_rate = rate_df.iloc[-1]

    lower_rate = latest_rate["Lower Rate (%)"]
    upper_rate = latest_rate["Upper Rate (%)"]
    rate_date = latest_rate["Date"]

    st.metric(
        "Fed Target Range",
        f"{lower_rate:.2f}% – {upper_rate:.2f}%"
    )

    st.caption(
        f"Last updated: {rate_date}"
    )


# ==============================
# News
# ==============================

with news_tab:

    st.subheader("Market News")

    for _, row in news_df.head(10).iterrows():

        st.markdown(
            f"### [{row['Title']}]({row['Link']})"
        )

        st.caption(
            f"{row['Category']} · "
            f"{row['Published']}"
        )

        st.divider()


# ==============================
# Footer
# ==============================

st.caption(
    "Market data: Yahoo Finance · "
    "Interest rate data: FRED · "
    "News: CNBC RSS"
)