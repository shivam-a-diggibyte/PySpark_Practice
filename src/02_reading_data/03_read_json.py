from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Read JSON")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.json(
    "src/data/customers.json"
)

df.show()
df.printSchema()
spark.stop()