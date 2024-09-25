# Databricks notebook source
from pyspark.sql.functions import explode
import requests

url = "https://api.havvarsel.no/apis/duapi/havvarsel/v2/depths"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

depth_data = response.json()
depth_df = spark.read.json(sc.parallelize([depth_data]))
# Explode the depthItems array to flatten it
depth_df_flat = depth_df.select(explode("depthItems").alias("depthItem"))

# Select the depthIndex and depthValue from the flattened structure
depth_data = depth_df_flat.select(
    "depthItem.depthIndex",
    "depthItem.depthValue"
)

# COMMAND ----------

from helpers.adls_utils import save_df_as_delta
save_df_as_delta(depth_data, "depth_index_to_meter_mapping")


# COMMAND ----------

from helpers.adls_utils import read_df_as_delta

df = read_df_as_delta("depth_index_to_meter_mapping")
display(df)

