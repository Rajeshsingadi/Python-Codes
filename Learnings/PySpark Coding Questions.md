
[1)Write a spark program to check whether a given keyword exists in a huge text file or not?](#question-1)  
[2)How do you create a SparkSession in PySpark? What are its main uses?](#question-2)  
[3)You have a DataFrame in PySpark with two columns: `name` (representing user names) and `skills` (containing a comma-separated list of skills). Write a PySpark script that counts the number of skills for each user and returns the names and skill counts of users who have the highest number of skills? ](#question-3)
[4)Sample question here?](#question-4)
[5)Sample question here?](#question-5)
[6)Sample question here?](#question-6)
[7)Sample question here?](#question-7)
[8)Sample question here?](#question-8)
[9)Sample question here?](#question-9)
[10)Sample question here?](#question-10)



## Question 1 
Write a spark program to check whether a given keyword exists in a huge text file or not?  
A)  
Here's a simple PySpark program to check whether a given keyword exists in a large text file:

```python
from pyspark import SparkContext

# Initialize Spark Context
sc = SparkContext("local", "Keyword Search")

# Load the text file
file_path = "path_to_your_text_file.txt"
text_file = sc.textFile(file_path)

# Define the keyword to search
keyword = "your_keyword"

# Filter lines that contain the keyword
keyword_present = text_file.filter(lambda line: keyword in line)

# Check if the keyword exists
if keyword_present.count() > 0:
    print(f"Keyword '{keyword}' exists in the file.")
else:
    print(f"Keyword '{keyword}' does not exist in the file.")

# Stop the SparkContext
sc.stop()
```

### Steps:
1. **Load the Text File**: The `sc.textFile(file_path)` reads the large text file.
2. **Keyword Search**: The `.filter()` function checks each line for the presence of the keyword.
3. **Check Existence**: If the filtered RDD has a count greater than zero, the keyword exists; otherwise, it doesn't.


## Question 2
How do you create a SparkSession in PySpark? What are its main uses?  
A)  
from pyspark.sql import SparkSession

spark = SparkSession.builder \  
    .appName("MyApp") \  # Specify the application name  
    .config("spark.some.config.option", "config-value") \  # Optional configuration  
    .getOrCreate()  

real time example:
A real-time example of using a `SparkSession` in PySpark to analyze a large dataset of customer orders:

### Scenario: Analyzing Customer Orders

Imagine you have a CSV file containing millions of customer orders. You want to analyze this data to find the total sales per product category.

### Step-by-Step Code Example:

1. **Create a SparkSession**:
   ```python
   from pyspark.sql import SparkSession

   spark = SparkSession.builder \
       .appName("CustomerOrderAnalysis") \
       .getOrCreate()
   ```

2. **Load the Data**:
   ```python
   # Load the CSV file into a DataFrame
   orders_df = spark.read.csv("hdfs://path/to/customer_orders.csv", header=True, inferSchema=True)
   ```

3. **Data Exploration**:
   ```python
   # Show the first few rows of the DataFrame
   orders_df.show()
   
   # Print the schema of the DataFrame
   orders_df.printSchema()
   ```

4. **Data Analysis**: Calculate total sales per product category.
   ```python
   # Group by product category and sum the sales
   sales_per_category = orders_df.groupBy("product_category").agg({"sales": "sum"})
   
   # Rename the column for clarity
   sales_per_category = sales_per_category.withColumnRenamed("sum(sales)", "total_sales")
   
   # Show the result
   sales_per_category.show()
   ```

5. **Save the Results**:
   ```python
   # Save the result to a new CSV file
   sales_per_category.write.csv("hdfs://path/to/total_sales_per_category.csv", header=True)
   ```

### Explanation:

- **Creating a SparkSession**: Initializes the application for processing.
- **Loading Data**: Reads a large CSV file directly into a Spark DataFrame, which allows for efficient processing.
- **Data Analysis**: Groups the data by product category and calculates the total sales using built-in aggregation functions.
- **Saving Results**: Outputs the results back to a CSV file in HDFS.

This example demonstrates how you can leverage `SparkSession` to efficiently analyze large datasets in a real-world scenario. 


## Question 3  
You have a DataFrame in PySpark with two columns: `name` (representing user names) and `skills` (containing a comma-separated list of skills). Write a PySpark script that counts the number of skills for each user and returns the names and skill counts of users who have the highest number of skills. 


```sql
WITH SkillCounts AS (
    SELECT 
        name, 
        LENGTH(skills) - LENGTH(REPLACE(skills, ',', '')) + 1 AS skill_count
    FROM 
        your_table
)
SELECT 
    name,
    skill_count
FROM 
    SkillCounts
WHERE 
    skill_count = (SELECT MAX(skill_count) FROM SkillCounts)
```

--- 

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, expr, regexp_replace

# Create Spark session
spark = SparkSession.builder.appName("Skill Count").getOrCreate()

# Sample data (replace this with your actual DataFrame)
data = [
    ("Alice", "Python,SQL,Java"),
    ("Bob", "Python"),
    ("Charlie", "Python,SQL,Java,Scala"),
    ("David", "Python,SQL"),
    ("Eve", "Python,SQL,Java,C++"),
    ("Frank", "SQL,Java")
]

columns = ["name", "skills"]
df = spark.createDataFrame(data, columns)

# Calculate skill counts
skill_counts = df.withColumn(
    "skill_count", 
    length(col("skills")) - length(regexp_replace(col("skills"), ",", "")) + 1
)

# Find maximum skill count
max_skill_count = skill_counts.agg({"skill_count": "max"}).collect()[0][0]

# Filter users with the maximum skill count
result = skill_counts.filter(col("skill_count") == max_skill_count).select("name", "skill_count")

# Show results
result.show()
```
### Expected Output:
Running the above code will yield results similar to this (depending on the sample data):

```
+-------+-----------+
|   name|skill_count|
+-------+-----------+
|  Eve  |          4|
|Charlie|          4|
+-------+-----------+
```



## Question 1  
## Question 1  
## Question 1  


