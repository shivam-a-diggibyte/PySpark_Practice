from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def clean_employee_data(df: DataFrame) -> DataFrame:
    return (
        df
        .filter(col("salary") > 0)
        .dropDuplicates(["employee_id"])
    )