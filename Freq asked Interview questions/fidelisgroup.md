
#right angled triangle of stars< input as 4 constructor > use class 
```python
class Triangle:
    def __init__(self, layers=None, text=None):
        self.layers=layers
        self.text = text
        
    def func(self):
        for i in range(1, self.layers+1):
            print("*" * i)
            
    def add_decorator(self, suffix):
        def decorator(func):
            def wrapper(*args, **kwargs):
                res = func(*args, **kwargs)
                return res + suffix
            return wrapper
        return decorator
        
    @add_decorator("rahul")        
    def revString(self):
        
        if self.text:
            #return self.text[::-1]
            temp_reverse_string = ""
            for char in self.text:
                temp_reverse_string = char + temp_reverse_string
            return temp_reverse_string
        else:
            return "Please provide the valid text"

triangle = Triangle(4)
triangle.func()
print()
rev_text = Triangle(text="Hello")
print(rev_text.revString())
```



2)

```sql
create or replace table 'my_table.sample' (
order_id STRING,
customer_name STRING,
order_date DATE,
items ARRAY<STRUCT<item_name STRING, price FLOAT64>>
)

SELECT order_id, customer_name,  order_date, item_name, price
FROM 'my_table.sample'
UNNSET(items) as item;


orders
order_id int primary key
customer_id varchar
amount decimal 
status varchar
order_date TIMESTAMP

customers
customer_id int primary key
first_name varchar
last_name varchar
email varchar
created_at TIMESTAMP


customer who has placed the maximum order in 1 month

with LastmonthMaxOrder AS(
select   customer_id, count(order_id) as order_count,
from orders  
WHERE order_date >= CURRENT_DATE - INTERVAL 1 MONTH 
GROUP BY customer_id
)
select o.customer_id, c.first_name, c.last_name, c.email
 from LastmonthMaxOrder o 
 join customers c on c. customer_id=o. customer_id
 order by o. order_count DESC
 limit 1
 
 3)
 
 emp who have 5th highest salary for each department
 create a single nested table
 employee
 emp{id int, emp_name varchar, hire_date timestamp }
 dept:{ dept_id int,  dept_name varchar}
 comp{Totalsalary decimal, NetSalary decimal}
 
 with EmpSalary AS(
  select e.id, e. emp_name, e.salary, 
  RANK() OVER(PARITION BY d.dept_id order by c.Totalsalary DESC) AS rnk
   from 
   employee e
   UNNSET(e.dept) as d, 
   UNNSET(e. comp) as c
 )
 
 select id, emp_name, salary
 from  EmpSalary where rnk=5 
 order by dept_id
 
 
 with EmpSalary AS(
  select e.id, e. emp_name, e.salary, d.dept_id, d.dept_name, c.Totalsalary
  from 
employee e
UNNSET(e.dept) as d, 
UNNSET(e. comp) as c  
)
select dept_id, dept_name, emp_name, Totalsalary
from EmpSalary s1 
where Totalsalary = (
select distinct Totalsalary
from 
EmpSalary s2 
where s1.dept_id=s2.dept_id
order by Totalsalary DESC
LIMIT 1 OFFSET 4
)

```

4) What are different operators in Airflow?  


5) what are different window functions in sql?  

6)what are different oops concepts in python?  

7)what are different joins in SQL?

8) Nested array in Bigquery using UNNSET?

9)what is hyperloglog in dataflow?

10)what are restAPI in python?  

11)what are decorators in python?











