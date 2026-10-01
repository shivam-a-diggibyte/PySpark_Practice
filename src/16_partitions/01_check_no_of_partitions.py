from pyspark.sql import SparkSession
spark = (
    SparkSession.builder
    .appName("Partitions")
    .master("local[*]")
    .getOrCreate()
)

df = spark.range(100)

print("Partitions:", df.rdd.getNumPartitions())

spark.stop()