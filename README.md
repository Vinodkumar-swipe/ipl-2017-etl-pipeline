
# IPL 2017 Multi-Source ETL & ELT Pipeline

## Project Overview
This project demonstrates a production-oriented ETL and ELT pipeline built using IPL 2017 cricket datasets. The objective was to simulate real-world enterprise data engineering workflows involving multi-source ingestion, transformation, validation, aggregation, and reporting.

The project was developed during internship training to strengthen practical understanding of:
- ETL vs ELT concepts
- Data pipeline development
- Structured data processing
- Data validation and reconciliation
- Cloud-oriented analytics engineering workflows

## Business Problem
Sports analytics organizations and media platforms require structured analytical pipelines to process large transactional datasets such as:
- Ball-by-ball match events
- Player performance records
- Team statistics
- Match-level summaries

The challenge is to:
- ingest multiple relational datasets
- transform raw records into analytical outputs
- ensure data quality and consistency
- generate business insights efficiently

## Architecture Overview
Kaggle Dataset
↓
Google Colab ETL Pipeline
↓
Python Pandas Transformation Layer
↓
Aggregation & Validation
↓
SQLite Database
↓
Excel Reporting Layer

Additional ELT Exposure:
Databricks SQL Transformation Workflow

## Tech Stack
### ETL Pipeline
- Python
- Pandas
- SQLite
- Google Colab
- KaggleHub
- OpenPyXL

### ELT Pipeline
- Databricks
- SQL
- Distributed Processing Concepts

### Reporting
- Excel
- CSV Outputs

## ETL Workflow

### Extract
- Downloaded IPL dataset using KaggleHub
- Loaded structured CSV datasets into Pandas DataFrames

### Transform
Performed:
- Season filtering
- Aggregation
- Joins
- Null handling
- Data cleansing
- Grouping
- Validation checks
- KPI generation

### Load
Loaded outputs into:
- SQLite database
- Excel reporting layer

## Validation Checks
Implemented:
- Null value checks
- Row count validation
- Aggregation verification
- Duplicate checks
- Schema consistency checks

Example:
assert matches_2017.shape[0] > 0
assert top_batsmen['Runs'].sum() > 0

## Business Insights Generated
- Top 10 Batsmen by Runs
- Teams with Most Wins
- Top MVP Players

## ETL vs ELT Understanding

### ETL
Transformations performed before loading into SQLite using Python Pandas.

### ELT
Raw data loaded first and transformed later using SQL workflows in Databricks.

## Challenges Faced
- Managing joins across multiple relational datasets
- Handling null values and schema inconsistencies
- Maintaining aggregation accuracy
- Designing modular transformation logic

## Learnings
- ETL pipeline architecture
- SQL transformation logic
- Data validation workflows
- Cloud-oriented data engineering concepts
- ELT processing approaches
- Structured reporting pipelines

## Future Enhancements
- Migrate SQLite to PostgreSQL
- Implement Azure Data Factory orchestration
- Add incremental loads
- Integrate Power BI dashboards
- Add Airflow scheduling
- Add logging and monitoring
- Implement PySpark transformations
- Add Docker containerization

## How to Run

pip install -r requirements.txt
python etl_pipeline.py

## Author
Vinod Kumar
Business Intelligence & Data Engineering Engineer
