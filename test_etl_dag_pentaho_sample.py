import airflow
from airflow import DAG
from airflow.operators.test_plugin import PentahoOperator

dag = DAG('test_pentaho_sample_1')

step1 = PentahoOperator(
    task_id='first-step',
    dag=dag,
    start_date=airflow.utils.dates.days_ago(2),
    pentaho_job_id='ej-etl-sample-v1.0',
    pentaho_job_file_name='simple-job.kjb'
)

