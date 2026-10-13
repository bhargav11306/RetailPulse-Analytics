import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Sales Trends", layout="wide")
st.title("📈 Sales Performance & Revenue Trends")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
tx_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if tx_path.exists():
    df_tx = pd.read_csv(tx_path)
    monthly = df_tx.groupby('YearMonth')['TotalPrice'].sum().reset_index()
    fig = px.line(monthly, x='YearMonth', y='TotalPrice', title="Monthly Sales Revenue Trajectory ($)", markers=True)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Data file not found. Ensure RetailPulse_Cleaned_Transactions.csv exists in processed/.")