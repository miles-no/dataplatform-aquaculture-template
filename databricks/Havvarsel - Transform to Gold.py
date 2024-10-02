# Databricks notebook source
from helpers.adls_utils import read_df_as_delta
df_silver = read_df_as_delta("/silver/hav_temperature_projection_latest")
display(df_silver)

# COMMAND ----------

from helpers.adls_utils import save_df_as_csv
save_df_as_csv(df_silver, "/gold/hav_temperature_projection_latest")

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

