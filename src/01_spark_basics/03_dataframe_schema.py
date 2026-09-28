from pyspark.sql import SparkSession
spark = (
    SparkSession.builder
    .appName("DataFrame Schema")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Shivam", 25),
    (2, "Rahul", 26),
    (3, "Amit", 24)
]

columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)
df.printSchema()
spark.stop()