# it's an alias for the union

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("unionAll").master("local[*]").getOrCreate()

df1 = spark.createDataFrame([(1, "Shivam")], ["id", "name"])
df2 = spark.createDataFrame([(2, "Rahul")], ["id", "name"])

df1.unionAll(df2).show()

spark.stop()