from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("rename").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [(1, "Shivam"), (2, "Rahul")],
    ["id", "name"]
)

df.withColumnRenamed("name", "customer_name").show()

spark.stop()