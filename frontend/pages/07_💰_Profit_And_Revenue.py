import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Profit & Revenue", layout="wide")
st.title("💰 Revenue & Profit Margin Insights")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    df['EstimatedProfit'] = df['TotalPrice'] * 0.25  # Estimated 25% profit margin
    monthly_profit = df.groupby('YearMonth')[['TotalPrice', 'EstimatedProfit']].sum().reset_index()
    
    fig = px.line(monthly_profit, x='YearMonth', y=['TotalPrice', 'EstimatedProfit'], title="Gross Revenue vs Estimated Profit ($)")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv") 