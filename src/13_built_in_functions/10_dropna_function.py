# removes the rows containing null values

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("dropna").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [(1, "Shivam", 25), (2, None, 30), (3, "Amit", None)],
    ["id", "name", "age"]
)

df.dropna().show()

spark.stop()