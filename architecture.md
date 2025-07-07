# Architecture Overview

This document outlines the end-to-end architecture for the `civic-bike-data-challenge` project. It covers all technical layers used to simulate a real-world data engineering solution on a cloud platform.

---

## System Context
The system is designed to support public sector analytics needs — in this case, daily bike traffic metrics for urban planning. It simulates a production-grade data platform using Google Cloud tools, Python, and open-source frameworks.

---

## Component Breakdown

| Component                | Tool                                         |
|--------------------------|----------------------------------------------|
| **Data Ingestion**       | Python (`requests`, `pandas`)                |
| **Cloud Platform**       | Google Cloud Platform (Free Tier used)       |
| **Storage**              | Google Cloud Storage (raw) + BigQuery        |
| **Processing Engine**    | PySpark                                      |
| **Visualization**        | Streamlit / Google Looker Studio             |
| **Data Orchestration**   | Manual script run / cron (simulated Airflow) |
| **Testing**              | Python `unittest`                            |

---

## 🔄 Data Flow

1. **Ingestion**:
   - Raw CSV/JSON data is fetched from public sources using Python.
   - Temporarily stored in-memory and optionally written to a local temp file.

2. **Raw Data Storage**:
   - Raw files uploaded to Google Cloud Storage (GCS) in a structured bucket layout (e.g., `/raw/bike/YYYY/MM/DD`).

3. **Transformation**:
   - PySpark jobs clean and normalize data (e.g., timestamp parsing, missing values).
   - Resulting DataFrames are written to BigQuery with partitioning enabled.

4. **Storage & Query**:
   - BigQuery acts as the data warehouse and main analytical store.
   - Tables are organized by domain (e.g., `bike_traffic_events`, `aggregated_daily_counts`).

5. **Visualization**:
   - Streamlit or Google Looker Studio connects to BigQuery to expose:
     - Daily/weekly trends
     - Heatmaps of traffic times
     - Rolling averages for planners

6. **Orchestration**:
   - Scripts are run manually or via cron.
   - Each script performs atomic steps: ingest → transform → load → notify.

7. **Testing**:
   - Validation scripts ensure schema consistency and check for nulls or anomalies.

---

## Cloud Configuration
- **GCP Project**: `civic-bike-insights`
- **Bucket Name**: `civic-bike-data-raw`
- **BigQuery Dataset**: `bike_analytics`
- **Permissions**:
  - Service account with Storage Admin & BigQuery Data Editor
  - IAM roles limited per module for best practice simulation

---

## Scalability Notes
- PySpark jobs are built to scale from local to Google Cloud Dataproc (optional upgrade).
- BigQuery handles large-scale queries natively with automatic indexing and partitioning.
- Modular pipeline structure allows integration with Airflow or Cloud Functions for automation.

---

## Design Rationale
- **GCP** chosen for easy setup and free-tier flexibility
- **BigQuery** to avoid setting up a DB engine and to mimic MS Fabric-like data warehousing
- **Streamlit** to simulate an interactive internal tool a client might request
- **PySpark** prepares you for Databricks or Hadoop-style workloads

---

> Architecture designed to meet Senior Data Engineer expectations. All tools selected for cloud realism and cost-effective testing.
