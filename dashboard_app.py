import streamlit as st
import pandas as pd
import os
from google.cloud import bigquery
from google.oauth2 import service_account

# Config
CLEAN_DATA_DIR = "data/cleaned"
PROJECT_ID = "your-gcp-project-id"
DATASET_ID = "bike_data"
TABLE_ID = "traffic_counts"

# Load data from BigQuery if possible, otherwise fallback to latest local CSV
def load_data():
    try:
        encoded_key = st.secrets["GCP_CREDENTIALS_B64"]
        decoded_json = base64.b64decode(encoded_key).decode("utf-8")
        credentials_info = json.loads(decoded_json)

        credentials = service_account.Credentials.from_service_account_info(credentials_info)
        client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

        query = f"""
        SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
        WHERE timestamp IS NOT NULL
        ORDER BY timestamp DESC
        LIMIT 10000
        """
        df = client.query(query).to_dataframe()
        return df
    except Exception as e:
        st.warning(f"Could not connect to BigQuery: {e}")
        st.info("Falling back to latest local cleaned CSV.")
        files = sorted([f for f in os.listdir(CLEAN_DATA_DIR) if f.endswith(".csv")])
        if not files:
            st.error("No local data files found.")
            return pd.DataFrame()
        df = pd.read_csv(os.path.join(CLEAN_DATA_DIR, files[-1]), parse_dates=["timestamp"])
        return df

# App
st.title("🚲 Copenhagen Bike Traffic Dashboard")
st.markdown("This dashboard visualizes bike count data from open civic datasets.")

df = load_data()

if df.empty:
    st.stop()

# Filters
min_date = df["timestamp"].min()
max_date = df["timestamp"].max()
date_range = st.date_input("Select date range", [min_date, max_date])

if len(date_range) == 2:
    df = df[(df["timestamp"] >= pd.to_datetime(date_range[0])) & (df["timestamp"] <= pd.to_datetime(date_range[1]))]

# KPIs
st.subheader("📊 Key Stats")
col1, col2 = st.columns(2)
col1.metric("Total Records", len(df))
col2.metric("Total Bike Count", int(df["bike_count"].sum()))

# Time Series
st.subheader("📈 Bike Counts Over Time")
df_hourly = df.copy()
df_hourly["hour"] = df_hourly["timestamp"].dt.floor("H")
hourly_counts = df_hourly.groupby("hour")["bike_count"].sum().reset_index()
st.line_chart(hourly_counts.rename(columns={"hour": "index"}).set_index("index"))

# Top Locations
st.subheader("🚦 Top Streets by Bike Count")
top_streets = df.groupby("street_name")["bike_count"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_streets)

# Optional Export
st.download_button("Download Displayed Data", df.to_csv(index=False), file_name="bike_data_filtered.csv")

st.caption("Data source: [Opendata.dk](https://admin.opendata.dk)")
