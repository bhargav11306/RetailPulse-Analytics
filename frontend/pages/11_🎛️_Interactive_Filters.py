import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Interactive Filters", layout="wide")
st.title("🎛️ Interactive Data Filter")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    country_list = df['Country'].unique().tolist()
    selected_country = st.selectbox("Select Country Filter:", country_list)
    
    filtered_df = df[df['Country'] == selected_country]
    st.write(f"Showing **{len(filtered_df)}** records for **{selected_country}**:")
    st.dataframe(filtered_df.head(50), use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")