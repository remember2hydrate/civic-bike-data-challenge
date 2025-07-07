# Mock User Stories – Civic Bike Data Platform

This document outlines simulated user stories used to plan and build the data platform for Copenhagen’s public bike traffic analysis.

---

## Epic: As a municipality data analyst, I want to understand bike usage trends, so I can support infrastructure decisions.

---

### ✅ User Story 1 – Ingest Civic Data

**As** a Data Engineer  
**I want** to ingest bike count data from the [Opendata.dk datastore API](https://admin.opendata.dk)  
**So that** we can centralize and process raw civic transport data.

- Acceptance Criteria:
  - Data is pulled using the `resource_id=50f7a383-653a-4860-bb4e-306f221a2d2a`
  - First version should store results locally as raw JSON/CSV
  - Later version should push raw files to Google Cloud Storage

---

### ✅ User Story 2 – Clean and Transform Data

**As** a Data Engineer  
**I want** to validate and normalize raw bike traffic data  
**So that** it’s suitable for analysis in BigQuery.

- Acceptance Criteria:
  - Missing or malformed timestamps are dropped or corrected
  - Station names are standardized
  - Output is written to BigQuery in a structured table

---

### ✅ User Story 3 – Build Queryable Dataset in BigQuery

**As** a Data Analyst  
**I want** the processed data to be available in BigQuery  
**So that** I can run SQL queries for reporting and exploration.

- Acceptance Criteria:
  - Table schema includes timestamp, station, direction, count
  - Queries like “bike counts per hour” or “top 5 stations” return accurate results

---

### ✅ User Story 4 – Build Insights Dashboard

**As** a Policy Advisor  
**I want** to view bike traffic KPIs and trends in a dashboard  
**So that** I can present visual findings to stakeholders.

- Acceptance Criteria:
  - Show total daily/weekly bike counts
  - Graph busiest hours and top-performing locations
  - Deployed via Streamlit or Google Looker Studio

---

### ✅ User Story 5 – Schedule Data Refresh

**As** a Technical Stakeholder  
**I want** the data pipeline to run automatically every day  
**So that** our dashboards always show fresh data.

- Acceptance Criteria:
  - Python script scheduled via cron or simulated orchestration
  - Logs success/failure to terminal or file

---

### ✅ User Story 6 – Validate Ingested Data

**As** a QA Engineer  
**I want** automated checks on the ingested dataset  
**So that** data issues are caught early.

- Acceptance Criteria:
  - Unit tests verify presence of critical fields
  - Schema consistency is enforced
  - Record count > 0

---

### ✅ User Story 7 – Demonstrate Tech Stack to Client

**As** a Consultant  
**I want** to document the stack and decisions  
**So that** Sopra Steria stakeholders and clients can understand the architecture.

- Acceptance Criteria:
  - Include detailed `architecture.md`
  - README includes how to run, test, and access dashboard
  - GitHub repository is structured and readable

---

## Notes

- Initial data exploration via:
  - [Base query](https://admin.opendata.dk/api/3/action/datastore_search?resource_id=50f7a383-653a-4860-bb4e-306f221a2d2a&limit=5)
  - [Search by field](https://admin.opendata.dk/api/3/action/datastore_search?q=jones&resource_id=50f7a383-653a-4860-bb4e-306f221a2d2a)
  - [SQL](https://admin.opendata.dk/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%2250f7a383-653a-4860-bb4e-306f221a2d2a%22%20WHERE%20title%20LIKE%20%27jones%27)

