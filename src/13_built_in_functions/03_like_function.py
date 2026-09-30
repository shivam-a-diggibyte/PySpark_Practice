# use for pattern matching in PySpark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("like").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [(1, "Shivam"), (2, "Rahul"), (3, "Amit")],
    ["id", "name"]
)

df.where(df.name.like("S%")).show()

spark.stop()