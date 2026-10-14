import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Product Performance", layout="wide")
st.title("🏷️ Product Performance & Best Sellers")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    top_products = df.groupby('Description')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False).head(10)
    fig = px.bar(top_products, x='TotalPrice', y='Description', orientation='h', title="Top 10 Products by Total Revenue ($)", color='TotalPrice')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")