from pyspark.sql.functions import col

def clean_employee_data(df):
    return (
        df
        .filter(col("salary") > 0)
        .dropDuplicates(["employee_id"])
    )