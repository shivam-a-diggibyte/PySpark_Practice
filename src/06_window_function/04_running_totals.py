from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count
from pyspark.sql.window import Window

spark = (
    SparkSession.builder
    .appName("Running Totals")
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

window_spec = (
    Window
    .orderBy("order_date")
    .rowsBetween(
        Window.unboundedPreceding,
        Window.currentRow
    )
)


# --------------------------------------------------
# RUNNING SUM
# --------------------------------------------------

result = df.withColumn(
    "running_total",
    sum("amount").over(window_spec)
)

print("RUNNING TOTAL:")
result.show()


# --------------------------------------------------
# RUNNING AVERAGE
# --------------------------------------------------

result = df.withColumn(
    "running_average",
    avg("amount").over(window_spec)
)

print("RUNNING AVERAGE:")
result.show()


# --------------------------------------------------
# RUNNING COUNT
# --------------------------------------------------

result = df.withColumn(
    "running_count",
    count("order_id").over(window_spec)
)

print("RUNNING COUNT:")
result.show()


spark.stop()