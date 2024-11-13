from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("HDFSReadTextFileExample").getOrCreate()

# Path to the text file in HDFS
hdfs_path = "hdfs://localhost:9000/input/input.txt"
# hdfs_path = "hdfs://localhost:9000/data/recruit_10_14.json"

# Read the text file into a DataFrame (each line is a row)
df = spark.read.text(hdfs_path)
print('\n')  # Access the line content
print('\n')  # Access the line content

# Show the contents of the file
df.show(truncate=False)

print('\n')  # Access the line content
print('\n')  # Access the line content
# Collect the data (use only for small files)
data = df.collect()
for row in data:
    print(row[0])  # Access the line content
print('\n')  # Access the line content
print('\n')  # Access the line content

# Stop the Spark session
spark.stop()
