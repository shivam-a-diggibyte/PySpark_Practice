from pyspark.sql import SparkSession
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