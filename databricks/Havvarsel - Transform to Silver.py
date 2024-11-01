# Databricks notebook source
from helpers.adls_utils import read_df_as_delta
df_bronze = read_df_as_delta("/bronze/hav_temperature_projection_latest")
display(df_bronze)

# COMMAND ----------

from pyspark.sql.functions import col, explode, from_unixtime

# Extract lat and lon, and select the first element from variables
df_silver = df_bronze.select(
    col("closestGridPointWithData.lat").alias("lat"),
    col("closestGridPointWithData.lon").alias("lon"),
    explode(col("variables")[0]["data"]).alias("data"),
    col("data.rawTime").alias("forecast_timestamp_utc"),
    col("data.value").alias("ocean_temperature"), 
    "depth_meters",
    "fetch_timestamp_utc"
) \
.drop("data") \
.withColumn("forecast_timestamp_utc", from_unixtime(col("forecast_timestamp_utc") / 1000))

display(df_silver)

# COMMAND ----------


from helpers.adls_utils import save_df_as_delta
save_df_as_delta(df_silver, "/silver/hav_temperature_projection_latest")

# COMMAND ----------

from helpers.adls_utils import read_df_as_delta
df_check_silver = read_df_as_delta("/silver/hav_temperature_projection_latest")
display(df_check_silver)
