import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Inventory Risk", layout="wide")
st.title("📦 Inventory & Stock Risk Analysis")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    stock_df = df.groupby('StockCode').agg(TotalQty=('Quantity', 'sum')).reset_index().sort_values(by='TotalQty', ascending=True).head(15)
    
    fig = px.bar(stock_df, x='StockCode', y='TotalQty', title="Low Turnover / Low Stock Items", color='TotalQty')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")