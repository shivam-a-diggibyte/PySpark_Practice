> A quick-reference sheet for the PySpark operations covered in training.

---

# 1. SparkSession

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .master("local[*]") \
    .getOrCreate()

spark.stop()
```

---

# 2. Create DataFrame

## From Python data

```python
data = [
    (1, "Shivam", 25),
    (2, "Rahul", 30)
]

df = spark.createDataFrame(
    data,
    ["id", "name", "age"]
)
```

## With explicit schema

```python
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

df = spark.createDataFrame(data, schema)
```

---

# 3. DataFrame Inspection

```python
df.show()
df.show(10)
df.show(truncate=False)

df.printSchema()

df.schema
df.dtypes
df.columns
df.count()
len(df.columns)

df.describe().show()
```

---

# 4. Read CSV

```python
df = spark.read.csv(
    "file.csv",
    header=True,
    inferSchema=True
)
```

## With explicit schema

```python
df = spark.read.csv(
    "file.csv",
    header=True,
    schema=schema
)
```

---

# 5. Read JSON

```python
df = spark.read.json("file.json")
```

```python
df = spark.read.json(
    "file.json",
    schema=schema
)
```

---

# 6. Read Parquet

```python
df = spark.read.parquet("file.parquet")
```

---

# 7. Read Delta

```python
df = spark.read \
    .format("delta") \
    .load("path")
```

---

# 8. Write CSV

```python
df.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output_path")
```

---

# 9. Write JSON

```python
df.write \
    .mode("overwrite") \
    .json("output_path")
```

---

# 10. Write Parquet

```python
df.write \
    .mode("overwrite") \
    .parquet("output_path")
```

---

# 11. Write Delta

```python
df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("output_path")
```

---

# 12. Select

```python
df.select("name", "age").show()
```

```python
from pyspark.sql.functions import col

df.select(
    col("name"),
    col("age")
).show()
```

```python
df.select(
    col("name"),
    (col("age") + 1).alias("next_age")
).show()
```

---

# 13. Filter 

```python
df.filter(
    col("age") > 18
).show()
```

## Multiple conditions

```python
df.filter(
    (col("age") > 18) &
    (col("city") == "Delhi")
).show()
```


---

# 14. withColumn()

```python
df = df.withColumn(
    "double_age",
    col("age") * 2
)
```

```python
df = df.withColumn(
    "age",
    col("age") + 1
)
```

---

# 15. when() / otherwise()

```python
from pyspark.sql.functions import when

