1)
a = [1,2,3]*3

 print a 

 output:
 [1, 2, 3, 1, 2, 3, 1, 2, 3]


2)

Use List comprehension to increase the value by 1
b=[2,6,8,10]
ouput:
print([ i+1 for i in b])

3)  

find largest element in the array

 input1 = [-10,-20,-50]  ans: -10

 input2 = [5,999,99999,1010101] ans: 1010101

 input3= [] ans []

A)  
def find_largest(input_list):
    if not input_list:  # If the list is empty, return an empty list
        return []
    
    largest = input_list[0]  # Assume the first element is the largest to start
    for num in input_list:
        if num > largest:
            largest = num  # Update largest if the current number is bigger
    
    return largest

# Test cases
input1 = [-10, -20, -50]
input2 = [5, 999, 99999, 1010101]
input3 = []

print(find_largest(input1))  # Output: -10
print(find_largest(input2))  # Output: 1010101
print(find_largest(input3))  # Output: []

4)  
a = tuple([1,2,3,4,5])

 a[0]=5

 print a

 A) 
 In Python, tuples are immutable, meaning their elements cannot be changed once they are created. When you try to assign a new value to an element of a tuple, it results in an error.

Here’s the code you provided with the error explanation:

```python
a = tuple([1, 2, 3, 4, 5])

a[0] = 5  # This will raise a TypeError because tuples are immutable

print(a)
```

This will raise a `TypeError: 'tuple' object does not support item assignment`.

To modify the tuple, you would need to convert it into a list, update the value, and then convert it back to a tuple:

```python
a = tuple([1, 2, 3, 4, 5])

# Convert tuple to list
a_list = list(a)
a_list[0] = 5

# Convert list back to tuple
a = tuple(a_list)

print(a)
```

This would output:
```
(5, 2, 3, 4, 5)
```

5)  


delete duplicates from employee table

 emp_id, emp_name, dept_id, salary, manager_id

 1		akash		101		100		2

 2		aakriti		101 	200 	null

 3 		jorge		102		150     4

 1		akash 		101		500		2

A)  
```
WITH ranked_employees AS (
    SELECT 
        emp_id,
        emp_name,
        dept_id,
        salary,
        manager_id,
        ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY salary DESC) AS row_num
    FROM employee
)
DELETE FROM employee
WHERE emp_id IN (
    SELECT emp_id FROM ranked_employees WHERE row_num > 1
);
```
6)  
### Question:
Given the following tables:

**agent table:**

| agent_id | agent_name |
|----------|------------|
| 999      | John       |
| 991      | Alice      |
| 992      | Bob        |

**orders table:**

| order_id | product_id | category | sales | order_date | agent_id |
|----------|------------|----------|-------|------------|----------|
| 1        | 101        | apparel  | 100   | 2022-01-01 | 999      |
| 2        | 102        | Shoes    | 1999  | 2023-05-01 | 999      |
| 3        | 101        | apparel  | 1000  | 2023-06-01 | 991      |
| 4        | 103        | Sunglass | 100   | 2024-01-01 | 992      |
| 5        | 104        | Beauty   | 999   | 2024-02-01 | 992      |
| 6        | 104        | Beauty   | 2999  | 2024-08-01 | 991      |

**Task:** Write a SQL query to find the top 3 products with the highest total sales. Use Common Table Expressions (CTEs) to first calculate the total sales per product, and then rank the products based on total sales.

### Answer:
Here’s the SQL query that accomplishes this:

```sql
WITH salesTable AS (
    SELECT 
        product_id, 
        SUM(sales) AS total_sales
    FROM 
        orders
    GROUP BY 
        product_id
),
orderTable AS (
    SELECT 
        product_id, 
        total_sales,
        DENSE_RANK() OVER (ORDER BY total_sales DESC) AS rnk
    FROM 
        salesTable
)
SELECT 
    product_id, 
    total_sales 
FROM 
    orderTable
WHERE 
    rnk <= 3;
```

### Explanation:
1. **`salesTable` CTE**: This CTE calculates the total sales for each product by grouping the sales data in the `orders` table:
   - **`SUM(sales) AS total_sales`**: Aggregates sales for each `product_id`.
   - **`GROUP BY product_id`**: Ensures that the aggregation is done per product.

2. **`orderTable` CTE**: This CTE ranks the products based on their total sales:
   - **`DENSE_RANK() OVER (ORDER BY total_sales DESC)`**: Assigns a rank to each product based on total sales in descending order.

3. **Final Selection**: The main query selects the `product_id` and `total_sales` from `orderTable` where the rank (`rnk`) is 3 or less, effectively returning the top 3 products by total sales.

### Example Result:
Given the data in the `orders` table, the query will return:

| product_id | total_sales |
|------------|-------------|
| 104        | 3998        |
| 102        | 1999        |
| 101        | 1100        |

- **Product `104`** (Beauty) has the highest total sales of `3998`.
- **Product `102`** (Shoes) follows with `1999`.
- **Product `101`** (Apparel) has total sales of `1100`. 

This query successfully identifies the top 3 products based on total sales using CTEs and ranking.

7)  
table_a		table_b

 col_1		col_2

 1			1

 1			1

 1			2
 null		null
 null

use all the joins and give the count of each join?

A) 
inner join = 6
left join = 8
right join = 8
full join = 10
cross join = 5*4=20