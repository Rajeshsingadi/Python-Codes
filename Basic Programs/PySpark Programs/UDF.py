from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("UDFExample").getOrCreate()

def greet(name):
       return f"Hello, {name}!"

greet_udf = udf(greet, StringType())

df = spark.createDataFrame([("Alice",), ("Bob",)], ["name"])
df_with_greeting = df.withColumn("greeting", greet_udf(df["name"]))
df_with_greeting.show()
