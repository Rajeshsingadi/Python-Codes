Interview questions
-----------------

[1)Write a result for left,right and full outer join when we join below tables?  Table A - 1 1 2 1 4 3 and Table B - 1 2 1 2 3 3 ?](#question-1)  
[2)?](#question-2)  
[3)Write a SQL query to calculate the cumulative sum of sales for each employee (`empld`) ordered by `sales_date`?](#question-3)  
[4)SQL QUERY to delete the duplicates and keep the record with minimum age?](#question-4)  
[5)To find employees who have a greater salary than their manager?](#question-5)  
[6)File 1 - Id,Name File 2 - Id, Salary Read two files, apply schema, do broadcast join assuming file 2 data is less. Add one status column and populate 'a' as active status and load to hive table?](#question-6)  


## Question 1  
Write a result for left,right and full outer join when we join below tables?  Table A - 1 1 2 1 4 3 and 
Table B - 1 2 1 2 3 3 ?  
A)  
Let's go through the logic again step by step to clarify how to achieve the counts you are seeing in your database. 

Given your tables:

### Table A
```
| Value |
|-------|
| 1     |
| 1     |
| 2     |
| 1     |
| 4     |
| 3     |
```

### Table B
```
| Value |
|-------|
| 1     |
| 2     |
| 1     |
| 2     |
| 3     |
| 3     |
```

### Join Results

1. **Left Outer Join**:
   - **For `1` from A**:
     - Matches both `1`s in B → **4 matches** (first 1 in A matches with both 1s in B).
   - **For `2` from A**:
     - Matches both `2`s in B → **2 matches** (2 in A matches both 2s in B).
   - **For `4` from A**:
     - No match → **1 NULL**.
   - **For `3` from A**:
     - Matches both `3`s in B → **2 matches** (3 in A matches both 3s in B).

Putting it all together:

```
| A.Value | B.Value |
|---------|---------|
| 1       | 1       |  // 1 from A matches 1 in B
| 1       | 1       |  // 1 from A matches 1 in B
| 1       | 1       |  // 1 from A matches 1 in B
| 1       | 1       |  // 1 from A matches 1 in B
| 2       | 2       |  // 2 from A matches 2 in B
| 2       | 2       |  // 2 from A matches 2 in B
| 1       | NULL    |  // 1 from A has no match
| 4       | NULL    |  // 4 from A has no match
| 3       | 3       |  // 3 from A matches 3 in B
| 3       | 3       |  // 3 from A matches 3 in B
```

**Total for Left Outer Join: 11 records**

2. **Right Outer Join**:
   - **For `1` from B**:
     - Matches all `1`s in A → **4 matches**.
   - **For `2` from B**:
     - Matches both `2`s in A → **2 matches**.
   - **For `3` from B**:
     - Matches both `3`s in A → **2 matches**.

Resulting in:

```
| A.Value | B.Value |
|---------|---------|
| 1       | 1       |  // 1 from B matches 1 in A
| 1       | 1       |  // 1 from B matches 1 in A
| 1       | 1       |  // 1 from B matches 1 in A
| 1       | 1       |  // 1 from B matches 1 in A
| NULL    | 2       |  // 2 from B has no match
| NULL    | 2       |  // 2 from B has no match
| 3       | 3       |  // 3 from B matches 3 in A
| NULL    | 3       |  // 3 from B has no match
```

**Total for Right Outer Join: 10 records**

3. **Full Outer Join**:
   Combines results from both left and right:

```
| A.Value | B.Value |
|---------|---------|
| 1       | 1       |  // 1 matches
| 1       | 1       |  // 1 matches
| 2       | 2       |  // 2 matches
| 1       | NULL    |  // 1 from A has no match
| 4       | NULL    |  // 4 from A has no match
| 3       | 3       |  // 3 matches
| NULL    | 2       |  // 2 from B has no match
| NULL    | 2       |  // 2 from B has no match
| NULL    | 3       |  // 3 from B has no match
```

**Total for Full Outer Join: 11 records**

### Summary of Results
- **Left Outer Join:** 11 records
- **Right Outer Join:** 10 records
- **Full Outer Join:** 11 records
- **inner Join:** 10 records
- **cross Join:** 36 records

Summary of Results (Without Duplicates)
- **Left Outer Join:** 4 records
- **Right Outer Join:** 3 records
- **Full Outer Join:** 4 records
- **inner Join:** 3 records
- **cross Join:** 12 records


## Question 2  

SELECT
    name,
    time,
    ROW_NUMBER() OVER (ORDER BY time) AS row_number,
    RANK() OVER (ORDER BY time) AS rank,
    DENSE_RANK() OVER (ORDER BY time) AS dense_rank
FROM
    your_table_name
ORDER BY    time;  


## Question 3  
### Question:
Given the following sales data:

| empld | sales_date | sales_amount |
|-------|------------|--------------|
| 101   | 2024-08-01 | 1000         |
| 102   | 2024-08-01 | 1500         |
| 101   | 2024-08-02 | 2000         |
| 103   | 2024-08-02 | 2500         |
| 101   | 2024-08-03 | 3000         |

