from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = SparkSession.builder \
    .appName("StructExample") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (1, ("Shivam", 25, "Bangalore")),
    (2, ("Rahul", 30, "Chennai")),
    (3, ("Amit", 28, "Delhi"))
]
schema = StructType([                      # created a struct schema 
    StructField("id", IntegerType(), True),

    StructField(
        "customer",
        StructType([
            StructField("name", StringType(), True),
            StructField("age", IntegerType(), True),
            StructField("city", StringType(), True)
        ]),
        True
    )
])
df = spark.createDataFrame(data, schema)
df.show(truncate=False)

# method 1, using dot notation
df.select(
    "customer.name"
).show()

# method 2, using col
df.select(
    col("customer.name").alias("customer_name"),
    col("customer.age").alias("customer_age"),
    col("customer.city").alias("customer_city")
).show()