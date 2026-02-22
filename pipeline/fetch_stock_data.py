import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# ── CONFIGURATION ──────────────────────────────────────────
TICKERS = {
    "AAPL":  {"name": "Apple",           "sector": "Technology"},
    "MSFT":  {"name": "Microsoft",       "sector": "Technology"},
    "NVDA":  {"name": "NVIDIA",          "sector": "Technology"},
    "JPM":   {"name": "JPMorgan Chase",  "sector": "Finance"},
    "GS":    {"name": "Goldman Sachs",   "sector": "Finance"},
    "JNJ":   {"name": "Johnson & Johnson","sector": "Healthcare"},
    "PFE":   {"name": "Pfizer",          "sector": "Healthcare"},
    "XOM":   {"name": "ExxonMobil",      "sector": "Energy"},
    "CVX":   {"name": "Chevron",         "sector": "Energy"},
    "SPY":   {"name": "S&P 500 ETF",     "sector": "Benchmark"},
}

END_DATE   = datetime.today().strftime("%Y-%m-%d")
START_DATE = (datetime.today() - timedelta(days=180)).strftime("%Y-%m-%d")

# ── FETCH DATA ─────────────────────────────────────────────
print("Fetching stock data... please wait.")

all_data = []

for ticker, info in TICKERS.items():
    print(f"  → Pulling {ticker}...")
    df = yf.download(ticker, start=START_DATE, end=END_DATE, auto_adjust=True, progress=False)
    
    if df.empty:
        print(f"  ⚠ No data for {ticker}, skipping.")
        continue

    df = df.reset_index()
    df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
    df["Ticker"]  = ticker
    df["Company"] = info["name"]
    df["Sector"]  = info["sector"]

    # ── CALCULATED FIELDS ───────────────────────────────────
    df["Daily_Return_%"]      = df["Close"].pct_change() * 100
    df["Cumulative_Return_%"] = ((df["Close"] / df["Close"].iloc[0]) - 1) * 100
    df["MA_20"]               = df["Close"].rolling(window=20).mean()
    df["Price_vs_MA20"]       = df["Close"] - df["MA_20"]
    df["Volatility_20d"]      = df["Daily_Return_%"].rolling(window=20).std()

    all_data.append(df)

# ── COMBINE & EXPORT ───────────────────────────────────────
final_df = pd.concat(all_data, ignore_index=True)

final_df = final_df[[
    "Date", "Ticker", "Company", "Sector",
    "Open", "High", "Low", "Close", "Volume",
    "Daily_Return_%", "Cumulative_Return_%",
    "MA_20", "Price_vs_MA20", "Volatility_20d"
]]

final_df["Daily_Return_%"]      = final_df["Daily_Return_%"].round(4)
final_df["Cumulative_Return_%"] = final_df["Cumulative_Return_%"].round(4)
final_df["MA_20"]               = final_df["MA_20"].round(2)
final_df["Price_vs_MA20"]       = final_df["Price_vs_MA20"].round(2)
final_df["Volatility_20d"]      = final_df["Volatility_20d"].round(4)

output_file = "stock_data.csv"
final_df.to_csv(output_file, index=False)

print(f"\n✅ Done! {len(final_df)} rows saved to {output_file}")
print(f"📅 Date range: {START_DATE} → {END_DATE}")
print(f"📊 Tickers: {list(TICKERS.keys())}")