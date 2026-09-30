from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sort").master("local[*]").getOrCreate()

df = spark.createDataFrame(
    [(1, "Shivam", 25), (2, "Rahul", 30), (3, "Amit", 22)],
    ["id", "name", "age"]
)

df.sort("age").show()

spark.stop()

# for descending order
# df.sort(df.age.desc()).show()