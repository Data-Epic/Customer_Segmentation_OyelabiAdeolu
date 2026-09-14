# Customer Segmentation Data Pipeline

## Overview
The **Customer Segmentation** project refactors monolithic Jupyter notebook workflows into a robust, production-ready modular Python package. It standardizes raw data processing, applies rigorous data cleaning rules, computes customer behavioral metrics, and establishes a comprehensive automated test suite.

## Project Architecture

```text
customer_segmentation/
│
├── src/
│   └── customer_segmentation/
│       ├── __init__.py
│       ├── load.py
│       ├── cleaning.py
│       ├── features.py
│       ├── aggregation.py
│       └── export.py
│
├── tests/
│   ├── conftest.py
│   ├── test_load.py
│   ├── test_cleaning.py
│   ├── test_features.py
│   ├── test_aggregation.py
│   └── test_export.py
│
├── pyproject.toml
└── README.md

```

## Core Pipeline Modules

* **`load.py`:** Handles raw data ingestion, validates file paths, and establishes initial DataFrame schemas.
* **`cleaning.py`:** Enforces standard `snake_case` column naming conventions, strips consecutive duplicate tracking records, converts sign-up date attributes while converting 2020 anomalies into `NaT`, and filters out low-value Canadian purchases where totals fall below five.
* **`features.py`:** Derives behavioral columns, calculating customer tenure and stratifying accounts into distinct loyalty score tiers based on purchasing volume.
* **`aggregation.py`:** Summarizes segmented customer metrics across geographic and behavioral dimensions.
* **`export.py`:** Standardizes final outputs by filtering required target columns, saving files with a reversed date pattern (`processed_data_DD-MM-YYYY.csv`), and outputting shuffled preview rows for visual verification.

## Testing Suite
Automated unit tests validate module logic using `pytest` alongside shared data fixtures in `conftest.py`. Individual test scripts (`test_load.py`, `test_cleaning.py`, `test_features.py`, `test_aggregation.py`, `test_export.py`) verify edge cases, schema integrity, and temporary file export safety.

## Setup and Execution
Package dependencies and environments are managed through Poetry.

* **Install the package and development dependencies:**
```bash
poetry install

```


* **Execute the test suite:**
```bash
poetry run pytest

```