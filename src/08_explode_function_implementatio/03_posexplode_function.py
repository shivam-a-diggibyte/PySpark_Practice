from pyspark.sql import SparkSession
from pyspark.sql.functions import posexplode
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    ArrayType
)

spark = SparkSession.builder \
    .appName("ExplodeExample") \
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
    "id",
    "name",
    posexplode("skills")
).show()