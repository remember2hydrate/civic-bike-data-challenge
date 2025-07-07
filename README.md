# civic-bike-data-challenge
This project simulates delivering an end-to-end cloud data solution for a public sector client (e.g., Copenhagen municipality), meeting all expectations in a Senior Data Engineer job description.


## 🚀 Stack

| Component                | Tool                                         |
|--------------------------|----------------------------------------------|
| Data Ingestion           | Python (`requests`, `pandas`)                |
| Cloud Platform           | Google Cloud Platform (Free Tier used)       |
| Storage                  | Google Cloud Storage (raw) + BigQuery        |
| Processing Engine        | PySpark                                      |
| Visualization            | Streamlit / Google Looker Studio             |
| Data Orchestration       | Manual script run / cron (simulated Airflow) |
| Testing                  | Python `unittest`                            |

---

## 🧪 How to Run

### Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the pipeline
```bash
python data_pipeline.py
```

### Launch dashboard
```bash
streamlit run dashboard_app.py
```

---

## Interview Description Match Checklist

| Requirement                                 | Covered in Project? |
|---------------------------------------------|----------------------|
| MS Fabric / SAS (platform experience)       | Simulated via BigQuery |
| Azure / AWS / GCP                           | GCP used throughout  |
| Databricks / Spark / Kafka                  | PySpark used         |
| SQL, Python, R                              | SQL + Python         |
| Agile methodology                           | `mock_user_stories.md` written |
| Consultancy mindset                         | Project framed as client delivery |
| Public sector context                       | Civic bike data case |

---
Created and revised with AI assistance for clarity and structure.
