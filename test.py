from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

data = [(1,), (2,), (3,), (1,), (3,)]
columns = ["ID"]

spark = SparkSession.builder.appName("Count SQL").getOrCreate()

df = sqlContext.createDataFrame(data, columns)

# Register the DataFrame as a temporary table
df.createOrReplaceTempView("emp")

# Execute SQL query using SQLContext
result_df = sqlContext.sql("""
    WITH IdCount AS (
        SELECT Id, COUNT(*) AS count
        FROM emp
        GROUP BY Id
    )
    SELECT Id, count
    FROM IdCount
    WHERE count > 1
""")

# Show the result
result_df.show(truncate=False)