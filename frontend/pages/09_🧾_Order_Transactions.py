import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Order Transactions", layout="wide")
st.title("🧾 Transaction Data Explorer")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    st.dataframe(df.head(100), use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")