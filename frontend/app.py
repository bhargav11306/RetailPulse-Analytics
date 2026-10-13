import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="RetailPulse - Executive Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 RetailPulse: Executive Summary Dashboard")
st.markdown("Use the vertical navigation menu on the left sidebar to switch between analytics pages.")

BASE_DIR = Path(__file__).resolve().parent.parent
tx_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"
rfm_path = BASE_DIR / "processed" / "Customer_RFM_Segments.csv"

if tx_path.exists() and rfm_path.exists():
    df_tx = pd.read_csv(tx_path)
    df_rfm = pd.read_csv(rfm_path)
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Revenue", f"${df_tx['TotalPrice'].sum():,.2f}")
    c2.metric("Total Orders", f"{df_tx['Invoice'].nunique():,}")
    c3.metric("Active Customers", f"{df_rfm['CustomerID'].nunique():,}")
    
    at_risk = len(df_rfm[df_rfm['Churn_Probability'] >= 0.70])
    c4.metric("At-Risk Customers", f"{at_risk:,}", delta="-High Risk", delta_color="inverse")
    
    st.markdown("---")
    st.subheader("Data Quality Verification")
    st.write(f"Loaded **{len(df_tx):,}** clean transactions across **{df_tx['Country'].nunique()}** countries.")
else:
    st.error("Missing cleaned CSV files in `processed/`. Please execute `python notebooks/01_preprocessing.py` first.")