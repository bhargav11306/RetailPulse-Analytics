import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# 1. Page Configuration
st.set_page_config(page_title="RetailPulse Dashboard", layout="wide", page_icon="🛍️")

# 2. Custom CSS Animations (Hover effects & fade-in)
st.markdown("""
    <style>
    /* Metric Card Styling & Hover Animation */
    div[data-testid="stMetric"] {
        background-color: #1e222d;
        border: 1px solid #2e364f;
        padding: 18px;
        border-radius: 12px;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-6px);
        border-color: #ff4b4b;
        box-shadow: 0px 8px 20px rgba(255, 75, 75, 0.25);
    }
    
    /* Fade-In Header Animation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .main-title {
        animation: fadeIn 0.8s ease-in-out;
        font-size: 2.2rem;
        font-weight: 700;
        color: #FFFFFF;
    }
    </style>
    <h1 class="main-title">🛍️ RetailPulse Executive Analytics</h1>
""", unsafe_allow_html=True)

st.markdown("Welcome to the RetailPulse AI Analytics & Demand Platform.")

# 3. Data Processing
BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    
    # Auto-detect Customer ID column name
    cust_col = next((col for col in ['CustomerID', 'Customer_ID', 'Customer ID'] if col in df.columns), None)
    unique_custs = df[cust_col].nunique() if cust_col else "N/A"
    
    # Display animated metric cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Transactions", f"{len(df):,}")
    col2.metric("Total Revenue", f"${df['TotalPrice'].sum():,.2f}")
    col3.metric("Unique Customers", f"{unique_custs:,}" if isinstance(unique_custs, int) else unique_custs)
    col4.metric("Avg Order Value", f"${df['TotalPrice'].mean():,.2f}")

    st.subheader("📊 Executive Revenue Trajectory")
    
    with st.spinner("🔄 Loading animated revenue insights..."):
        if 'YearMonth' in df.columns:
            monthly_sales = df.groupby('YearMonth')['TotalPrice'].sum().reset_index()
            fig = px.line(monthly_sales, x='YearMonth', y='TotalPrice', markers=True, title="Monthly Revenue ($)")
            fig.update_layout(template="plotly_dark", transition_duration=500)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.dataframe(df.head(50), use_container_width=True)
else:
    st.warning("⚠️ Cleaned data file not found in `processed/RetailPulse_Cleaned_Transactions.csv`.")