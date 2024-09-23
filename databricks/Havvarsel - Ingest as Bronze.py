# Databricks notebook source
# Query Parameters
depth_index = 2 # 10m - look it up on the depth index table. 
lat = 5.32
lon = 60.39



# COMMAND ----------

import requests
from pyspark.sql.functions import lit

url = f"https://api.havvarsel.no/apis/duapi/havvarsel/v2/temperatureprojection/{lat}/{lon}?depth={depth_index}"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

data = response.json()
df_raw = spark.read.json(sc.parallelize([data]))




# COMMAND ----------

depth_data = spark.table("havvarsel_depth_index_to_meter_mapping")
depth_m = depth_data.filter(depth_data.depthIndex == depth_index).collect()[0].depthValue
fetch_date = datetime.now().strftime("%Y-%m-%d")

df_bronze = df_raw.withColumn("depth_meters", lit(depth_m)).withColumn("fetch_date", lit(fetch_date))

# COMMAND ----------

from datetime import datetime

bronze_fetch_date_path = f"/mnt/data/bronze/hav_temperature_projection_{fetch_date}"
bronze_latest_data_path = "/mnt/data/bronze/hav_temperature_projection_latest"

df_bronze.write.format("delta").mode("overwrite").save(bronze_fetch_date_path)
df_bronze.write.format("delta").mode("overwrite").save(bronze_latest_data_path)


