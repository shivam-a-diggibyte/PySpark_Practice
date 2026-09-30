from pyspark.sql import SparkSession
from util.transformations import (
    clean_employee_data,
)

spark = (
    SparkSession.builder
    .appName("ReusableTransformations")
    .master("local[*]")
    .getOrCreate()
)

df = spark.createDataFrame(
    [
        (1, "Shivam", 50000),
        (2, "Rahul", 70000),
        (3, "Amit", 45000),
        (2, "Rahul", 70000)
    ],
    ["employee_id", "name", "salary"]
)

clean_df = clean_employee_data(df)
clean_df.show()
spark.stop()