# Databricks notebook source
from helpers.adls_utils import read_df_as_delta
df_bronze_0 = read_df_as_delta("/bronze/hav_temperature_projection_latest")
display(df_bronze_0)

# COMMAND ----------

from pyspark.sql.functions import explode, from_unixtime, col

# Extract lat and lon, and explode variables
df_bronze_1 = df_bronze_0.select(
    col("closestGridPointWithData.lat").alias("lat"),
    col("closestGridPointWithData.lon").alias("lon"),
    explode(col("variables")).alias("variable"),
    "depth_meters"
)

display(df_bronze_1)

# COMMAND ----------

from pyspark.sql.functions import from_unixtime


# Extract fields from variable
df_bronze_2 = df_bronze_1.select(
    "lat",
    "lon",
    col("variable.variableName").alias("variable_name"),
    explode(col("variable.data")).alias("data"),
    col("data.rawTime").alias("time"),
    col("data.value").alias("ocean_temperature"), 
    "depth_meters"   
).drop("data")



display(df_bronze_2)

# COMMAND ----------

from pyspark.sql.functions import lit, col

# Convert time to readable format
df_bronze_3 = df_bronze_2.withColumn("time", from_unixtime(col("time") / 1000))


# Explode dimensions if necessary
df_silver = df_bronze_3.select(
    "lat",
    "lon",
    "variable_name",
    "time",
    "ocean_temperature",
    "depth_meters"
)

display(df_silver)


# COMMAND ----------


from helpers.adls_utils import save_df_as_delta
save_df_as_delta(df_silver, "/silver/hav_temperature_projection_latest")

# COMMAND ----------

from helpers.adls_utils import read_df_as_delta
df_check_silver = read_df_as_delta("/silver/hav_temperature_projection_latest")
display(df_check_silver)
