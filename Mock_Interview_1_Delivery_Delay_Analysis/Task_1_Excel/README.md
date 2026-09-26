# 🚚 Delivery Delay Analysis
### 📦 Logistics Performance • Delay Intelligence • Operational Analytics

<p align="center">
  <img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" alt="Excel">
  <img src="https://img.shields.io/badge/Data%20Cleaning-0F9D58?style=for-the-badge&logo=databricks&logoColor=white" alt="Data Cleaning">
  <img src="https://img.shields.io/badge/Business%20Analytics-4285F4?style=for-the-badge&logo=googleanalytics&logoColor=white" alt="Business Analytics">
  <img src="https://img.shields.io/badge/Status-Completed-6A1B9A?style=for-the-badge" alt="Completed">
</p>

---

## 📌 Executive Overview

**Delivery Delay Analysis** is an end-to-end logistics analytics project designed to convert raw delivery records into actionable operational insights.

The project focuses on identifying **where delivery delays occur, how delays vary across hubs and service types, and how delay patterns change over time**.

The workflow covers the complete analytical lifecycle:

> **Raw Data → Data Validation → Cleaning → Transformation → KPI Analysis → Operational Insights**

This project is designed as a practical **Data Analyst portfolio project** and demonstrates how spreadsheet-based analytics can support logistics and delivery-performance decisions.

---

## 🎯 Business Objective

The core business problem is simple:

> **How can a logistics operation identify delivery delays quickly and understand which operational segments require further investigation?**

### Key objectives

- ⏱️ Measure delivery delays against promised timelines
- 🏢 Compare delay performance across delivery hubs
- 🚛 Compare Express vs Standard services
- 📅 Identify monthly delay trends
- 🔍 Detect high-delay delivery records
- 🧹 Build a reliable cleaned analytical dataset
- 📊 Convert raw operational data into business-ready insights

---

## 🧠 Analytical Framework

```text
┌───────────────────────┐
│   Raw Delivery Data   │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Data Quality Checks   │
│ • Duplicates         │
│ • Missing/invalid    │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Data Transformation   │
│ • Route Mapping      │
│ • Service Mapping    │
│ • Delay Calculation  │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Clean Analytical Data │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ KPI & Trend Analysis  │
│ • Hub                 │
│ • Service Type        │
│ • Month               │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ Business Insights     │
└───────────────────────┘
```

---

## 📂 Project Structure

```text
Delivery-Delay-Analysis/
│
├── 📊 Delivery Delay Analysis.xlsx
│   ├── Raw
│   ├── Lookup
│   ├── Clean
│   └── Summary
│
├── 📄 deliveries.csv
├── 🛣️ routes.csv
└── 📘 README.md
```

---

## 🗃️ Data Architecture

### 📦 Delivery Dataset

The delivery data contains operational fields such as:

| Field | Purpose |
|---|---|
| `record_id` | Unique delivery identifier |
| `month` | Delivery month |
| `route_id` | Route identifier |
| `hub` | Delivery hub |
| `promised_days` | Customer-promised delivery duration |
| `actual_days` | Actual delivery duration |

### 🛣️ Route Lookup Dataset

The route lookup provides additional route/service information used to enrich the delivery records.

| Field | Purpose |
|---|---|
| `route_id` | Route identifier |
| `service_type` | Express / Standard classification |

---

## 🧹 Data Cleaning & Preparation

A strong analytics project starts with reliable data.

### Cleaning workflow

**01 — Duplicate Validation**  
Duplicate delivery records were identified and removed from the analytical dataset.

**02 — Route Enrichment**  
Route information was matched with the lookup table to identify service type.

**03 — Delay Calculation**  
Delivery delay was calculated using promised and actual delivery duration.

**04 — Analytical Validation**  
The cleaned dataset was checked before creating summary-level insights.

### 📊 Cleaning Result

| Metric | Result |
|---|---:|
| Raw records | **13** |
| Clean records | **12** |
| Duplicate records removed | **1** |
| Total delay days | **34** |

---

## 🧮 Core KPI Definition

### ⏱️ Delay Days

```text
Delay Days = Actual Days − Promised Days
```

### Example

```text
Promised Delivery = 3 Days
Actual Delivery   = 5 Days

Delay = 5 − 3
      = 2 Days
```

This KPI provides the foundation for hub, service, route, and monthly delay analysis.

---

# 📊 Key Performance Insights

## 🏢 Hub-Level Delay

| Hub | Total Delay |
|---|---:|
| 🔴 Delhi | **15 days** |
| 🟠 Mumbai | **14 days** |
| 🟢 Chennai | **5 days** |
| **TOTAL** | **34 days** |

**Analytical observation:** Delhi has the largest total delay contribution in the analyzed dataset.

---

## 🚛 Service-Type Analysis

| Service Type | Total Delay |
|---|---:|
| ⚡ Express | **12 days** |
| 📦 Standard | **22 days** |
| **TOTAL** | **34 days** |

Standard-service records account for the larger share of total delay days in this dataset.

---

## 📅 Monthly Delay Trend

| Service Type | January | February | March | Total |
|---|---:|---:|---:|---:|
| ⚡ Express | 1 | 3 | 8 | **12** |
| 📦 Standard | 7 | 6 | 9 | **22** |
| **TOTAL** | **8** | **9** | **17** | **34** |

### 📈 Trend Signal

```text
January   ████████  8
February  █████████ 9
March     █████████████████ 17
```

March records the highest total delay in the available analysis period.

---

# 🚨 High-Delay Exceptions

Exception analysis helps operations teams focus on the records that require deeper investigation.

