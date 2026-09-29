from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("NestedData") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (1, "Shivam", ["Python", "SQL", "PySpark"]),
    (2, "Rahul", ["Java", "Spark"]),
    (3, "Amit", ["Python", "Databricks"])
]

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("skills", ArrayType(StringType()), True)
])

df = spark.createDataFrame(data, schema)
df.show(truncate=False)

df.select(
    col("name"),
    col("skills")[0].alias("first_skill")
).show()