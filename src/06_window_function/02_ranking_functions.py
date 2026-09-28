from pyspark.sql import SparkSession
from pyspark.sql.functions import row_number, rank, dense_rank
from pyspark.sql.window import Window

spark = (
    SparkSession.builder
    .appName("Ranking Functions")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (101, "Shivam", 10, 45000),
    (102, "Amit", 10, 45000),
    (103, "Rahul", 10, 42000),
    (104, "Neha", 20, 55000),
    (105, "Priya", 20, 60000),
    (106, "Arjun", 20, 60000)
]

columns = [
    "employee_id",
    "name",
    "department_id",
    "salary"
]

df = spark.createDataFrame(data, columns)

df.show()


# --------------------------------------------------
# ROW_NUMBER
# --------------------------------------------------

window_spec = (
    Window
    .partitionBy("department_id")
    .orderBy("salary")
)

result = df.withColumn(
    "row_number",
    row_number().over(window_spec)
)

print("ROW_NUMBER:")
result.show()


# --------------------------------------------------
# RANK
# --------------------------------------------------

result = df.withColumn(
    "rank",
    rank().over(window_spec)
)

print("RANK:")
result.show()


# --------------------------------------------------
# DENSE_RANK
# --------------------------------------------------

result = df.withColumn(
    "dense_rank",
    dense_rank().over(window_spec)
)

print("DENSE_RANK:")
result.show()


# --------------------------------------------------
# Ranking by descending salary
# --------------------------------------------------

window_spec_desc = (
    Window
    .partitionBy("department_id")
    .orderBy(df.salary.desc())
)

result = df.withColumn(
    "salary_rank",
    dense_rank().over(window_spec_desc)
)

print("RANKING BY HIGHEST SALARY:")
result.show()


# --------------------------------------------------
# Top employee in each department
# --------------------------------------------------

result = (
    df
    .withColumn(
        "rank",
        row_number().over(window_spec_desc)
    )
    .filter("rank = 1")
)

print("TOP EMPLOYEE FROM EACH DEPARTMENT:")
result.show()


spark.stop()