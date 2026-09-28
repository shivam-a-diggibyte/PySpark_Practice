from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Joins") \
    .master("local[*]") \
    .getOrCreate()

customers_data = [
    (1, "Shivam"),
    (2, "Rahul"),
    (3, "Priya"),
    (4, "Amit")
]

orders_data = [
    (101, 1, 500),
    (102, 2, 700),
    (103, 1, 300),
    (104, 5, 900)
]

customers = spark.createDataFrame(
    customers_data,
    ["customer_id", "name"]
)

orders = spark.createDataFrame(
    orders_data,
    ["order_id", "customer_id", "amount"]
)
customers.show()
orders.show()

result = customers.join(orders, how="cross")

result.show()