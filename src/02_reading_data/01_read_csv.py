from pyspark.sql import SparkSession
spark = (
    SparkSession.builder
    .appName("Read CSV")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.csv(
    "src/data/employees.csv",
    header=True,
    inferSchema=True
)

df.show()
df.printSchema()
spark.stop()