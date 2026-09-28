from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = (
    SparkSession.builder
    .appName("With Column")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Shivam", 25),
    (2, "Rahul", 26),
    (3, "Amit", 24)
]

columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)
df = df.withColumn("age_after_5_years", col("age") + 5)
df.show()
spark.stop()