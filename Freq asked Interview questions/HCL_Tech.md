1)To achieve the desired output of counting the number of male and female employees from the provided `emp` table, you can use a SQL query that aggregates the data based on the gender. Here’s how you can write the query:

### Sample Input Data
Assuming the `emp` table is structured as follows:

#### **Emp Table**
| name   | gender  |
|--------|---------|
| Ankit  | male    |
| Akriti | female  |
| Asths  | FEMALE  |
| Ravi   | Male    |
| Nitin  | malE    |

A)  

### SQL Query
You can use the following SQL query to get the count of males and females:

```sql
SELECT 
    SUM(CASE WHEN LOWER(gender) = 'male' THEN 1 ELSE 0 END) AS No_of_male,
    SUM(CASE WHEN LOWER(gender) = 'female' THEN 1 ELSE 0 END) AS No_of_female
FROM 
    emp;
```

### Explanation:
- **LOWER(gender)**: This is used to handle case insensitivity, ensuring that variations like "Male", "male", or "MALe" are counted as male.
- **CASE Statement**: It checks the gender and counts it as 1 if it matches 'male' or 'female' and 0 otherwise.
- **SUM()**: This aggregates the counts to give the total number of males and females.

### Expected Output
When you run the above query on the provided data, you should get the following result:

| No_of_male | No_of_female |
|-------------|---------------|
| 3           | 2             |

This output indicates that there are 3 males and 2 females in the `emp` table.  


2)  
ankit
rajesh
ankit
nithin
count the names in SQL 

A)  
SELECT 
    name, 
    COUNT(*) AS name_count
FROM 
    emp  -- Assuming your table is named 'emp'
GROUP BY 
    name;

3)  
dept table
dept_id, dept_name

employee table
dept_id, salary

3rd highest salary in each dept
op:
dept_id, dept_name,salary

A)  
WITH SalaryRank AS (
    SELECT 
        e.dept_id, 
        d.dept_name, 
        e.salary, 
        DENSE_RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS salary_rank
    FROM 
        employee e
    JOIN 
        dept d ON e.dept_id = d.dept_id
)
SELECT 
    dept_id, 
    dept_name, 
    salary
FROM 
    SalaryRank
WHERE 
    salary_rank = 3;


4)  
 Find all the lines in a file which starts with digits in python.

 file content is

 apple

 1apple

 2apple

 banana

 1banana


A)  
To find all the lines in a file that start with digits using Python, you can read the file line by line and check if each line starts with a digit using the `str.isdigit()` method. Here's a simple program to achieve this:

### Python Program

```python
# Function to find lines starting with digits
def find_lines_starting_with_digits(file_path):
    lines_with_digits = []  # List to store lines starting with digits
    
    with open(file_path, 'r') as file:  # Open the file in read mode
        for line in file:  # Iterate through each line in the file
            line = line.strip()  # Remove leading/trailing whitespace
            if line and line[0].isdigit():  # Check if the line is not empty and starts with a digit
                lines_with_digits.append(line)  # Add line to the list
    
    return lines_with_digits  # Return the list of lines

# Specify the file path
file_path = 'your_file.txt'  # Change this to your actual file path

# Call the function and print the result
lines = find_lines_starting_with_digits(file_path)
print("Lines starting with digits:")
for line in lines:
    print(line)
```

### Explanation:
1. **Function Definition**: The `find_lines_starting_with_digits` function takes a file path as an argument and initializes an empty list to store the lines that start with digits.
2. **Open the File**: It opens the file in read mode using a `with` statement, which ensures the file is properly closed after processing.
3. **Iterate Through Lines**: It iterates through each line in the file, stripping leading and trailing whitespace.
4. **Check for Digits**: It checks if the line is not empty and whether the first character is a digit using `line[0].isdigit()`.
5. **Store Matching Lines**: If a line meets the criteria, it is added to the `lines_with_digits` list.
6. **Return and Print Results**: Finally, it returns the list of matching lines and prints them.

### Example File Content
For the given file content:
```
apple
1apple
2apple
banana
1banana
```

### Expected Output
When you run the program with this file content, the output will be:
```
Lines starting with digits:
1apple
2apple
1banana
```

Make sure to replace `'your_file.txt'` with the actual path to your text file when you run the code.  


5)  
Given a nested_list = [1, 2, [3, 4, [5],[]], [6]] 
The result should flatten the list and would become [1,2,3,4,5,6] as output?

A)  
def flatten(nested_list):
    result = []  # Initialize an empty list to store flattened values
    for item in nested_list:
        if isinstance(item, list):  # Check if the item is a list
            result.extend(flatten(item))  # Recursively flatten the nested list
        else:
            result.append(item)  # Append non-list items directly
    return result  # Return the flattened list

# Given nested list
nested_list = [1, 2, [3, 4, [5], []], [6]]

# Flatten the list
flattened_list = flatten(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]


6)  
Given a list of student’s details in a classroom with their names and the marks they got.
 
Write a program to return students’ details whose marks are greater than the average marks in the classroom.
 
sample list
 
L=[('Mahendra', 10),('Mahi', 20),('Varun', 10),('Sam',20),('Ishak',10),('Tarun',20)]
result should be list > avg marks 
A)  
You can achieve this by first calculating the average marks of the students and then filtering out the students whose marks are greater than that average. Here's a simple Python program to do this:

### Python Program

```python
# Sample list of students with their marks
L = [('Mahendra', 10), ('Mahi', 20), ('Varun', 10), ('Sam', 20), ('Ishak', 10), ('Tarun', 20)]

# Calculate the average marks
total_marks = sum(marks for name, marks in L)  # Sum of all marks
num_students = len(L)  # Total number of students
average_marks = total_marks / num_students if num_students > 0 else 0  # Calculate average

# Filter students whose marks are greater than the average
students_above_avg = [student for student in L if student[1] > average_marks]

# Print the result
print("Students with marks greater than average:", students_above_avg)
```

### Explanation:
1. **Calculate Total Marks**: The program calculates the total marks using a generator expression that iterates through the list of tuples.
2. **Calculate Average Marks**: It computes the average marks by dividing the total marks by the number of students.
3. **Filter Students**: It uses a list comprehension to create a new list that includes only those students whose marks are greater than the average.
4. **Print the Result**: Finally, it prints the list of students with marks above average.

### Expected Output
For the provided sample list:
```plaintext
Students with marks greater than average: [('Mahi', 20), ('Sam', 20), ('Tarun', 20)]
```

This output lists the students who scored above the average marks in the classroom.