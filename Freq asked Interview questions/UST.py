# Company UST
# ------------

# 1)
# l = ['Spark','Scala', 'Sony']
# Output
# 'Spark', 5
# 'Scala', 5
# Sony, 4

# 1A)
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("WordLength").getOrCreate()

# Sample list
l = ['Spark', 'Scala', 'Sony']

# Create a Spark DataFrame from the list
df = spark.createDataFrame([(word, len(word)) for word in l], ["word", "length"])

# Show the output
df.show(truncate=False)

# 1B)
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

# Initialize Spark Session
spark = SparkSession.builder.appName("WordLengthUDF").getOrCreate()

# Sample list
l = ['Spark', 'Scala', 'Sony']

# Create a DataFrame from the list
df = spark.createDataFrame([(word,) for word in l], ["word"])

# Define a UDF to calculate the length of the word
def word_length(word):
    return len(word)

# Register the UDF
word_length_udf = udf(word_length, IntegerType())

# Apply the UDF to calculate the length of each word
df_with_length = df.withColumn("length", word_length_udf(df["word"]))

# Show the result
df_with_length.show(truncate=False)


# 2)



# emp table
# --------
# Id column
# —
# 1
# 1
# 1
# 2
# 3
# 4
# 5
# 5
 
# -----
# Output
# 1,3
# 5,2

# 2A) using SQL code
# SELECT Id, COUNT(*) AS count
# FROM emp
# GROUP BY Id
# HAVING COUNT(*) > 1;

# 2B) Using SQL code using CTE
# WITH IdCount AS (
#     SELECT Id, COUNT(*) AS count
#     FROM emp
#     GROUP BY Id
# )
# SELECT Id, count
# FROM IdCount
# WHERE count > 1;

# 2C) using pyspark code
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("EmpCount").getOrCreate()

# Sample data for emp table
data = [(1,), (1,), (1,), (2,), (3,), (4,), (5,), (5,)]
columns = ["Id"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Group by Id and count occurrences
df_grouped = df.groupBy("Id").count()

# Filter rows where count is greater than 1 (to match your desired output format)
df_filtered = df_grouped.filter(df_grouped['count'] > 1)

# Show the result
df_filtered.show(truncate=False)


