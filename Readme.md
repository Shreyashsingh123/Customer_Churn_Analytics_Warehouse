# Customer Churn Analytics using Amazon Redshift

## Overview

This project implements a Customer Churn Analytics pipeline using Amazon Redshift. Customer churn data is loaded from Amazon S3 into Redshift, transformed through staging tables, and analyzed to generate business insights.

## Technologies Used

* Amazon S3
* Amazon Redshift
* Python
* Psycopg2
* SQL
* AWS IAM
* Git & GitHub

## Project Workflow

1. Upload datasets to Amazon S3.
2. Load raw data into Redshift using the COPY command.
3. Store data in staging tables.
4. Create an analytical table by joining customer and population datasets.
5. Perform churn analysis using SQL queries.
6. Optimize Redshift tables using ANALYZE and VACUUM.

## Database Tables

### Raw Table

* `raw_customer_churn`

### Staging Tables

* `customer_churn`
* `zip_population`

### Analytical Table

* `analytical_table`

## Analytics Performed

* Churn Rate Across All Customers
* Top Cities with Highest Churn
* Customer Churn Distribution by Tenure
* Total Revenue Lost Due to Churn
* Population vs Customer Count by ZIP Code

## Redshift Optimization

* ANALYZE
* VACUUM
* DISTKEY and SORTKEY implementation

## Project Structure

```text
Custome-Churn-Analytics-Redshift/
│
├── scripts/
│   ├── Operations/
│   │   ├── connections.py
│   │   ├── create_table.py
│   │   ├── load_data.py
│   │   ├── optimizer.py
│   │   └── SQL_Operation.py
│   │
│   └── utils/
│       ├── bucket.py
│       ├── create_redshift.py
│       ├── upload_file.py
│       └── optimizer.py
│
├── documentation/
├── main.py
├── .gitignore
└── README.md
```

## How to Run

1. Configure Redshift connection details.
2. Create tables in Redshift.
3. Load data from S3 using COPY commands.
4. Populate staging and analytical tables.
5. Run:

```bash
python3 main.py
```

## Key Learning Outcomes

* Amazon Redshift Architecture
* Data Warehousing Concepts
* Columnar Storage
* ETL Pipeline Development
* SQL Analytics
* Redshift Query Optimization
* Python and Psycopg2 Integration


