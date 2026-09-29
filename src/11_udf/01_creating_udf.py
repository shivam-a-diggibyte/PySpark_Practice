from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder \
    .appName("UDFExample") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (1, 10),
    (2, 20),
    (3, 30)
]

df = spark.createDataFrame(
    data,
    ["id", "number"]
)

df.show()

# create a python function
def square(x):
    return x * x

# convert that function to udf
square_udf = udf(square, IntegerType())

df = df.withColumn(
    "square",
    square_udf("number")
)

df.show()