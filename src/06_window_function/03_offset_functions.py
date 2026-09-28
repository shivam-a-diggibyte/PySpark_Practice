from pyspark.sql import SparkSession
from pyspark.sql.functions import lag, lead, col
from pyspark.sql.window import Window

spark = (
    SparkSession.builder
    .appName("Offset Functions")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "2026-09-01", 1000),
    (2, "2026-09-02", 1500),
    (3, "2026-09-03", 1200),
    (4, "2026-09-04", 1800),
    (5, "2026-09-05", 2000)
]

columns = [
    "order_id",
    "order_date",
    "amount"
]

df = spark.createDataFrame(data, columns)

window_spec = Window.orderBy("order_date")


# --------------------------------------------------
# LAG
# --------------------------------------------------

result = df.withColumn(
    "previous_amount",
    lag("amount", 1).over(window_spec)
)

print("LAG:")
result.show()


# --------------------------------------------------
# LEAD
# --------------------------------------------------

result = df.withColumn(
    "next_amount",
    lead("amount", 1).over(window_spec)
)

print("LEAD:")
result.show()


# --------------------------------------------------
# LAG + Difference
# --------------------------------------------------

result = (
    df
    .withColumn(
        "previous_amount",
        lag("amount", 1).over(window_spec)
    )
    .withColumn(
        "difference_from_previous",
        col("amount") - col("previous_amount")
    )
)

print("CURRENT VS PREVIOUS:")
result.show()


# --------------------------------------------------
# LEAD + Difference
# --------------------------------------------------

result = (
    df
    .withColumn(
        "next_amount",
        lead("amount", 1).over(window_spec)
    )
    .withColumn(
        "difference_from_next",
        col("next_amount") - col("amount")
    )
)

print("CURRENT VS NEXT:")
result.show()


spark.stop()