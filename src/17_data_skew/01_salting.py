from pyspark.sql import SparkSession
spark = (
    SparkSession.builder
    .appName("SaltingExample")
    .master("local[*]")
    .getOrCreate()
)
df = spark.createDataFrame(
    [
        (999, 100),
        (999, 200),
        (999, 300),
        (999, 400),
        (999, 500),
        (1, 100),
        (2, 200),
        (3, 300)
    ],
    ["customer_id", "amount"]
)

df.show()

# Createing salted column to avoid data skewness in join operation. Salted column will have random values between 0 to 4.
from pyspark.sql.functions import floor, rand

salted_df = df.withColumn(
    "salt",
    floor(rand() * 5)
)

salted_df.show()