from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder \
    .appName("String_UDF_Example") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (1, "shivam"),
    (2, "rahul"),
    (3, "amit")
]

df = spark.createDataFrame(
    data,
    ["id", "name"]
)

def make_upper(name):
    return name.upper()

upper_udf = udf(make_upper, StringType())

df.withColumn(
    "upper_name",
    upper_udf("name")
).show()