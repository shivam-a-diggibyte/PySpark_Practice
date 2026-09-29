from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    ArrayType
)
from pyspark.sql.functions import explode

spark = SparkSession.builder \
    .appName("ArrayOfStructExample") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (
        101,
        "Shivam",
        [
            (1, "Laptop", 50000),
            (2, "Mouse", 2000)
        ]
    ),
    (
        102,
        "Rahul",
        [
            (3, "Keyboard", 3000),
            (4, "Monitor", 15000)
        ]
    )
]

order_schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("product", StringType(), True),
    StructField("amount", IntegerType(), True)
])

schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField(
        "orders",
        ArrayType(order_schema),
        True
    )
])

df = spark.createDataFrame(data, schema)
df.printSchema()
df.show(truncate=False)

result = df.select(
    "customer_id",
    "name",
    explode("orders").alias("order")
)

result.select(
    "customer_id",
    "name",
    "order.order_id",
    "order.product",
    "order.amount"
).show()

spark.stop()