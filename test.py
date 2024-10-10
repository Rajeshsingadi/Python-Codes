from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast,lit

spark = SparkSession.builder.enableHiveSupport().appName("BroadCastJoin").getOrCreate()


df_file1 = spark.read.option("header","true").csv("pathtofile1.csv")
df_file2 = spark.read.option("header","true").csv("pathtofile2.csv")

# (Id,Name)
df_file1 = df_file1.withColumn("Id", df_file1["Id"].cast("int"))

# (Id,Salary)
df_file2 = df_file2.withColumn("Id", df_file2["Id"].cast("int"))\
                    .withColumn("Salary", df_file2["Salary"].cast("float"))

df_joined = df_file1.join(broadcast(df_file2), on="Id", how="inner")

df_final = df_joined.withColumn("status", lit("a"))

df_final.write.mode("overwrite").saveAsTable("employee_data_hive")