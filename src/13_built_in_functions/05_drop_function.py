# removes column in PySpark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("drop").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [(1, "Shivam", 25), (2, "Rahul", 30)],
    ["id", "name", "age"]
)

df.drop("age").show()

spark.stop()