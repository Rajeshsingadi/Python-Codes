Questions
-----------------

[1)Find indices of two numbers that add up to a target? Input: numbers = [2,7,11,15], target = 9?](#question-1)  
[2)ind numbers in a table that are equal to both their previous and next values?](#question-2)  
[3)Describe the data pipeline flow in the architecture diagram, detailing how data is ingested, processed, and stored across various components?](#question-3)  
[4)More general question and few questions in apache spark file!](#question-4)  


## Question 1  
Find indices of two numbers that add up to a target? Input: numbers = [2,7,11,15], target = 9?
A)  
numbers = [2,7,11,15]
target = 9

def func(numbers, target):
    indexDict ={}
    for index, num in enumerate(numbers):
        c = target - num
        if c in indexDict:
            return [indexDict[c] + 1, index + 1 ]
        indexDict[num] = index
    return []

print(func(numbers, target))


## Question 2  
Find numbers in a table that are equal to both their previous and next values?
A)  
with logsTable as (
  select id, num, LEAD(num) over(order by Id) as next_num, 
  LAG(num) over(order by Id) as prev_num 
  from logs  
)
select num 
from logsTable 
where num = prev_num and num = next_num

Output :  
RunCount: 1

## Question 3  
Describe the data pipeline flow in the architecture diagram, detailing how data is ingested, processed, and stored across various components?  
A)  
Architecture Solution
The architecture diagram represents a data pipeline workflow that involves several components:

Data Ingestion:
Source: Data is ingested from multiple external sources like APIs, databases (e.g., MySQL, PostgreSQL), flat files (CSV, JSON), or cloud storage (e.g., AWS S3, GCP Storage).
Method: This data ingestion is typically handled by services like Apache Kafka (for real-time streaming data) or AWS Glue/Google Dataflow for batch data loading.
Data Processing:
Processing Engine: The ingested data is processed using Apache Spark or PySpark for large-scale data transformations and ETL (Extract, Transform, Load) operations. Spark’s distributed computing capabilities allow it to handle large datasets efficiently.
Transformations: During this stage, data cleaning, filtering, and transformation rules are applied to convert raw data into a structured format. This involves applying business logic, data quality checks, and optimizations like caching for faster processing.
Data Storage:
Data Lake: The transformed data is stored in a Data Lake (e.g., Amazon S3, Google Cloud Storage) for long-term storage of structured, semi-structured, and unstructured data.
Data Warehouse: A Data Warehouse (e.g., Amazon Redshift, Google BigQuery, or Snowflake) is used to store processed and structured data for reporting and analytics.
Data Mart: Some specific datasets are further refined and stored in Data Marts for faster querying and analysis, often used by specific departments or business teams.
Data Access & Analytics:
BI Tools: The processed data is consumed by Business Intelligence (BI) tools like Tableau, Looker, or Power BI for reporting, visualization, and decision-making.
Machine Learning: Data scientists can access this data for building machine learning models using platforms like Databricks or AWS SageMaker.
Monitoring & Orchestration:
Airflow/Dagster: The pipeline is orchestrated using workflow automation tools like Apache Airflow, which handles the scheduling, monitoring, and dependency management of various tasks in the data pipeline.
Logging and Alerts: Systems like CloudWatch or Datadog monitor the pipeline’s performance, triggering alerts for failures or bottlenecks.  

