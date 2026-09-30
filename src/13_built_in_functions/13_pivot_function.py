# converts rows into column
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("pivot").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [
        ("Shivam", "Sales", 100),
        ("Shivam", "IT", 200),
        ("Rahul", "Sales", 300),
        ("Rahul", "IT", 400)
    ],
    ["name", "department", "amount"]
)

df.groupBy("name") \
  .pivot("department") \
  .agg(sum("amount")) \
  .show()

spark.stop()