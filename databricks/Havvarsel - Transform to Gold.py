# Databricks notebook source
from helpers.adls_utils import read_df_as_delta
df_silver = read_df_as_delta("/silver/hav_temperature_projection_latest")
display(df_silver)

# COMMAND ----------

from datetime import datetime

# Convert the current datetime to a string in the appropriate format
current_time_str = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
df_silver = df_silver.where(f"forecast_timestamp_utc >= '{current_time_str}'")

# COMMAND ----------

display(df_silver)

# COMMAND ----------

import pytz
from datetime import datetime
from pyspark.sql.functions import from_utc_timestamp, udf, col
from pyspark.sql.types import StringType
from dateutil import parser 


# Custom function to transform a timestamp to the Europe/Oslo timezone
def transform_to_local_timezone(utc_time_str):
    # Parse the string to a naive datetime object (assuming it is in UTC)
    utc_time = datetime.strptime(utc_time_str, '%Y-%m-%d %H:%M:%S')
    # Make it timezone-aware in UTC
    utc_time = pytz.utc.localize(utc_time)

    # Convert to Europe/Oslo timezone
    local_time = utc_time.astimezone(pytz.timezone("Europe/Oslo"))

    # Return formatted time as a string with timezone offset
    return local_time.strftime('%Y-%m-%d %H:%M:%S %z')  # Includes the timezone offset


# Register the function as a UDF
transform_to_local_timezone_udf = udf(transform_to_local_timezone, StringType())

# COMMAND ----------

df_silver_time_transformed = df_silver \
    .withColumn(
        "fetch_timestamp_local",
        transform_to_local_timezone_udf(col("fetch_timestamp_utc").cast(StringType()))
    ) \
    .withColumn(
        "forecast_timestamp_local",
        transform_to_local_timezone_udf(col("forecast_timestamp_utc").cast(StringType()))
    )

# COMMAND ----------

display(df_silver_time_transformed)

# save as a mangaged table for SQL Dashboards
df_silver_time_transformed.write.format("delta").mode("overwrite").saveAsTable("gold_hav_temperature_projection_latest")


# COMMAND ----------

from helpers.adls_utils import save_df_as_csv
save_df_as_csv(df_silver_time_transformed, "/gold/hav_temperature_projection_latest")

# COMMAND ----------

from helpers.adls_utils import get_adls_folder_path
from datetime import datetime

gold_path = f"{get_adls_folder_path()}/gold"
hav_gold_folder= f"{gold_path}/hav_temperature_projection_latest"
files = dbutils.fs.ls(hav_gold_folder)

old_file = [file.path for file in files if file.name.startswith("part-")][0]

today = datetime.now().strftime("%Y-%m-%d")
destination_path = f"{gold_path}/havtemp-pred-latest.csv"
dbutils.fs.mv(old_file, destination_path)

# COMMAND ----------

dbutils.fs.rm(hav_gold_folder, recurse=True)

