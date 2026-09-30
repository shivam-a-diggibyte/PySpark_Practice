# helps to fill null values in coulmns

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("fillna").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [(1, "Shivam", None), (2, None, 30)],
    ["id", "name", "age"]
)

df.fillna({"name": "Unknown", "age": 0}).show()

spark.stop()