from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType


spark = SparkSession.builder\
            .appName("Sum Function")\
            .getOrCreate()

df = spark.createDataFrame([(12,), (13,)], ["id"])
agg_df = df.agg({"id":"sum"})
Total_df = agg_df.withColumnRenamed("sum(id)", "Total")
Total_df.show(truncate=False)
spark.stop()