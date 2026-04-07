
from airflow import DAG
from airflow.operators.bash import BashOperator 
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime , timedelta


def transaction_time ():
    current_time = datetime.now()
    print(f"Transaction pipeline started at {current_time}")


def Report() :
    transactions = [120, 300, 450, 200]
    counts = len(transactions)
    total = sum(transactions)

    report_content = (f"Daily Transaction Report\n"
                        f"Number of transactions: {counts}\n"
                        f"Total amount: {total}")
    
    with open('/data/transactions_report.txt', 'w') as f:
        f.write(report_content)
    


def get_report_content():
    try:
        with open('/data/transactions_report.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Report file not found."


with DAG (
    
    dag_id = "dag1",
    start_date = datetime(2026, 4 , 1),
    schedule_interval = timedelta(minutes= 10),
    catchup = False
) as dag : 
    task1 = PythonOperator(
        task_id = "task1",
        python_callable = transaction_time
    )
    task2 = PythonOperator(
        task_id = "task2",
        python_callable = Report
    )
    task3 = BashOperator(
        task_id = "task3",
        bash_command = 'python3  /data/process_transactions.py'
        
    )
    task4 = EmailOperator(
        
        task_id = "task4",
        to = 'minamaged0055@gmial.com',
        subject = 'Transaction Report',
        html_content = get_report_content()
    )
    
    task1 >> task2 >> task3 >> task4