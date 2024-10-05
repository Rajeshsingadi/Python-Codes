### **Question:**
You are given two tables:

#### **`Emp` Table:**
| Column      | Description                            |
|-------------|----------------------------------------|
| Empname     | Name of the employee                   |
| Id          | Unique identifier for the employee     |
| Salary      | Salary of the employee                 |
| Manager_Id  | Id of the employee's manager (nullable)|
| Dept_Id     | Department Id where the employee works |

#### **`Department` Table:**
| Column         | Description                            |
|----------------|----------------------------------------|
| Department_Id  | Unique identifier for the department    |
| Department_Name| Name of the department                 |

Write a SQL query to find the highest-paid employee in each department along with their manager's name. The query should return:
- The name of the department
- The name of the highest-paid employee in that department
- The name of their manager (if they have one)
- The salary of the highest-paid employee

If multiple employees have the same salary, all of them should be included.

### **Expected Output:**
| Department_Name | Empname | Manager_Name | Salary |
|-----------------|---------|--------------|--------|
| [Department 1]  | [Employee Name] | [Manager Name] | [Salary] |
| [Department 2]  | [Employee Name] | [Manager Name] | [Salary] |


Answer)  
WITH OutPutTable AS (
    SELECT 
        d.Department_Name, 
        e.Empname, 
        e2.Empname AS Manager_Name, 
        e.salary,
        DENSE_RANK() OVER(PARTITION BY e.dept_id ORDER BY e.salary DESC) AS rnk
    FROM 
        Emp e
    LEFT JOIN 
        Emp e2 ON e.manager_id = e2.Id
    JOIN 
        Department d ON d.Department_Id = e.dept_id
)

SELECT 
    Department_Name, 
    Empname, 
    Manager_Name, 
    salary
FROM 
    OutPutTable
WHERE 
    rnk = 1;
