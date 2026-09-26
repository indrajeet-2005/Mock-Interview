# 🚚 Delivery Delay Analysis — SQL & Data Analytics Project

<p align="center">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/SQL-Data%20Analysis-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL">
  <img src="https://img.shields.io/badge/Logistics-Analytics-FF6B35?style=for-the-badge" alt="Logistics Analytics">
  <img src="https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge" alt="Completed">
</p>

<p align="center">
  <b>📦 Delivery Performance • ⏱️ Delay Intelligence • 🛣️ Route Analytics • 🏢 Hub Performance</b>
</p>

---

## 🧭 Project Overview

**Delivery Delay Analysis** is a SQL-based logistics analytics project that transforms raw delivery and route data into actionable operational insights.

The project models delivery operations using a relational database and answers practical business questions such as:

- 🚛 Which service type accumulates the most delay?
- 🛣️ Which routes have significant delivery delays?
- 🏢 Which hubs contribute the highest total delay?
- 🔗 Are all delivery records correctly mapped to a valid route?
- ⏱️ How should delivery delay be calculated consistently?
- 📊 How can SQL turn operational records into decision-ready metrics?

The project follows a realistic analytics workflow:

```text
Raw CSV Data
     ↓
Relational Data Model
     ↓
Database & Table Creation
     ↓
Primary / Foreign Key Validation
     ↓
JOIN + Aggregation
     ↓
Delay KPI Calculation
     ↓
Business Questions
     ↓
Operational Insights
```

---

# 🎯 Business Problem

Delivery companies promise customers a specific delivery timeline. When actual delivery time exceeds the promised timeline, the business needs to identify the size and concentration of the delay.

### Core business question

> **Where is delivery performance falling behind promised timelines, and which operational segments should be investigated?**

This project answers that question using SQL rather than relying only on manual spreadsheet calculations.

---

# 🏆 Project Objectives

### Primary objectives

- 📌 Build a relational database for delivery analytics
- 🔗 Connect delivery transactions with route/service information
- 🧮 Calculate delivery delay using a consistent business rule
- 🚛 Compare Express and Standard service performance
- 🛣️ Identify routes with significant cumulative delay
- 🏢 Find the highest-delay hubs
- 🔍 Validate route-key integrity
- 📊 Produce business-ready SQL outputs

### Secondary objectives

- Demonstrate SQL JOIN proficiency
- Demonstrate `GROUP BY` and aggregate analysis
- Demonstrate `HAVING` for business thresholds
- Demonstrate conditional delay calculations
- Demonstrate primary-key / foreign-key data modeling
- Build reusable queries for operational reporting

---

# 🗂️ Project Architecture

```text
                         ┌────────────────────┐
                         │   routes table     │
                         ├────────────────────┤
                         │ route_id (PK)      │
                         │ route              │
                         │ service_type       │
                         └─────────┬──────────┘
                                   │
                                   │ 1 : Many
                                   │
                         ┌─────────▼──────────┐
                         │  deliveries table  │
                         ├────────────────────┤
                         │ record_id (PK)     │
                         │ month              │
                         │ route_id (FK)      │
                         │ hub                │
                         │ promised_days      │
                         │ actual_days        │
                         └────────────────────┘
```

### 🔑 Relationship

```text
routes.route_id
       │
       └──────────────► deliveries.route_id
```

One route can be associated with multiple delivery records.

---

# 🗃️ Data Model

## 🛣️ `routes`

| Column | Type | Key | Description |
|---|---|---|---|
| `route_id` | VARCHAR(10) | 🔑 PK | Unique route identifier |
| `route` | VARCHAR(100) | — | Route name |
| `service_type` | VARCHAR(30) | — | Express / Standard |

### Route master data

| Route ID | Route | Service |
|---|---|---|
| R1 | Metro Link | ⚡ Express |
| R2 | City Dash | ⚡ Express |
| R3 | Highway Freight | 📦 Standard |
| R4 | Rural Feeder | 📦 Standard |

---

## 📦 `deliveries`

| Column | Type | Key | Description |
|---|---|---|---|
| `record_id` | INT | 🔑 PK | Unique delivery record |
| `month` | VARCHAR(10) | — | Delivery month |
| `route_id` | VARCHAR(10) | 🔗 FK | Route reference |
| `hub` | VARCHAR(50) | — | Delivery hub |
| `promised_days` | INT | — | Promised delivery duration |
| `actual_days` | INT | — | Actual delivery duration |

---

# 📊 Dataset Snapshot

