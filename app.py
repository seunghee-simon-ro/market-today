import streamlit as st
import pandas as pd
import yfinance as yf
import altair as alt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Market Today",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 1400px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    .main-title {
        font-size: 2.6rem;
        font-weight: 700;
        letter-spacing: -0.04em;
        margin-bottom: 0.1rem;
    }

    .subtitle {
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }

    .live-status {
        display: inline-block;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        color: #15803d;
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-radius: 20px;
        padding: 5px 11px;
        margin-bottom: 1.8rem;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 650;
        letter-spacing: -0.02em;
        margin-top: 0.5rem;
        margin-bottom: 0.4rem;
    }

    .section-description {
        color: #6b7280;
        font-size: 0.88rem;
        margin-bottom: 1.2rem;
    }

    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
    }

    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem;
        font-weight: 600;
        color: #4b5563;
    }

    div[data-testid="stMetricValue"] {
        font-size: 1.75rem;
        font-weight: 650;
        letter-spacing: -0.03em;
    }

    div[data-testid="stMetricDelta"] {
        font-size: 0.9rem;
        font-weight: 600;
    }

    button[data-baseweb="tab"] {
        font-size: 0.95rem;
        font-weight: 600;
    }

    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }

    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.75rem;
        margin-top: 2.5rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📈 Market Today</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Global markets, explained simply.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="live-status">● LIVE DATA</div>',
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

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


# ============================================================
# MARKET FLAGS
# ============================================================

flag_map = {
    "S&P 500": "🇺🇸",
    "NASDAQ 100": "🇺🇸",
    "ASX 200": "🇦🇺",
    "Nikkei 225": "🇯🇵",
    "KOSPI": "🇰🇷",
    "Hang Seng": "🇭🇰"
}


# ============================================================
# TABS
# ============================================================

market_tab, fx_tab, commodity_tab, rate_tab, news_tab = st.tabs(
    [
        "📊 Markets",
        "💱 FX",
        "🪨 Commodities",
        "💰 Rates",
        "📰 News"
    ]
)


# ============================================================
# MARKETS
# ============================================================

with market_tab:

    st.markdown(
        '<div class="section-title">Global Markets</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Major global equity indices and daily performance.'
        '</div>',
        unsafe_allow_html=True
    )

    # First row
    market_cols = st.columns(3)

    for col, (_, row) in zip(
        market_cols,
        market_df.iloc[:3].iterrows()
    ):

        market = row["Market"]
        price = row["Price"]
        change = row["Daily Change (%)"]
        date = row["Date"]

        flag = flag_map.get(
            market,
            ""
        )

        with col:

            st.markdown(
                f"**{flag} {market}**"
            )

            st.metric(
                label="",
                value=f"{price:,.2f}",
                delta=f"{change:+.2f}%"
            )

            st.caption(
                f"Updated {date}"
            )

    # Second row
    market_cols = st.columns(3)

    for col, (_, row) in zip(
        market_cols,
        market_df.iloc[3:6].iterrows()
    ):

        market = row["Market"]
        price = row["Price"]
        change = row["Daily Change (%)"]
        date = row["Date"]

        flag = flag_map.get(
            market,
            ""
        )

        with col:

            st.markdown(
                f"**{flag} {market}**"
            )

            st.metric(
                label="",
                value=f"{price:,.2f}",
                delta=f"{change:+.2f}%"
            )

            st.caption(
                f"Updated {date}"
            )

    st.divider()

    # Market Performance
    st.markdown(
        '<div class="section-title">Market Performance</div>',
        unsafe_allow_html=True
    )

    market_options = market_df["Market"].tolist()

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

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        selected_market = st.selectbox(
            "Select market",
            market_options
        )

    with chart_col2:

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

        close_data = chart_data["Close"]

        if isinstance(
            close_data,
            pd.DataFrame
        ):

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
            f"{selected_market} · "
            f"{selected_period} price movement"
        )


# ============================================================
# FX
# ============================================================

with fx_tab:

    st.markdown(
        '<div class="section-title">Foreign Exchange</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Australian dollar exchange rates against major currencies.'
        '</div>',
        unsafe_allow_html=True
    )

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

        with col:

            st.metric(
                pair,
                rate_text,
                f"{change:+.2f}%"
            )

            st.caption(
                f"Updated {date}"
            )


# ============================================================
# COMMODITIES
# ============================================================

with commodity_tab:

    st.markdown(
        '<div class="section-title">Commodities</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Key commodities followed by global markets.'
        '</div>',
        unsafe_allow_html=True
    )

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

        with col:

            st.metric(
                commodity,
                price_text,
                f"{change:+.2f}%"
            )

            st.caption(
                f"Updated {date}"
            )


# ============================================================
# INTEREST RATES
# ============================================================

with rate_tab:

    st.markdown(
        '<div class="section-title">US Federal Funds</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'The latest Federal Funds target range available in FRED.'
        '</div>',
        unsafe_allow_html=True
    )

    latest_rate = rate_df.iloc[-1]

    lower_rate = latest_rate[
        "Lower Rate (%)"
    ]

    upper_rate = latest_rate[
        "Upper Rate (%)"
    ]

    rate_date = latest_rate[
        "Date"
    ]

    rate_col1, rate_col2 = st.columns(2)

    with rate_col1:

        st.metric(
            "Fed Target Range",
            f"{lower_rate:.2f}% – "
            f"{upper_rate:.2f}%"
        )

    with rate_col2:

        st.metric(
            "Range Width",
            f"{upper_rate - lower_rate:.2f} "
            "percentage points"
        )

    st.caption(
        f"Updated {rate_date}"
    )


# ============================================================
# NEWS
# ============================================================

with news_tab:

    st.markdown(
        '<div class="section-title">Market News</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Recent financial and economic headlines.'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # News category filter
    # --------------------------------------------------------

    categories = sorted(
        news_df["Category"]
        .dropna()
        .unique()
        .tolist()
    )

    category_options = [
        "All News"
    ] + categories

    selected_category = st.selectbox(
        "News category",
        category_options
    )


    # --------------------------------------------------------
    # Filter news
    # --------------------------------------------------------

    if selected_category == "All News":

        filtered_news = news_df

    else:

        filtered_news = news_df[
            news_df["Category"] == selected_category
        ]


    # --------------------------------------------------------
    # News count
    # --------------------------------------------------------

    st.caption(
        f"{len(filtered_news)} articles"
    )


    # --------------------------------------------------------
    # News cards
    # --------------------------------------------------------

    news_items = filtered_news.head(10).reset_index(
        drop=True
    )

    for start in range(
        0,
        len(news_items),
        2
    ):

        news_cols = st.columns(2)

        for col, index in zip(
            news_cols,
            range(
                start,
                min(start + 2, len(news_items))
            )
        ):

            row = news_items.iloc[index]

            title = row["Title"]
            link = row["Link"]
            category = row["Category"]
            published = row["Published"]

            with col:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        f"### [{title}]({link})"
                    )

                    st.caption(
                        f"{category} · {published}"
                    )

                    st.markdown(
                        "↗ **Read full article**"
                    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Market data: Yahoo Finance ·
        Interest rate data: FRED ·
        News: CNBC RSS
    </div>
    """,
    unsafe_allow_html=True
)