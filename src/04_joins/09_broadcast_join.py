from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder \
    .appName("Broadcast_Join") \
    .master("local[*]") \
    .getOrCreate()

employees = spark.createDataFrame(
    [
        (1, "Shivam", 10),
        (2, "Rahul", 20),
        (3, "Amit", 10)
    ],
    ["employee_id", "name", "department_id"]
)

departments = spark.createDataFrame(
    [
        (10, "IT"),
        (20, "HR")
    ],
    ["department_id", "department"]
)

result = employees.join(
    broadcast(departments),
    "department_id"
)

result.show()