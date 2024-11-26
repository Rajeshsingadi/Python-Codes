
--2nd highest salary

select max(salary) from employees 
where salary < (select max(salary) from employees)

--2nd highest dept wise

select department, salary as second_highest from 
(
select department, salary, rank() over(partition by department order by salary desc) as rnk from employees
) rnk_salaries
where rnk=2

--department 

employee_df = spark.read.parquet("path/to/file.parquet")
department_df = spark.read.parquet("path/to/department.parquet")
joined_df = employee_df.join(department_df, on="Department_ID" , how="inner")

wind_spec = window.partitionBy("department").orderBy(col("salary").desc())

ranked_df = joined_df.withColumn("rank", rank().over(wind_spec))

second_highest_salary_df = ranked_df.filter(col("rank") == 2 ).select("col1", "col2")

second_highest_salary_df.show()




