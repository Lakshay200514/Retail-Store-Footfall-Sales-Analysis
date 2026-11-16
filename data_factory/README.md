
# Azure Data Factory Pipeline

## Overview

Azure Data Factory is used to orchestrate the
Retail Store Footfall vs Sales Analysis pipeline.

It manages the movement and processing of data
between Azure Data Lake Storage, Databricks
and Azure SQL Database.

## Pipeline Architecture

ADLS Gen2 -> Azure Data Factory -> Databricks
-> Azure SQL Database -> Power BI

## Pipeline Components

### 1. Azure Data Lake Storage Gen2

Stores the raw sales and footfall datasets.

Containers:
- raw
- silver
- gold

### 2. Azure Data Factory

Responsible for pipeline orchestration.

Activities:
- Read raw datasets.
- Execute Databricks notebooks.
- Process data through multiple layers.
- Copy Gold-layer output into Azure SQL.

### 3. Azure Databricks

Executes PySpark notebooks for:

- Raw data processing.
- Silver layer transformations.
- Gold layer aggregations.

### 4. Azure SQL Database

Stores the final analytical table:

Store_Performance

### 5. Power BI

Connects to Azure SQL Database to visualize
sales and footfall information.

## Execution Workflow

1. Raw datasets are stored in ADLS Gen2.
2. ADF starts the processing pipeline.
3. Databricks executes the Raw processing notebook.
4. Silver notebook cleans the data.
5. Gold notebook generates store performance.
6. ADF copies Gold output into Azure SQL.
7. Power BI visualizes the processed data.

## Data Processing Layers

| Layer | Description |
|-------|-------------|
| Raw | Original source data |
| Silver | Cleaned and transformed data |
| Gold | Aggregated analytical data |

## Expected Outcome

An automated batch-processing workflow
for analyzing retail sales and customer footfall.
