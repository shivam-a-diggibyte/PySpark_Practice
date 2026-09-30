from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SCD_Type_0")
    .master("local[*]")
    .getOrCreate()
)

# Existing target dimension
target_df = spark.createDataFrame(
    [
        (101, "Shivam", "Delhi"),
        (102, "Rahul", "Mumbai")
    ],
    ["customer_id", "name", "city"]
)

# Incoming source data
source_df = spark.createDataFrame(
    [
        (101, "Shivam", "Bangalore"),
        (102, "Rahul", "Pune"),
        (103, "Amit", "Chennai")
    ],
    ["customer_id", "name", "city"]
)

# Find only completely new customers
new_records = source_df.join(
    target_df,
    on="customer_id",
    how="left_anti"
)

# Add new customers to the existing target
final_df = target_df.unionByName(new_records)

print("Final SCD Type 0 Data:")
final_df.show()
spark.stop()