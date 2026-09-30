# union rows based on position

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("union").master("local[*]").getOrCreate()

df1 = spark.createDataFrame([(1, "Shivam")], ["id", "name"])
df2 = spark.createDataFrame([(2, "Rahul")], ["id", "name"])

df1.union(df2).show()

spark.stop()