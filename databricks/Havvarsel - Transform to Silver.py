# Databricks notebook source
df_bronze_0 = spark.read.format("delta").load("/mnt/data/bronze/hav_temperature_projection_latest")
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


silver_latest_path = "/mnt/data/silver/hav_temperature_projection_latest"
df_silver.write.format("delta").mode("overwrite").save(silver_latest_path)

# COMMAND ----------

df_check_silver = spark.read.format("delta").load(silver_latest_path)

display(df_check_silver)
