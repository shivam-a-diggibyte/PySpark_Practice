from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    count,
    countDistinct,
    sum,
    avg,
    min,
    max,
)

spark = (
    SparkSession.builder
    .appName("Aggregations")
    .master("local[*]")
    .getOrCreate()
)

employees = spark.read.csv(
    "src/data/employees.csv",
    header=True,
    inferSchema=True
)

print("Original Data:")
employees.show()

# FILTER AFTER AGGREGATION
print("FILTER AFTER AGGREGATION:")

result = (
    employees
    .groupBy("department_id")
    .agg(
        sum("salary").alias("total_salary")
    )
    .filter("total_salary > 100000")
    )

result.show()