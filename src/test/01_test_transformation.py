from pyspark.sql import SparkSession

from util.transformations import (
    clean_employee_data,
)

spark = (
    SparkSession.builder
    .appName("TestTransformations")
    .master("local[2]")
    .getOrCreate()
)

def test_clean_employee_data():

    df = spark.createDataFrame(
        [
            (1, "Shivam", 50000),
            (2, "Rahul", 70000),
            (2, "Rahul", 70000),
            (3, "Amit", 0)
        ],
        ["employee_id", "name", "salary"]
    )

    result = clean_employee_data(df)

    assert result.count() == 2

    ids = {
        row["employee_id"]
        for row in result.collect()
    }

    assert ids == {1, 2}

spark.stop()