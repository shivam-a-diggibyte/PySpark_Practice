# Removes duplicates based on selected columns.
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("dropDuplicates").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [(1, "Shivam", "Delhi"),
     (1, "Shivam", "Mumbai"),
     (2, "Rahul", "Pune")],
    ["id", "name", "city"]
)

df.dropDuplicates(["id"]).show()

spark.stop()