df = df.withColumn(
    "category",
    when(col("age") >= 18, "Adult")
    .otherwise("Minor")
)
```

## Multiple conditions

```python
df = df.withColumn(
    "category",
    when(col("age") >= 60, "Senior")
    .when(col("age") >= 18, "Adult")
    .otherwise("Minor")
)
```

---

# 16. Alias

```python
df.select(
    col("name").alias("customer_name")
).show()
```

---

# 17. Rename Columns

```python
df = df.withColumnRenamed(
    "name",
    "customer_name"
)
```

---

# 18. Drop Columns

```python
df = df.drop("age")
```

```python
df = df.drop("age", "city")
```

---

# 19. Drop Duplicates

```python
df = df.dropDuplicates()
```

```python
df = df.dropDuplicates(
    ["customer_id"]
)
```

---

# 20. String Functions

```python
from pyspark.sql.functions import (
    upper,
    lower,
    length,
    trim,
    ltrim,
    rtrim,
    substring,
    concat,
    concat_ws,
    regexp_replace
)
```

```python
upper("name")
lower("name")
length("name")
trim("name")
ltrim("name")
rtrim("name")
substring("name", 1, 3)
```

```python
df.withColumn(
    "full_name",
    concat_ws(" ", "first_name", "last_name")
)
```

```python
df.withColumn(
    "clean_phone",
    regexp_replace(
        "phone",
        "[^0-9]",
        ""
    )
)
```

---

# 21. Date and Timestamp Functions

```python
from pyspark.sql.functions import (
    current_date,
    current_timestamp,
    to_date,
    to_timestamp
)
```

```python
df.withColumn(
    "today",
    current_date()
)
```

```python
df.withColumn(
    "current_time",
    current_timestamp()
)
```

```python
df.withColumn(
    "date",
    to_date("date_string", "yyyy-MM-dd")
)
```

```python
df.withColumn(
    "timestamp",
    to_timestamp(
        "timestamp_string",
        "yyyy-MM-dd HH:mm:ss"
    )
)
```

---

# 22. Aggregation Functions

```python
from pyspark.sql.functions import (
    count,
    countDistinct,
    sum,
    avg,
    min,
    max
)
```

```python
df.select(
    count("*").alias("total")
).show()
```

```python
df.select(
    countDistinct("customer_id")
).show()
```

```python
df.select(
    sum("salary").alias("total_salary")
).show()
```

```python
df.select(
    avg("salary").alias("average_salary")
).show()
```

```python
df.select(
    min("salary").alias("minimum_salary")
).show()
```

```python
df.select(
    max("salary").alias("maximum_salary")
).show()
```

---

# 23. groupBy()

```python
df.groupBy("department").count().show()
```

```python
df.groupBy(
    "department",
    "city"
).count().show()
```

---

# 24. groupBy() + agg()

```python
df.groupBy("department").agg(
    sum("salary").alias("total_salary"),
    avg("salary").alias("avg_salary"),
    min("salary").alias("min_salary"),
    max("salary").alias("max_salary"),
    count("*").alias("employee_count")
).show()
```

---

# 25. Joins

## Inner

```python
df1.join(
    df2,
    df1.id == df2.id,
    "inner"
)
```

## Left

```python
df1.join(
    df2,
    df1.id == df2.id,
    "left"
)
```

## Right

```python
df1.join(
    df2,
    df1.id == df2.id,
    "right"
)
```

## Full Outer

```python
df1.join(
    df2,
    df1.id == df2.id,
    "full"
)
```

## Left Semi

```python
df1.join(
    df2,
    df1.id == df2.id,
    "left_semi"
)
```

## Left Anti

```python
df1.join(
    df2,
    df1.id == df2.id,
    "left_anti"
)
```

## Same join-key name

```python
df1.join(
    df2,
    "id",
    "inner"
)
```

---

# 26. Arrays

```python
from pyspark.sql.types import ArrayType
```

```python
ArrayType(StringType())
ArrayType(IntegerType())
```

## Access an array element

```python
df.select(
    col("skills")[0].alias("first_skill")
)
```

## Array size

```python
from pyspark.sql.functions import size

df.withColumn(
    "skill_count",
    size("skills")
)
```

## Create an array

```python
from pyspark.sql.functions import array

df.withColumn(
    "skills",
    array("skill1", "skill2", "skill3")
)
```

---

# 27. explode()

## Array

```python
from pyspark.sql.functions import explode

df.select(
    "id",
    explode("skills").alias("skill")
).show()
```

## Map

```python
df.select(
    "id",
    explode("details").alias("key", "value")
).show()
```

---

# 28. explode_outer()

```python
from pyspark.sql.functions import explode_outer

df.select(
    "id",
    explode_outer("skills").alias("skill")
).show()
```

---

# 29. posexplode()

```python
from pyspark.sql.functions import posexplode

df.select(
    "id",
    posexplode("skills").alias(
        "position",
        "skill"
    )
).show()
```

---

# 30. posexplode_outer()

```python
from pyspark.sql.functions import posexplode_outer

df.select(
    "id",
    posexplode_outer("skills").alias(
        "position",
        "skill"
    )
).show()
```

---

# 31. Structs

## Define StructType

```python
from pyspark.sql.types import (
    StructType,
    StructField
)

address_schema = StructType([
    StructField("city", StringType(), True),
    StructField("state", StringType(), True)
])
```

## Create struct

```python
from pyspark.sql.functions import struct

df.withColumn(
    "address",
    struct("city", "state")
)
```

## Access struct field

```python
df.select(
    "address.city"
)
```

## Nested struct

```python
df.select(
    "customer.address.city"
)
```

---

# 32. Array of Structs

```python
order_schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("product", StringType(), True),
    StructField("amount", DoubleType(), True)
])

orders_schema = ArrayType(order_schema)
```

```python
df.select(
    "customer_id",
    explode("orders").alias("order")
)
```

```python
df.select(
    "customer_id",
    "order.order_id",
    "order.product",
    "order.amount"
)
```

---

# 33. from_json()

## JSON string → Struct

```python
from pyspark.sql.functions import from_json

customer_schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

df = df.withColumn(
    "customer",
    from_json(
        "customer_data",
        customer_schema
    )
)
```

## Access parsed fields

```python
df.select(
    "customer.name",
    "customer.age"
)
```

---

# 34. from_json() + Array of Structs

```python
order_schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("product", StringType(), True),
    StructField("amount", DoubleType(), True)
])

