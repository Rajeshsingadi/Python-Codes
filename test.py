from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, length, regexp_replace, col
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("Comma Seperated Max").getOrCreate()


data = [
    ("Alice", "Python,SQL,Java"),
    ("Bob", "Python"),
    ("Charlie", "Python,SQL,Java,Scala"),
    ("David", "Python,SQL"),
    ("Eve", "Python,SQL,Java,C++"),
    ("Frank", "SQL,Java")
]

columns = ["name", "skills"]

df = spark.createDataFrame(data,columns)


df_skill = df.withColumn("SkillCount", length(col("skills")) - length(regexp_replace(col("skills"), ",", "")) +1 )

max_skill_count = df_skill.agg({"SkillCount":"max"} ).collect()[0][0]
result = df_skill.filter(col("SkillCount")==max_skill_count)

result.show()