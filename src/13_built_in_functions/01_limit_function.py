from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Limit").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [
        (1, "Shivam", "Delhi"),
        (2, "Rahul", "Mumbai"),
        (3, "Amit", "Chennai"),
        (4, "Ravi", "Pune"),
        (5, "Vikas", "Kolkata")
    ],
    ["id", "name", "city"]
)

df.limit(3).show()

spark.stop()