
# Retail Store Footfall vs. Sales Analysis

<p align="center">
  <b>Data Engineering and Analytics Project</b>
</p>

## Project Overview

Retail Store Footfall vs. Sales Analysis is a
data engineering project that combines retail
sales information and customer footfall data
to analyze store performance.

The project uses Microsoft Azure services,
PySpark, SQL and Power BI to build a batch
data processing and analytics pipeline.

## Project Objectives

- Analyze retail sales transactions.
- Process customer footfall data.
- Perform data cleaning and transformation.
- Calculate hourly sales and customer footfall.
- Analyze store performance and conversion rates.
- Generate insights through Power BI dashboards.

## Technology Stack

| Technology | Purpose |
|---|---|
| Azure Data Lake Storage Gen2 | Data storage |
| Azure Data Factory | Pipeline orchestration |
| Azure Databricks | Data processing |
| PySpark | Data transformation |
| Azure SQL Database | Analytical data storage |
| SQL | Data analysis |
| Power BI | Data visualization |
| Python | Programming |

## Project Architecture

```text
Sales Data + Footfall Data
           |
           v
 Azure Data Lake Storage
           |
           v
   Azure Data Factory
           |
           v
   Azure Databricks
        (PySpark)
           |
           v
    Raw Layer
           |
           v
   Silver Layer
           |
           v
    Gold Layer
           |
           v
    Azure SQL
           |
           v
       Power BI
```

## Data Processing Architecture

### 1. Raw Layer

Stores the original sales and footfall datasets
in Azure Data Lake Storage Gen2.

### 2. Silver Layer

Performs:
- Duplicate removal
- Missing value handling
- Data type conversion
- Data cleaning

### 3. Gold Layer

Prepares aggregated analytical data for
store performance analysis.

## Key Performance Indicators

- Total Sales
- Total Customer Footfall
- Hourly Sales
- Hourly Customer Footfall
- Store Performance
- Customer Conversion Rate

## Dataset Information

The project uses the Instacart Market Basket
Analysis dataset for sales-related data.

Customer footfall data is generated separately
for analytical purposes.

## Repository Structure

```text
Retail-Store-Footfall-Sales-Analysis/
│
├── notebooks/
│   ├── 01_raw_processing.py
│   ├── 02_silver_transformation.py
│   └── 03_gold_analysis.py
│
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── data_factory/
│   └── README.md
│
└── README.md
```

## Project Outcomes

The project demonstrates an end-to-end
cloud-based data engineering workflow.

It provides a foundation for analyzing
customer traffic, sales patterns and
retail store performance.

## Author

**Lakshay Khandelwal**

B.Tech - Computer Science and Engineering
(Specialization in Artificial Intelligence)
