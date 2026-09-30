from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("where").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [(1, "Shivam", 25), (2, "Rahul", 30), (3, "Amit", 22)],
    ["id", "name", "age"]
)

df.where(df.age > 25).show()

spark.stop()