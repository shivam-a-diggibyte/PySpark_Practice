from pyspark.sql import SparkSession
spark = (
    SparkSession.builder
    .appName("Group By")
    .master("local[*]")
    .getOrCreate()
)

employees = spark.read.csv(
    "src/data/employees.csv",
    header=True,
    inferSchema=True
)

result = employees.groupBy("department_id").count()
result.show()
spark.stop()