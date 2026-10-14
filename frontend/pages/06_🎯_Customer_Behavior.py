import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Customer Behavior", layout="wide")
st.title("🎯 Customer Behavior & Basket Size")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    fig = px.histogram(df, x='Quantity', title="Item Quantity Distribution per Transaction", nbins=50, range_x=[0, 50])
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")