Write a SQL query to calculate the cumulative sum of sales for each employee (`empld`) ordered by `sales_date`.

### Answer:
You can use the `SUM()` window function to calculate the cumulative sum of sales for each employee. Here’s the SQL query:

```sql
SELECT
    empld,
    sales_date,
    sales_amount,
    SUM(sales_amount) OVER (PARTITION BY empld ORDER BY sales_date) AS cumulative_sales
FROM
    sales_table
ORDER BY
    empld, sales_date;
```

### Explanation:
- `SUM(sales_amount) OVER (PARTITION BY empld ORDER BY sales_date)`: This calculates the cumulative sum of `sales_amount` for each `empld`, ordering the results by `sales_date`.
- The `PARTITION BY` clause groups the results by `empld`, ensuring that the cumulative sum is calculated separately for each employee.
- The final `ORDER BY` clause orders the overall output by `empld` and `sales_date`.

### Sample Output:
Assuming the data is correctly set up, the output will look like this:

| empld | sales_date | sales_amount | cumulative_sales |
|-------|------------|--------------|-------------------|
| 101   | 2024-08-01 | 1000         | 1000              |
| 101   | 2024-08-02 | 2000         | 3000              |
| 101   | 2024-08-03 | 3000         | 6000              |
| 102   | 2024-08-01 | 1500         | 1500              |
| 103   | 2024-08-02 | 2500         | 2500              |

This output reflects the cumulative sales for each employee over time.
## Question 4  
SQL QUERY to delete the duplicates and keep the record with minimum age?  
A)  

WITH ranked_employees AS (
    SELECT ID, Name, Age,
           ROW_NUMBER() OVER (PARTITION BY Name ORDER BY Age ASC) AS row_num
    FROM employee
)
DELETE FROM employee
WHERE ID IN (
    SELECT ID
    FROM ranked_employees
    WHERE row_n
um > 1
);

## Question 5  
To find employees who have a greater salary than their manager, you can use a SQL query that involves a self-join on the employee table. Here’s how you can structure the query based on your provided data:

### Sample Data
Here is the sample data you provided:

| empid | emp_name | salary | manager_id |
|-------|----------|--------|------------|
| 1     | John     | 70000  | 5          |
| 2     | Alice    | 60000  | 5          |
| 3     | Bob      | 90000  | 4          |
| 4     | Charlie  | 80000  | NULL       |
| 5     | Eve      | 75000  | 4          |

### SQL Query

```sql
SELECT e.empid, e.emp_name, e.salary AS employee_salary, m.salary AS manager_salary
FROM employee e
LEFT JOIN employee m ON e.manager_id = m.empid
WHERE e.salary > m.salary;
```

### Explanation

1. **Self-Join**:
   - The table `employee` is joined with itself. Here, `e` is an alias for the employee (the one being compared), and `m` is an alias for the manager.
   - The join condition matches the `manager_id` of the employee with the `empid` of the manager.

2. **Where Clause**:
   - The `WHERE` clause filters the results to include only those employees whose salary is greater than their manager's salary.

### Result Interpretation

Given the sample data, the query will return employees who earn more than their respective managers. For example:
- If we assume manager ID 4 (Bob) has a salary of 90000, and the manager ID 5 (Eve) has a salary of 75000, the results will show whether employees like John and Alice earn more than their managers.

### Sample Output
If we were to run this query on the provided dataset, the expected output would look something like this:

| empid | emp_name | employee_salary | manager_salary |
|-------|----------|------------------|-----------------|
| 1     | John     | 70000            | 75000           |
| 2     | Alice    | 60000            | 75000           |
| 3     | Bob      | 90000            | 80000           |

In this case, only Bob would show in the results because Bob has a salary greater than his manager's salary (80000).

Feel free to reach out if you need further clarification or additional help with SQL queries!  

## Question 6  

A)  
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, lit

# Initialize Spark session with Hive support
spark = SparkSession.builder \
    .enableHiveSupport() \
    .appName("BroadCastJoin") \
    .getOrCreate()

# Read the CSV files
df_file1 = spark.read.option("header", "true").csv("pathtofile1.csv")
df_file2 = spark.read.option("header", "true").csv("pathtofile2.csv")

# Cast columns to appropriate data types
df_file1 = df_file1.withColumn("Id", df_file1["Id"].cast("int"))  # Assuming Id is integer
df_file2 = df_file2.withColumn("Id", df_file2["Id"].cast("int")) \
                    .withColumn("Salary", df_file2["Salary"].cast("float"))  # Assuming Salary is float

# Perform the broadcast join
df_joined = df_file1.join(broadcast(df_file2), on="Id", how="inner")

# Add the status column
df_final = df_joined.withColumn("status", lit("a"))

# Write the final DataFrame to a Hive table
df_final.write.mode("overwrite").saveAsTable("employee_data_hive")

# Stop the Spark session
spark.stop()


## Question 7  
## Question 8  
## Question 9  
## Question 10  
