from pyspark.sql import SparkSession

# Step 1: Create a SparkSession (this is the entry point to use PySpark)
spark = SparkSession.builder.appName("LineWordCount").getOrCreate()

# Step 2: Read the text file
file_path = "path/to/your/textfile.txt"  # Replace with the path to your file
lines_rdd = spark.sparkContext.textFile(file_path)

# Step 3: Count the number of words in each line
# We split each line by spaces and then count the length of the resulting list (number of words)
word_counts_per_line = lines_rdd.map(lambda line: (line, len(line.split())))

# Step 4: Collect the results (bring data to the driver node) and print
results = word_counts_per_line.collect()

# Step 5: Print the results (each line and its word count)
for line, count in results:
    print(f"Line: '{line}' has {count} words")

# Step 6: Stop the Spark session when done
spark.stop()
