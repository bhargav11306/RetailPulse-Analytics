import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Regional Sales", layout="wide")
st.title("🌍 Regional & Country Performance")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    country_sales = df.groupby('Country')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False)
    
    st.subheader("Top Revenue Markets")
    fig = px.bar(country_sales.head(10), x='Country', y='TotalPrice', title="Top 10 Revenue by Country ($)", color='TotalPrice')
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(country_sales, use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")