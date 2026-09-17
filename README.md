# 📈 Market Today

> **The market snapshot I check every morning.**

Market Today is a personal financial dashboard designed to provide a quick snapshot of the global markets I follow on a daily basis.

Instead of checking multiple websites and financial platforms every morning, the dashboard brings the key market indicators together in one place so I can quickly see what has changed since the previous trading session.

## 🌍 What I Check Every Morning

### 📊 Global Markets

Major equity indices across key markets:

- 🇺🇸 S&P 500
- 🇺🇸 NASDAQ 100
- 🇦🇺 ASX 200
- 🇯🇵 Nikkei 225
- 🇰🇷 KOSPI
- 🇭🇰 Hang Seng

Each market shows its latest index level, daily percentage change, and last available trading date.

Historical performance can also be explored across:

- 1 Month
- 6 Months
- 1 Year
- 5 Years
- 10 Years

### 💱 Foreign Exchange

AUD exchange rates against major currencies:

- AUD/USD
- AUD/KRW
- AUD/CNY
- AUD/JPY

These are particularly useful for monitoring movements in the Australian dollar against major currencies.

### 🪨 Commodities

Key commodities that I follow:

- Gold
- Crude Oil
- Copper
- Iron Ore

### 💰 Interest Rates

The dashboard tracks the US Federal Funds target range using data from the Federal Reserve Economic Data (FRED).

### 📰 Market News

Recent financial and economic headlines collected through CNBC RSS.

News can be filtered by category to quickly focus on the topics relevant to the day's market movements.

## 🖥️ Dashboard

The dashboard is organised into five sections:

**Markets · FX · Commodities · Rates · News**

The objective is simple:

> **Open the dashboard → scan the key numbers → understand what moved → start the day.**

## 🛠️ Tools & Technologies

- **Python**
- **Streamlit**
- **Pandas**
- **yfinance**
- **FRED API**
- **Feedparser**
- **Altair**
- **Git & GitHub**

## 📁 Project Structure

```text
market-today/
│
├── app.py
├── README.md
├── .gitignore
├── .env
│
├── data/
│   ├── global_market_snapshot.csv
│   ├── us_interest_rate.csv
│   ├── fx_snapshot.csv
│   ├── commodity_snapshot.csv
│   └── news_snapshot.csv
│
└── src/
    ├── market_data.py
    ├── interest_rates.py
    ├── fx_data.py
    ├── commodity_data.py
    └── news_data.py

## 📊 Data Sources

| Data | Source |
|---|---|
| Global Markets | Yahoo Finance |
| Foreign Exchange | Yahoo Finance |
| Commodities | Yahoo Finance |
| US Federal Funds Target Range | FRED |
| Market News | CNBC RSS |

## 🔎 Key Features

- Daily global market snapshot
- Latest index levels and daily movements
- Historical market performance
- AUD-based FX monitoring
- Key commodity prices
- US Federal Funds target range
- Categorised market news
- Single-page morning market overview
- Interactive Streamlit dashboard

## 🎯 Project Purpose

I built Market Today to solve a simple problem in my own daily workflow.

Every morning, I want to quickly check the markets that matter to me — equity indices, currencies, commodities, interest rates, and major financial news.

Previously, this meant checking multiple sources separately.

Market Today brings these indicators together into a single dashboard so that I can get a quick overview of the global market before starting the day.

The project also serves as a practical exercise in building a data pipeline from external data sources and turning the results into a usable analytical interface.

## 🚀 Future Improvements

Potential future improvements include:

- Automated daily data refresh
- Additional global market indices
- More central bank interest rates
- Historical FX and commodity charts
- Market comparison tools
- Additional economic indicators
- Improved news classification
- Cloud deployment