from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json

spark = SparkSession.builder \
    .appName("FromJsonExample") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (1, '{"name":"Shivam","age":25}'),
    (2, '{"name":"Rahul","age":30}'),
    (3, '{"name":"Amit","age":28}')
]

df = spark.createDataFrame(
    data,
    ["id", "customer_data"]
)

df.show(truncate=False)
# it will show customer_data as a string

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType
)

customer_schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

df_parsed = df.withColumn(
    "customer",
    from_json("customer_data", customer_schema)
)

df_parsed.show(truncate=False)