| Metric | Value |
|---|---:|
| 📦 Delivery records | **12** |
| 🛣️ Routes | **4** |
| 🏢 Hubs | **3** |
| 🚛 Service types | **2** |
| 📅 Months | **3** |
| ⏱️ Total delay days | **34** |
| 🚨 Delayed deliveries | **9** |
| 🎯 On-time deliveries | **3** |
| 📊 Average delay / delivery | **2.83 days** |
| 🔥 Maximum individual delay | **9 days** |

> **Note:** Delay metrics use `MAX(actual_days - promised_days, 0)`, so an early/on-time delivery contributes zero negative delay.

---

# 🧮 Core Business Logic

## ⏱️ Delay Days

The project uses the following business rule:

```sql
GREATEST(actual_days - promised_days, 0)
```

### Formula

```text
Delay Days = MAX(Actual Days − Promised Days, 0)
```

### Example

```text
Promised = 6 days
Actual   = 15 days

Delay = MAX(15 - 6, 0)
      = 9 days
```

For an on-time delivery:

```text
Promised = 3 days
Actual   = 3 days

Delay = MAX(3 - 3, 0)
      = 0 days
```

---

# 🧱 Database Setup

The project creates a dedicated database:

```sql
CREATE DATABASE delivery_delay_analysis;
USE delivery_delay_analysis;
```

The database contains two normalized tables:

```text
delivery_delay_analysis
│
├── routes
│
└── deliveries
```

---

# 🔐 Data Integrity

The project uses relational constraints to protect data quality.

### Primary keys

```sql
PRIMARY KEY (route_id)
PRIMARY KEY (record_id)
```

### Foreign key

```sql
FOREIGN KEY (route_id)
REFERENCES routes(route_id)
```

This ensures that delivery records reference valid routes.

---

# 🔎 SQL Analysis

## 1️⃣ Total Delay by Service Type

### Business Question

> Which service type contributes the highest total delay?

```sql
SELECT
    r.service_type,
    SUM(GREATEST(d.actual_days - d.promised_days, 0)) AS total_delay_days
FROM deliveries d
JOIN routes r
    ON d.route_id = r.route_id
GROUP BY r.service_type
ORDER BY total_delay_days DESC;
```

### Result

| Service Type | Total Delay |
|---|---:|
| 📦 Standard | **22 days** |
| ⚡ Express | **12 days** |

---

# 2️⃣ Routes with Significant Delay

### Business Question

> Which routes have more than 8 cumulative delay days?

```sql
SELECT
    d.route_id,
    r.route,
    SUM(GREATEST(d.actual_days - d.promised_days, 0)) AS total_delay_days
FROM deliveries d
JOIN routes r
    ON d.route_id = r.route_id
GROUP BY d.route_id, r.route
HAVING SUM(GREATEST(d.actual_days - d.promised_days, 0)) > 8
ORDER BY total_delay_days DESC;
```

### Result

| Route ID | Route | Total Delay |
|---|---|---:|
| R4 | Rural Feeder | **14 days** |
| R1 | Metro Link | **9 days** |

The query threshold identifies two routes above the defined **8-day cumulative delay** threshold.

---

# 3️⃣ Top Two Hubs by Delay

### Business Question

> Which two hubs have the highest cumulative delivery delay?

```sql
SELECT
    d.hub,
    SUM(GREATEST(d.actual_days - d.promised_days, 0)) AS total_delay_days
FROM deliveries d
GROUP BY d.hub
ORDER BY total_delay_days DESC, d.hub ASC
LIMIT 2;
```

### Result

| Rank* | Hub | Total Delay |
|---:|---|---:|
| 1 | Mumbai | **15 days** |
| 2 | Delhi | **14 days** |

\*The order shown here reflects the SQL query's descending delay output; it is not a recommendation or quality ranking.

---

# 🔍 4️⃣ Route-Key Diagnostic

Data relationships should be validated before relying on JOIN-based analysis.

```sql
SELECT d.route_id
FROM deliveries d
LEFT JOIN routes r
    ON d.route_id = r.route_id
WHERE r.route_id IS NULL;
```

### Expected interpretation

- **No rows returned** → all delivery route IDs have a matching route master record.
- **Rows returned** → unmatched route IDs require data-quality investigation.

This is a simple but important **referential-integrity diagnostic**.

---

# 📈 Analytical Summary

## 🏢 Delay by Hub

| Hub | Total Delay |
|---|---:|
| Mumbai | **15** |
| Delhi | **14** |
| Chennai | **5** |
| **Total** | **34** |

---

