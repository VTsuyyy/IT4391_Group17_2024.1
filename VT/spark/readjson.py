from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Read JSON from HDFS") \
    .getOrCreate()
# Specify the HDFS path to the JSON file
json_file_path = "hdfs://localhost:9000/data/recruit_1_4.json"

# Load JSON data from HDFS into a DataFrame
df = spark.read.json(json_file_path)

# Show the contents of the DataFrame (optional)
df.show()


# Collect the data (use only for small files)
data = df.collect()
for row in data:
    print(row[0])  # Access the line content

# Stop the Spark session
spark.stop()
