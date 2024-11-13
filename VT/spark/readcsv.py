from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("HDFSReadExample").getOrCreate()

# Read the data from HDFS
df = spark.read.csv("hdfs://localhost:9000/.csv", header=True, inferSchema=True)

# Collect the data to the driver node
data = df.collect()

# Print the data
for row in data:
    print(row)

# Stop the Spark session
spark.stop()
