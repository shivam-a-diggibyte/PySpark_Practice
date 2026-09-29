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


# 1. COUNT
print("COUNT:")
employees.groupBy("department_id").agg(
    count("employee_id").alias("employee_count")
).show()


# 2. COUNT DISTINCT
print("COUNT DISTINCT:")
employees.groupBy("department_id").agg(
    countDistinct("age").alias("distinct_ages")
).show()


# 3. SUM
print("SUM:")
employees.groupBy("department_id").agg(
    sum("salary").alias("total_salary")
).show()


# 4. AVG
print("AVG:")
employees.groupBy("department_id").agg(
    avg("salary").alias("average_salary")
).show()


# 5. MIN
print("MIN:")
employees.groupBy("department_id").agg(
    min("salary").alias("minimum_salary")
).show()


# 6. MAX
print("MAX:")
employees.groupBy("department_id").agg(
    max("salary").alias("maximum_salary")
).show()

# 11. MULTIPLE AGGREGATIONS
print("MULTIPLE AGGREGATIONS:")

result = employees.groupBy("department_id").agg(
    count("employee_id").alias("employee_count"),
    countDistinct("age").alias("distinct_ages"),
    sum("salary").alias("total_salary"),
    avg("salary").alias("average_salary"),
    min("salary").alias("minimum_salary"),
    max("salary").alias("maximum_salary")
)

result.show()

spark.stop()