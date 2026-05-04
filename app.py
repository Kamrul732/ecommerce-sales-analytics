import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 E-Commerce Sales Analytics Dashboard")
st.markdown("Analyzing **397,884 transactions** from a UK-based online retailer (2010–2011)")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/online_retail_clean.csv", parse_dates=["InvoiceDate"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

countries = ["All"] + sorted(df["Country"].unique().tolist())
selected_country = st.sidebar.selectbox("Select Country", countries)

months = ["All"] + sorted(df["Month"].unique().tolist())
selected_month = st.sidebar.selectbox("Select Month", months)

# Apply filters
filtered = df.copy()
if selected_country != "All":
    filtered = filtered[filtered["Country"] == selected_country]
if selected_month != "All":
    filtered = filtered[filtered["Month"] == selected_month]

# KPI Cards
st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)

total_revenue = filtered["Revenue"].sum()
total_orders = filtered["InvoiceNo"].nunique()
total_customers = filtered["CustomerID"].nunique()
avg_order = filtered.groupby("InvoiceNo")["Revenue"].sum().mean()

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Unique Customers", f"{total_customers:,}")
col4.metric("Avg Order Value", f"${avg_order:,.0f}")

st.divider()

# Chart 1 — Monthly Revenue
st.subheader("Monthly Revenue Trend")
monthly = filtered.groupby(["Year", "Month"])["Revenue"].sum().reset_index()
monthly["date"] = pd.to_datetime(monthly[["Year", "Month"]].assign(day=1))
fig1 = px.line(monthly, x="date", y="Revenue",
               color_discrete_sequence=["#185FA5"],
               labels={"Revenue": "Revenue ($)", "date": "Month"})
fig1.update_layout(showlegend=False)
st.plotly_chart(fig1, use_container_width=True)

# Chart 2 — Revenue by Country
st.subheader("Revenue by Country (Top 10)")
country_rev = filtered.groupby("Country")["Revenue"].sum().reset_index()
country_rev = country_rev.sort_values("Revenue", ascending=False).head(10)
fig2 = px.bar(country_rev, x="Revenue", y="Country",
              orientation="h",
              color_discrete_sequence=["#0F6E56"],
              labels={"Revenue": "Total Revenue ($)"})
fig2.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig2, use_container_width=True)

col1, col2 = st.columns(2)

# Chart 3 — Top Products
with col1:
    st.subheader("Top 10 Products")
    top_products = filtered.groupby("Description")["Revenue"].sum().reset_index()
    top_products = top_products[~top_products["Description"].isin(["POSTAGE", "Manual"])]
    top_products = top_products.sort_values("Revenue", ascending=False).head(10)
    fig3 = px.bar(top_products, x="Revenue", y="Description",
                  orientation="h",
                  color_discrete_sequence=["#534AB7"])
    fig3.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig3, use_container_width=True)

# Chart 4 — Revenue by Day
with col2:
    st.subheader("Revenue by Day of Week")
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday']
    day_rev = filtered.groupby("DayOfWeek")["Revenue"].sum().reindex(day_order).reset_index()
    fig4 = px.bar(day_rev, x="DayOfWeek", y="Revenue",
                  color_discrete_sequence=["#854F0B"],
                  labels={"Revenue": "Total Revenue ($)", "DayOfWeek": "Day"})
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# Key Insights
st.subheader("Key Insights")
col1, col2 = st.columns(2)

with col1:
    st.info("🇬🇧 **UK dominates** — 82% of total revenue comes from the United Kingdom")
    st.info("📅 **Q4 surge** — November is the peak month, driven by holiday season demand")

with col2:
    st.warning("🐳 **Whale customers** — Netherlands has only 9 customers but $285K revenue")
    st.warning("📦 **Thursday peak** — Highest revenue day, suggesting B2B buying patterns")

st.divider()
st.caption("Data source: UCI Machine Learning Repository — Online Retail Dataset")