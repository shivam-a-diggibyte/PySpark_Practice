from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

spark = (
    SparkSession.builder
    .appName("Read CSV With Schema")
    .master("local[*]")
    .getOrCreate()
)

schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("department_id", IntegerType(), True),
    StructField("age", IntegerType(), True),
    StructField("salary", IntegerType(), True)
])

df = spark.read.csv(
    "src/data/employees.csv",
    header=True,
    schema=schema
)

df.show()
df.printSchema()
spark.stop()