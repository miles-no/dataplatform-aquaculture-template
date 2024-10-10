# Databricks notebook source
depth_indices = [0, 1, 2, 3] # [0m, 3m, 10m, 15m] below sea level
locations = [
     {"lat": 14.565382891612964, "lon": 68.22784304432557}, #Lofoten, Svolvær
      {"lat": 13.62931782826355, "lon": 68.08787504064836}, #Lofoten, Buksnesfjorden
      {"lat": 14.814009616694364, "lon": 68.44104810992098} #Ofoten, Melbu
] 

# COMMAND ----------

def fetch_ocean_temperature_preditions(depth_index, lat, lon):
    url = f"https://api.havvarsel.no/apis/duapi/havvarsel/v2/temperatureprojection/{lat}/{lon}?depth={depth_index}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()


# COMMAND ----------

depth_data = spark.table("havvarsel_depth_index_to_meter_mapping")


# COMMAND ----------

import requests
from pyspark.sql.functions import lit, current_timestamp, date_format
from datetime import datetime 
from helpers.adls_utils import save_df_as_delta, get_adls_folder_path, connect_to_adls
connect_to_adls()

fetch_time = datetime.utcnow()
formatted_time = fetch_time.strftime("%Y-%m-%dT%H%M%S")

bronze_df_file_name = f"bronze/hav_temperature_projection_{formatted_time}" # have a new bronze for each fetch date

print(bronze_df_file_name)

dbutils.fs.rm(f"{get_adls_folder_path()}/{bronze_df_file_name}", recurse=True) # delete old in order to remove duplicates


# COMMAND ----------


for loc_nr, location in enumerate(locations):
    for depth_index in depth_indices:
        print(f"Fetching data for depth index {depth_index} at location ({location['lat']}, {location['lon']})")
        data = fetch_ocean_temperature_preditions(depth_index, location["lat"], location["lon"])
        if ("code" in data and data["code"] == 404): 
            print("-- Error, message: ", data["message"])
            continue
        
        df_raw = spark.read.json(sc.parallelize([data]))

        # add depth info and fetch date in order to have metadata in the table
        depth_m = depth_data.filter(depth_data.depthIndex == depth_index).collect()[0].depthValue
        df_bronze = df_raw.withColumn("depth_meters", lit(depth_m)).withColumn("fetch_timestamp_utc", lit(fetch_time.strftime("%Y-%m-%d %H:%M:%S")))

        save_df_as_delta(df_bronze, bronze_df_file_name, "append")




# COMMAND ----------


latest_path = f"{get_adls_folder_path()}/bronze/hav_temperature_projection_latest"
dbutils.fs.rm(latest_path, recurse=True) # delete oldest latest before copy

# in order to have an updated latest, we overwrite the latest with the newly fetched dataframe. 
dbutils.fs.cp(f"{get_adls_folder_path()}/{bronze_df_file_name}", latest_path, recurse=True)

