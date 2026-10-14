import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Seasonality Analysis", layout="wide")
st.title("📅 Monthly & Weekly Seasonality Trends")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
    
    day_sales = df.groupby('DayOfWeek')['TotalPrice'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).reset_index()
    fig = px.line(day_sales, x='DayOfWeek', y='TotalPrice', title="Revenue Distribution by Day of Week", markers=True)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")