## 🛣️ Delay by Route

| Route | Route Name | Service | Total Delay |
|---|---|---|---:|
| R4 | Rural Feeder | Standard | **14** |
| R1 | Metro Link | Express | **9** |
| R3 | Highway Freight | Standard | **8** |
| R2 | City Dash | Express | **3** |

---

## 📅 Delay by Month

| Month | Total Delay |
|---|---:|
| Jan | **8** |
| Feb | **9** |
| Mar | **17** |
| **Total** | **34** |

March contains the largest accumulated delay in the available dataset.

---

# 🚨 Exception Analysis

The largest individual delivery delay is:

```text
Record ID : 12
Month     : Mar
Route     : R4
Hub       : Mumbai
Promised  : 6 days
Actual    : 15 days
Delay     : 9 days
```

This record can be treated as an operational exception for further investigation.

Other high-delay records include:

| Record | Route | Hub | Delay |
|---:|---|---|---:|
| 9 | R1 | Delhi | **6 days** |
| 7 | R3 | Delhi | **5 days** |
| 3 | R3 | Delhi | **3 days** |
| 4 | R4 | Mumbai | **4 days** |

> These records identify where the delay is concentrated; the current dataset does not contain enough operational variables to establish the cause of each delay.

---

# 💼 Business Interpretation

The SQL analysis provides several factual signals for operational investigation:

### 📦 Service-level signal

Standard deliveries account for **22 of 34 total delay days**, while Express deliveries account for **12**.

### 🛣️ Route-level signal

R4 / **Rural Feeder** contributes **14 delay days**, followed by R1 / **Metro Link** with **9**.

### 🏢 Hub-level signal

Mumbai and Delhi have **15** and **14** accumulated delay days respectively.

### 📅 Time signal

March contributes **17 of the 34 total delay days** in the dataset.

These observations can be used as starting points for deeper operational analysis.

---

# 🧠 Advanced Analytics Opportunities

The current SQL analysis can be extended into a larger analytics solution.

## 🐍 Python Layer

```text
CSV / SQL
   ↓
Pandas
   ↓
Data Cleaning
   ↓
EDA
   ↓
Outlier Detection
   ↓
Visualization
   ↓
Predictive Analysis
```

Potential additions:

- Distribution of delay days
- Route-level outlier detection
- Correlation analysis
- Statistical summaries
- Predictive delay classification

---

## 🗄️ SQL Layer

Potential production-level extensions:

- Stored procedures
- Views
- CTE-based reporting
- Window functions
- Date/calendar dimensions
- Automated KPI queries
- Data-quality monitoring
- Incremental loading

Example KPI view concept:

```sql
CREATE VIEW delivery_delay_kpi AS
SELECT
    d.record_id,
    d.month,
    d.route_id,
    d.hub,
    r.route,
    r.service_type,
    d.promised_days,
    d.actual_days,
    GREATEST(d.actual_days - d.promised_days, 0) AS delay_days
FROM deliveries d
JOIN routes r
    ON d.route_id = r.route_id;
```

---

# 📊 Power BI Dashboard Roadmap

This SQL dataset can be connected to Power BI to create an interactive logistics dashboard.

### KPI Cards

```text
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Total Rides  │ │ Delay Days   │ │ Avg Delay    │
│     12       │ │      34      │ │    2.83      │
└──────────────┘ └──────────────┘ └──────────────┘
```

### Recommended visuals

- 📊 Delay by Hub
- 🛣️ Delay by Route
- 🚛 Delay by Service Type
- 📅 Monthly Delay Trend
- 🚨 Top Delay Records
- 📦 Promised vs Actual Delivery
- 🔎 Route-level drill-down

### Recommended filters

- Month
- Hub
- Route
- Service Type
- Delay status

---

# 🛠️ Technology Stack

| Technology | Role |
|---|---|
| 🐬 **MySQL** | Relational database |
| 🧮 **SQL** | Data querying & analysis |
| 📄 **CSV** | Source data |
| 🐍 **Python** | Future advanced analytics |
| 📊 **Power BI** | Future dashboard layer |
| 📚 **Git / GitHub** | Project version control |

---

# 📁 Repository Structure

```text
Delivery-Delay-Analysis/
│
├── 📄 setup.sql
│   └── Database + table creation + sample data
│
├── 🔎 queries.sql
│   └── Business analysis queries
│
├── 📦 deliveries.csv
│   └── Delivery transaction data
│
├── 🛣️ routes.csv
│   └── Route master data
│
└── 📘 README.md
    └── Project documentation
```

