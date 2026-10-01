from pyspark.sql import SparkSession
spark = (
    SparkSession.builder
    .appName("Partitions")
    .master("local[*]")
    .getOrCreate()
)

df = spark.range(100)
print("Partitions:", df.rdd.getNumPartitions()) # to check  number of partitions

df2 = df.repartition(4)
print(df2.rdd.getNumPartitions())

df3 = df2.coalesce(2)
print(df3.rdd.getNumPartitions())

spark.stop()