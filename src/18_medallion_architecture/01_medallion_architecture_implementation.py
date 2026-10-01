from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    trim,
    upper,
    current_timestamp,
    sum
)
spark = (
    SparkSession.builder
    .appName("MedallionArchitecture")
    .master("local[*]")
    .getOrCreate()
)
source_df = spark.createDataFrame(
    [
        (1, " Shivam ", "Bangalore", 50000),
        (2, "Rahul", "Bengaluru", 60000),
        (3, "Amit", "Chennai", 45000),
        (1, " Shivam ", "Bangalore", 50000),
        (4, None, "Mumbai", -1000)
    ],
    ["customer_id", "name", "city", "salary"]
)
# Bronze Layer: Raw Data

bronze_df = (
    source_df
    .withColumn(
        "_ingestion_timestamp",
        current_timestamp()
    )
)

bronze_df.show()
bronze_df.write.mode("append").format("delta").saveAsTable(
    "bronze.customer_raw"
)

# Silver Layer: Cleaned Data

silver_df = (
    bronze_df
    .withColumn("name", trim(col("name")))
    .withColumn("city", upper(col("city")))
    .filter(col("salary") >= 0)
)

silver_df.show()
silver_df.write.mode("overwrite").format("delta").saveAsTable(
    "silver.customer_cleaned"
)

gold_df = (
    silver_df
    .groupBy("city")
    .agg(
        sum("salary").alias("total_salary")
    )
)
gold_df.show()
gold_df.write.mode("overwrite").format("delta").saveAsTable(
    "gold.customer_summary"
)
