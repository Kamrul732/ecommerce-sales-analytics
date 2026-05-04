# E-Commerce Sales Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)

An end-to-end sales analytics pipeline analyzing 397,884 transactions 
from a UK-based online retailer using Python, SQL, and Streamlit.

## 🚀 [Live Dashboard](https://ecommerce-sales-analytics-memp9dwcgg9emuj7envvox.streamlit.app/)

## Key Insights
- **UK dominates** — 82% of total revenue comes from United Kingdom
- **Q4 surge** — November peak driven by holiday season demand
- **Whale customers** — Netherlands has only 9 customers but $285K revenue
- **Thursday peak** — Highest revenue day, suggesting B2B buying patterns
- **144,025 dirty rows removed** — cancelled orders, returns, guest checkouts

## Tech Stack
- **Python** — data collection, cleaning, analysis
- **Pandas** — data wrangling and transformation
- **SQLite + SQL** — data storage and business queries
- **Matplotlib & Seaborn** — static visualizations
- **Plotly** — interactive charts
- **Streamlit** — live web dashboard

## How to Run Locally
1. Clone the repo
```bash
   git clone https://github.com/Kamrul732/ecommerce-sales-analytics.git
   cd ecommerce-sales-analytics
```
2. Create virtual environment
```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```
3. Run the app
```bash
   streamlit run app.py
```

## Data Source
UCI Machine Learning Repository — Online Retail Dataset
541,909 transactions | 38 countries | Dec 2010 – Dec 2011