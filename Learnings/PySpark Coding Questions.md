
[1)Write a spark program to check whether a given keyword exists in a huge text file or not?](#question-1)  
[2)Sample question here?](#question-2)  
[3)Sample question here?](#question-3)
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