---

# ▶️ How to Run the Project

## Step 1 — Install MySQL

Use any MySQL-compatible environment such as:

- MySQL Workbench
- MySQL Command Line Client
- MySQL Server

## Step 2 — Create the database

Run:

```sql
source setup.sql;
```

Or open `setup.sql` in MySQL Workbench and execute it.

## Step 3 — Run the analysis

Open:

```text
queries.sql
```

Execute the queries individually to reproduce the analysis.

## Step 4 — Review results

The SQL outputs provide:

```text
Service-level delay
        ↓
Route-level exceptions
        ↓
Hub-level concentration
        ↓
Data-integrity validation
```

---

# 🧪 Data Quality Checklist

| Check | Purpose |
|---|---|
| 🔑 Primary key validation | Prevent duplicate identifiers |
| 🔗 Foreign key validation | Maintain route relationships |
| 🧩 Unmatched-key query | Detect broken mappings |
| ➖ Negative delay protection | Prevent negative delay totals |
| 📊 Aggregate validation | Confirm summary calculations |
| 🔎 Exception review | Identify extreme delays |

---

# 📌 Key Metrics

| KPI | Value |
|---|---:|
| 📦 Total deliveries | **12** |
| ⏱️ Total delay | **34 days** |
| 📊 Average delay | **2.83 days** |
| 🚨 Delayed deliveries | **9 / 12** |
| 🎯 On-time deliveries | **3 / 12** |
| 🔥 Maximum delay | **9 days** |
| 🏢 Highest hub total | **Mumbai — 15 days** |
| 🛣️ Highest route total | **R4 — 14 days** |
| 📦 Highest service total | **Standard — 22 days** |
| 📅 Highest monthly total | **March — 17 days** |

---

# 🎓 Skills Demonstrated

### SQL Fundamentals

`SELECT` • `WHERE` • `JOIN` • `GROUP BY` • `HAVING` • `ORDER BY` • `LIMIT`

### SQL Analytics

`SUM()` • `GREATEST()` • Aggregation • Conditional KPI logic

### Database Concepts

`CREATE DATABASE` • `CREATE TABLE` • `PRIMARY KEY` • `FOREIGN KEY` • Relational modeling

### Data Analytics

`KPI Development` • `Exception Analysis` • `Trend Analysis` • `Segmentation` • `Data Validation`

### Business Intelligence

`Business Questions` • `Operational Insights` • `Reporting Logic` • `Dashboard Planning`

---

# 🌱 Future Project Evolution

```text
                   ┌───────────────┐
                   │   CSV DATA    │
                   └───────┬───────┘
                           ↓
                   ┌───────────────┐
                   │     MySQL     │
                   │  Data Model   │
                   └───────┬───────┘
                           ↓
                   ┌───────────────┐
                   │    Python     │
                   │   Analytics   │
                   └───────┬───────┘
                           ↓
                   ┌───────────────┐
                   │   Power BI    │
                   │   Dashboard   │
                   └───────┬───────┘
                           ↓
                   ┌───────────────┐
                   │   Business    │
                   │   Insights    │
                   └───────────────┘
```

The project can therefore evolve from a **SQL portfolio exercise** into a complete **end-to-end logistics analytics pipeline**.

---

# 👨‍💻 Author

## Indrajeet Maheshwari

🎓 B.Tech Computer Science Student  
📊 Aspiring Data Analyst  
💻 Data Analytics & Business Intelligence Enthusiast

### Skills

`SQL` `MySQL` `Python` `Power BI` `Excel` `Data Analytics` `Business Intelligence`

---

# ⭐ Project Highlights

```text
┌────────────────────────────────────────────────────┐
│                 DELIVERY ANALYTICS                 │
├────────────────────────────────────────────────────┤
│ 📦 12 Delivery Records                             │
│ 🛣️ 4 Routes                                       │
│ 🏢 3 Hubs                                          │
│ 🚛 2 Service Types                                 │
│ ⏱️ 34 Total Delay Days                             │
│ 🚨 9 Delayed Deliveries                            │
│ 📊 2.83 Average Delay Days                         │
│ 🔥 9-Day Maximum Individual Delay                  │
└────────────────────────────────────────────────────┘
```

---

## 📜 License

This project is intended for **educational, portfolio, and data-analytics demonstration purposes**.

---

<p align="center">

### 🚚 From Raw Delivery Records to SQL-Powered Insights 📊

**Built with SQL • Data • Analytics • Curiosity**

**© Indrajeet Maheshwari**

</p>