| Record | Month | Route | Hub | Promised | Actual | Delay |
|---:|---|---|---|---:|---:|---:|
| 3 | Jan | R3 | Delhi | 6 | 10 | 🔴 **4** |
| 7 | Feb | R3 | Delhi | 5 | 10 | 🔴 **5** |
| 9 | Mar | R1 | Delhi | 2 | 8 | 🔴 **6** |
| 12 | Mar | R4 | Mumbai | 6 | 15 | 🔴 **9** |

### 🔎 Why exception analysis matters

Large-delay records can be investigated against operational factors such as:

- Route congestion
- Hub processing time
- Capacity constraints
- Transit conditions
- Delivery scheduling
- Service-level planning

> ⚠️ These factors are potential investigation areas, not proven causes from the current dataset.

---

# 📌 KPI Dashboard Blueprint

If this project is converted into a Power BI or advanced Excel dashboard, the following KPI cards would provide a strong executive view:

| KPI | Purpose |
|---|---|
| 📦 Total Deliveries | Overall delivery volume |
| ⏱️ Total Delay Days | Total accumulated delay |
| 📊 Average Delay | Typical delay magnitude |
| 🚨 Delayed Deliveries | Number of late deliveries |
| 🎯 On-Time % | Service performance |
| 🔥 Maximum Delay | Largest individual delay |
| 🏢 Top Delay Hub | Hub requiring investigation |
| 🚛 Service Delay | Express vs Standard comparison |

---

# 📈 Recommended Dashboard Visuals

### Executive KPI Cards
Display the most important performance indicators at the top.

### Hub Performance
Use a horizontal bar chart to compare total delay by hub.

### Monthly Trend
Use a line or column chart to show delay movement across months.

### Service Comparison
Use a clustered column chart comparing Express and Standard delays.

### Exception Table
Highlight deliveries with the highest delay values.

### Route Analysis
Compare average and total delay across routes.

---

# 🛠️ Tools & Skills

### 🟩 Microsoft Excel
- Data cleaning
- Data validation
- Lookup functions
- Formula-based calculations
- Summary analysis
- Pivot-style reporting

### 📊 Data Analytics
- KPI development
- Trend analysis
- Segmentation
- Exception analysis
- Operational performance analysis

### 💼 Business Intelligence
- Business problem framing
- Insight generation
- Data storytelling
- Decision-support reporting

---

# 💡 Business Insight Areas

The current dataset highlights several areas that can be explored further:

### 1️⃣ March Performance
March has the highest total delay, making it an important period for operational investigation.

### 2️⃣ Hub Performance
Delhi and Mumbai account for the largest portions of total delay in the analyzed data.

### 3️⃣ Service Performance
Standard service has more accumulated delay days than Express service.

### 4️⃣ High-Delay Records
Individual extreme-delay records can provide useful starting points for root-cause analysis.

---

# 🚀 Future Scope

This project can be taken from a spreadsheet analysis to a complete modern analytics solution.

### 🐍 Python
- Automated data cleaning
- Exploratory Data Analysis
- Statistical analysis
- Outlier detection
- Delay prediction

### 🗄️ SQL
- Data warehouse design
- KPI queries
- Route-level performance analysis
- Automated reporting datasets

### 📊 Power BI
- Interactive logistics dashboard
- Drill-through analysis
- Dynamic filters
- KPI cards
- Route and hub performance maps
- Automated refresh

### 🤖 Advanced Analytics
- Predictive delivery-delay model
- Risk classification
- Route delay forecasting
- Hub performance monitoring

---

# 🔬 Suggested Advanced KPIs

For a production-level logistics dashboard:

```text
On-Time Delivery %
Average Delay Days
Median Delay Days
Total Delay Days
Maximum Delay
Delay Rate
Hub Delay Contribution %
Route Delay Contribution %
Express Delay Rate
Standard Delay Rate
Monthly Delay Growth %
```

---

# 📚 What This Project Demonstrates

This project demonstrates the ability to:

```text
Understand a Business Problem
          ↓
Inspect Raw Data
          ↓
Identify Data Quality Issues
          ↓
Clean & Transform Data
          ↓
Create Analytical Metrics
          ↓
Segment Performance
          ↓
Identify Exceptions
          ↓
Communicate Business Insights
```

This is the core workflow expected in practical **Data Analyst / Business Analyst** projects.

---

# 👨‍💻 About the Author

## Indrajeet Maheshwari

🎓 **B.Tech Computer Science Student**  
📊 **Aspiring Data Analyst**  
💻 Interested in **Data Analytics, Business Intelligence & Data Visualization**

### Core Skills

`Excel` • `SQL` • `Python` • `Power BI` • `Data Analysis` • `Business Intelligence`

---

# ⭐ Project Highlights

| Area | Details |
|---|---|
| 📦 Domain | Logistics / Delivery Analytics |
| 📊 Records | 12 cleaned records |
| ⏱️ Total Delay | 34 days |
| 🏢 Hubs | Delhi, Mumbai, Chennai |
| 🚛 Services | Express, Standard |
| 📅 Period | January – March |
| 🛠️ Primary Tool | Microsoft Excel |
| 📈 Analysis | Hub, Service, Monthly & Exception Analysis |

---

# 📁 Repository Files

```text
📦 Delivery Delay Analysis
│
├── 📊 Delivery Delay Analysis.xlsx
├── 📄 deliveries.csv
├── 🛣️ routes.csv
└── 📘 README.md
```

---

## 🌟 Final Note

This project demonstrates how a simple operational dataset can be transformed into a structured analytical solution using **data cleaning, KPI development, segmentation, trend analysis, and business storytelling**.

The next logical step is to extend the project into a **Python + SQL + Power BI logistics analytics pipeline** for larger datasets and automated reporting.

---

<p align="center">

### 🚚 Turning Delivery Data into Operational Insights 📊

**Made with 📊 + 💻 + 🚀 by Indrajeet Maheshwari**

</p>