from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = (
    SparkSession.builder
    .appName("SCD_Type_2")
    .master("local[*]")
    .getOrCreate()
)

# Existing target table
target_df = spark.createDataFrame(
    [
        (101, "Shivam", "Delhi", "2026-01-01", None, True),
        (102, "Rahul", "Mumbai", "2026-01-01", None, True)
    ],
    [
        "customer_id",
        "name",
        "city",
        "start_date",
        "end_date",
        "is_current"
    ]
)

# New source data
source_df = spark.createDataFrame(
    [
        (101, "Shivam", "Bangalore"),
        (102, "Rahul", "Mumbai"),
        (103, "Amit", "Chennai")
    ],
    [
        "customer_id",
        "name",
        "city"
    ]
)

change_date = "2026-10-01"

# Join source and target
joined_df = (
    source_df.alias("s")
    .join(
        target_df.alias("t"),
        "customer_id",
        "left"
    )
)

# Changed records
changed_df = joined_df.filter(
    col("t.customer_id").isNotNull() &
    (
        (col("s.name") != col("t.name")) |
        (col("s.city") != col("t.city"))
    )
)

# Close old records
old_records = changed_df.select(
    col("t.customer_id").alias("customer_id"),
    col("t.name").alias("name"),
    col("t.city").alias("city"),
    col("t.start_date").alias("start_date"),
    lit(change_date).alias("end_date"),
    lit(False).alias("is_current")
)

# Create new versions
new_versions = changed_df.select(
    col("s.customer_id").alias("customer_id"),
    col("s.name").alias("name"),
    col("s.city").alias("city"),
    lit(change_date).alias("start_date"),
    lit(None).cast("string").alias("end_date"),
    lit(True).alias("is_current")
)

# New customers
new_records = source_df.join(
    target_df,
    "customer_id",
    "left_anti"
).select(
    col("customer_id"),
    col("name"),
    col("city"),
    lit(change_date).alias("start_date"),
    lit(None).cast("string").alias("end_date"),
    lit(True).alias("is_current")
)

# Unchanged existing records
changed_ids = changed_df.select("customer_id")

unchanged_records = target_df.join(
    changed_ids,
    "customer_id",
    "left_anti"
)

# Final SCD Type 2 table
final_df = (
    unchanged_records
    .unionByName(old_records)
    .unionByName(new_versions)
    .unionByName(new_records)
)

final_df.orderBy("customer_id", "start_date").show(
    truncate=False
)

spark.stop()