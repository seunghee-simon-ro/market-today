# Market Today

**Global markets, explained simply.**

Market Today is a beginner-friendly global market project designed to make financial markets easier to understand.

The project collects market data and presents key movements in a simple format, with the goal of connecting **market data, business context, and clear explanations**.

## Project Overview

Market Today explores major global financial markets and helps answer simple questions:

- What happened in the market today?
- Which markets moved?
- How much did they move?
- Why might the movement matter?

The project is being developed step by step, starting with global market data collection.

## Current Features

### Global Market Snapshot

The current version collects daily market data for:

- S&P 500
- NASDAQ 100
- ASX 200
- Nikkei 225
- KOSPI
- Hang Seng

The data is collected using the Alpha Vantage API and saved as a CSV file for further analysis.

## Tools & Technologies

- Python
- Pandas
- Requests
- Alpha Vantage API
- Git
- GitHub

## Project Structure

```text
market-today/
├── README.md
├── data/
│   └── global_market_snapshot.csv
└── src/
    └── market_data.py
```

## Data Pipeline

```text
Alpha Vantage API
        │
        ▼
     Python
        │
        ▼
   Market Data
        │
        ▼
     Pandas
        │
        ▼
Daily Change
Calculation
        │
        ▼
Market Snapshot
        │
        ▼
     CSV File
```

## Future Development

The project will gradually expand to include:

- Global interest rates
- Foreign exchange rates
- Commodities
- Market news
- Simple market explanations
- "What happened?" summaries
- "Why does it matter?" explanations
- Interactive dashboard

## Project Goal

The goal is not simply to collect financial data.

Market Today aims to explore how **data and technology can make complex global markets easier to understand**, especially for people who are new to financial markets.

## Notes

Market data is collected through the Alpha Vantage API.

Some international market values are currently represented using market-related ETF proxies rather than the underlying index itself. This distinction will be addressed as the project develops.

This project is for educational and portfolio purposes and is not financial advice.