orders_schema = ArrayType(order_schema)

df = df.withColumn(
    "orders",
    from_json(
        "orders_json",
        orders_schema
    )
)

df = df.select(
    "customer_id",
    explode("orders").alias("order")
)

df.select(
    "customer_id",
    "order.order_id",
    "order.product",
    "order.amount"
)
```

---

# 35. UDF — User Defined Function

```python
from pyspark.sql.functions import udf
```

```python
def square(x):
    return x * x

square_udf = udf(
    square,
    IntegerType()
)

df.withColumn(
    "square",
    square_udf("number")
)
```

## String UDF

```python
def make_upper(name):
    return name.upper()

upper_udf = udf(
    make_upper,
    StringType()
)

df.withColumn(
    "upper_name",
    upper_udf("name")
)
```

## Conditional UDF

```python
def age_category(age):
    if age >= 18:
        return "Adult"
    return "Minor"

age_category_udf = udf(
    age_category,
    StringType()
)

df.withColumn(
    "category",
    age_category_udf("age")
)
```

### UDF rule

```text
Built-in function → first choice
UDF → use when necessary
```

---

# 36. Temporary Views

```python
df.createOrReplaceTempView(
    "customers"
)
```

```python
spark.sql("""
    SELECT *
    FROM customers
""").show()
```

---

# 37. Tables

## Write DataFrame as table

```python
df.write \
    .mode("overwrite") \
    .saveAsTable("customers")
```

## Read table

```python
df = spark.table("customers")
```

## SQL read

```python
df = spark.sql("""
    SELECT *
    FROM customers
""")
```

---

# 38. Table Write Modes

## Overwrite

```python
df.write \
    .mode("overwrite") \
    .saveAsTable("customers")
```

## Append

```python
df.write \
    .mode("append") \
    .saveAsTable("customers")
```

## Ignore

```python
df.write \
    .mode("ignore") \
    .saveAsTable("customers")
```

## Error if table exists

```python
df.write \
    .mode("error") \
    .saveAsTable("customers")
```

---

# 39. Delta Tables

## Write

```python
df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("delta_path")
```

## Read

```python
df = spark.read \
    .format("delta") \
    .load("delta_path")
```

---


# 40. Load Concepts

## Full load

```python
source_df = spark.read.csv(
    "source.csv",
    header=True,
    inferSchema=True
)

source_df.write \
    .mode("overwrite") \
    .saveAsTable("target_table")
```

## Append load

```python
new_df.write \
    .mode("append") \
    .saveAsTable("target_table")
```

## Incremental load by timestamp

```python
incremental_df = df.filter(
    col("updated_at") > last_load_time
)
```

---

# 41. Window Functions

## Imports

```python
from pyspark.sql.window import Window

from pyspark.sql.functions import (
    row_number,
    rank,
    dense_rank
)
```

## Define window

```python
window_spec = Window \
    .partitionBy("department") \
    .orderBy(col("salary").desc())
```

## row_number()

```python
df.withColumn(
    "row_num",
    row_number().over(window_spec)
)
```

## rank()

```python
df.withColumn(
    "rank",
    rank().over(window_spec)
)
```

## dense_rank()

```python
df.withColumn(
    "dense_rank",
    dense_rank().over(window_spec)
)
```

---

# 42. Window Aggregations

```python
from pyspark.sql.functions import sum

window_spec = Window \
    .partitionBy("department") \
    .orderBy("date") \
    .rowsBetween(
        Window.unboundedPreceding,
        Window.currentRow
    )

df.withColumn(
    "running_total",
    sum("sales").over(window_spec)
)
```

---

# 43. Useful Column Operations

```python
col("salary") + 1000
col("salary") - 1000
col("salary") * 2
col("salary") / 2

col("age") > 18
col("age") >= 18
col("age") == 18
col("age") != 18
```

---

# 44. Sort / Order By

```python
df.orderBy(
    col("age").asc()
)
```

```python
df.orderBy(
    col("age").desc()
)
```

```python
df.orderBy(
    col("city").asc(),
    col("age").desc()
)
```
---

# 45. Common Data Types

```python
from pyspark.sql.types import (
    StringType,
    IntegerType,
    LongType,
    FloatType,
    DoubleType,
    BooleanType,
    DateType,
    TimestampType,
    ArrayType,
    MapType,
    StructType,
    StructField
)
```

---

