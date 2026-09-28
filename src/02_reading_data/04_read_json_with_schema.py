from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = (
    SparkSession.builder
    .appName("Read JSON With Schema")
    .master("local[*]")
    .getOrCreate()
)

schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("city", StringType(), True),
    StructField("age", IntegerType(), True)
])

df = spark.read.json(
    "src/data/customers.json",
    schema=schema
)

df.show()
df.printSchema()

spark.stop()