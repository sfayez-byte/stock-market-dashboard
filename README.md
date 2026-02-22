# Market Pulse — Live Stock Market Dashboard

> A live financial dashboard monitoring price trends, sector performance, trading volume, and cumulative returns across 10 major stocks — powered by a Python ETL pipeline and refreshed daily.

**Built with:** Python | yfinance | pandas | Google Sheets | Tableau Public

🔗 **[View Live Dashboard](https://public.tableau.com/app/profile/samar.aladhadh/viz/MarketPulseLiveStockMarketDashboard/MainDashboard?publish=yes)**

---

## 📸 Dashboard Preview

![Market Pulse Dashboard](screenshots/Overview-KPI.png)

---

## 📊 What This Dashboard Answers

| Business Question | Chart |
|---|---|
| Which stocks are trending up over 6 months? | Price Trend |
| Which stocks delivered the best/worst daily returns? | Daily Return % |
| Which sectors are leading or lagging? | Sector Performance Heatmap |
| Which stocks have the highest trading conviction? | Volume Trend |
| What is the total return since August 2025? | Cumulative Returns |

---

## 🏗️ Architecture

```
Yahoo Finance API
      ↓
Python (yfinance + pandas)
      ↓
Google Sheets (live data layer)
      ↓
Tableau Public (live dashboard)
      ↓
GitHub (version control + documentation)
```

The pipeline runs manually to fetch the latest 6 months of OHLCV data, calculates derived metrics, and pushes to Google Sheets — which Tableau reads as a live data source.

---

## 📁 Repository Structure

```
stock-market-dashboard/
├── README.md
├── data/
│   └── stock_data.csv          # Clean dataset (1,230 rows × 14 fields)
├── pipeline/
│   └── fetch_stock_data.py     # Python ETL script
├── screenshots/
│   └── dashboard_overview.png  # Dashboard preview
└── docs/
    └── data_dictionary.md      # Field definitions
```

---

## 📦 Dataset

**10 Tickers across 4 Sectors:**

| Sector | Tickers |
|---|---|
| Technology | AAPL, MSFT, NVDA |
| Finance | JPM, GS |
| Healthcare | JNJ, PFE |
| Energy | XOM, CVX |
| Benchmark | SPY |

**Fields:**

| Field | Description |
|---|---|
| Date | Trading date |
| Ticker | Stock symbol |
| Company | Full company name |
| Sector | Industry sector |
| Open / High / Low / Close | Daily OHLC prices |
| Volume | Daily shares traded |
| Daily_Return_% | Day-over-day price change % |
| Cumulative_Return_% | Total return since start date |
| MA_20 | 20-day moving average |
| Price_vs_MA20 | Close price minus MA20 |
| Volatility_20d | 20-day rolling standard deviation |

---

## ⚙️ How to Run the Pipeline

**Prerequisites:**
```bash
pip install yfinance pandas
```

**Run:**
```bash
python pipeline/fetch_stock_data.py
```

This will:
1. Pull 6 months of historical data from Yahoo Finance
2. Calculate all derived metrics
3. Export a clean CSV to `/data/stock_data.csv`
4. Upload the data to Google Sheets manually for Tableau to read

---

## 🔑 Key Findings (as of Feb 2026)

- **Best Performer:** JNJ (+0.06% avg daily return) — only positive stock in the period
- **Worst Performer:** NVDA (-0.63% avg daily return) — highest volatility
- **Highest Volume:** NVDA — significant institutional trading activity
- **SPY Benchmark:** -0.0026% avg daily return — near-flat market overall

---

## 👤 Author

**Samar Aladhadh**
