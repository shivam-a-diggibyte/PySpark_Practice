from pyspark.sql import SparkSession
from pyspark.sql.functions import coalesce, col

spark = (
    SparkSession.builder
    .appName("SCD_Type_1_Coalesce")
    .master("local[*]")
    .getOrCreate()
)

# Target table
target_df = spark.createDataFrame(
    [
        (101, "Shivam", "Delhi"),
        (102, "Rahul", "Mumbai")
    ],
    ["customer_id", "name", "city"]
)

# Source data
source_df = spark.createDataFrame(
    [
        (101, "Shivam Kumar", None),
        (102, None, "Pune"),
        (103, "Amit", "Chennai")
    ],
    ["customer_id", "name", "city"]
)

# Join source and target
updated_df = (
    target_df.alias("t")
    .join(
        source_df.alias("s"),
        "customer_id",
        "full_outer"
    )
    .select(
        col("customer_id"),

        coalesce(
            col("s.name"),
            col("t.name")
        ).alias("name"),

        coalesce(
            col("s.city"),
            col("t.city")
        ).alias("city")
    )
)

updated_df.orderBy("customer_id").show()

spark.stop()