from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
from pyspark.sql.window import Window

spark = (
    SparkSession.builder
    .appName("Window Basics")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (101, "Shivam", 10, 45000),
    (102, "Amit", 10, 42000),
    (103, "Rahul", 20, 50000),
    (104, "Neha", 20, 55000),
    (105, "Priya", 30, 60000),
    (106, "Arjun", 30, 65000)
]

columns = [
    "employee_id",
    "name",
    "department_id",
    "salary"
]

df = spark.createDataFrame(data, columns)

print("Original Data:")
df.show()

window_spec = Window.partitionBy("department_id")

result = df.withColumn(
    "avg_department_salary",
    avg("salary").over(window_spec)
)

print("Window Function Result:")
result.show()

spark.stop()