# Transaction Processing Pipeline (Airflow)

A robust data engineering pipeline built with Apache Airflow that automates transaction data simulation, report generation, and email notifications every 10 minutes.

## 🚀 Project Overview
This project demonstrates a production-style automated workflow. It processes a fixed set of transactions, calculates key metrics, saves the data to a local file system, and triggers an external processing script before notifying stakeholders via email.

### Key Features
* **Automated Scheduling**: Runs every 10 minutes using Cron-based intervals.
* **Data Processing**: Python-based logic for transaction aggregation (Count & Total).
* **External Execution**: Integration with standalone Python scripts via Bash.
* **Reporting**: Automated SMTP email delivery with dynamic report content.

---

## 📊 Pipeline Logic & Visualization

### 1. Workflow Architecture 
The pipeline follows a strict sequential dependency to ensure data integrity. Each task must succeed before the next one begins.

<div align="center">
  <img src="images/Screenshot 2026-04-06 225054.png" alt="Airflow Graph View" width="850">
  <p><i><b>Figure 1:</b> The Graph View showing the flow from Initialization to Email Notification.</i></p>
</div>

### 2. Execution History 
As shown in the monitoring dashboard, the DAG maintains a consistent "Success" state across multiple scheduled intervals.

<div align="center">
  <img src="images/Screenshot 2026-04-06 225040.png" alt="Airflow Grid View Summary" width="850">
  <p><i><b>Figure 2:</b> The Grid View confirming 100% success rate for all task instances.</i></p>
</div>

---

## 📁 Project Structure
```text
transaction-pipeline-airflow/
├── dags/
│   └── transaction_dag.py        # Main Airflow DAG definition
├── scripts/
│   └── process_transactions.py    # External script executed by Task 3
├── data/
│   └── transactions_report.txt    # Generated output report
└── README.md                     # Documentation & Visuals
