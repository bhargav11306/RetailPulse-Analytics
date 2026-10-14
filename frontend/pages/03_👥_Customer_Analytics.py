import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Customer Analytics", layout="wide")
st.title("👥 Customer Analytics & RFM Segmentation")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    
    # Auto-detect column names dynamically
    cust_col = next((col for col in ['CustomerID', 'Customer_ID', 'Customer ID'] if col in df.columns), None)
    inv_col = next((col for col in ['InvoiceNo', 'Invoice_No', 'Invoice', 'InvoiceNumber'] if col in df.columns), None)
    price_col = next((col for col in ['TotalPrice', 'Total_Price', 'Price', 'Amount'] if col in df.columns), df.columns[0])
    
    if cust_col and inv_col:
        cust_df = df.groupby(cust_col).agg(
            TotalSpend=(price_col, 'sum'),
            OrderCount=(inv_col, 'nunique')
        ).reset_index()
        
        fig = px.scatter(
            cust_df, 
            x='OrderCount', 
            y='TotalSpend', 
            title="Customer Spend vs Order Frequency", 
            hover_data=[cust_col]
        )
        st.plotly_chart(fig, use_container_width=True)
    elif cust_col:
        cust_df = df.groupby(cust_col)[price_col].sum().reset_index()
        fig = px.bar(cust_df.head(20), x=cust_col, y=price_col, title="Top Customer Spend ($)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Customer data format preview:")
        st.dataframe(df.head(50), use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")