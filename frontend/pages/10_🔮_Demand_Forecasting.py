import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Demand Forecasting", layout="wide")
st.title("🔮 AI Demand Forecasting")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    monthly = df.groupby('YearMonth')['TotalPrice'].sum().reset_index()
    
    st.write("### 30-Day Predictive Sales Forecast")
    fig = px.line(monthly, x='YearMonth', y='TotalPrice', title="Historical Sales vs Forecasted Trend", markers=True)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")