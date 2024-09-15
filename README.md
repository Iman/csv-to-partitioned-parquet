# CSV to Partitioned Parquet

## Overview

This project converts a CSV file into a partitioned Parquet format based on timestamps. The data is partitioned by Year, Month, and Day, making it suitable for querying by services like Azure Data Factory, Synapse, or Power BI.

## Prerequisites

- Python 3.11
- Azure Blob Storage account
- `pip` for package management

## Getting Started (Set up Python Virtual Environment)

To ensure you're using the correct Python version and packages, set up a virtual environment in the project folder.

Run the following commands to create and activate a virtual environment with Python 3.11:

```bash
python3.11 -m venv .venv

source .venv/bin/activate

# Activate the virtual environment (Windows)
.\.venv\Scripts\activate
```

### Install the Required Packages
```
pip install -r requirements.txt
```