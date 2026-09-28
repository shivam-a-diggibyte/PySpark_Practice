from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import IntegerType, StringType

spark = (
    SparkSession.builder
    .appName("Explicit Schema")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Shivam", 25),
    (2, "Rahul", 26),
    (3, "Amit", 24)
]

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

df = spark.createDataFrame(data, schema)

df.printSchema()
df.show()
spark.stop()