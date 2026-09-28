from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("PySpark Practice")
    .master("local[*]")
    .getOrCreate()
)

print("Spark Version:", spark.version)

spark.stop()