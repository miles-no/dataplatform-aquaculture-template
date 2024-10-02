from databricks.sdk.runtime import *
import pyspark.dbutils
from pyspark.sql import SparkSession

STORAGE_ACCOUNT = "devaquaplatformst01"
spark = SparkSession.builder.getOrCreate()

def connect_to_adls(storage_account = STORAGE_ACCOUNT): 
    spark.conf.set(
        f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
        dbutils.secrets.get(scope="terraform-created-scope", key="scope-storage-account-key"))

def get_adls_folder_path(container = "datalake", storage_account = STORAGE_ACCOUNT): 
    return (f"abfss://{container}@{storage_account}.dfs.core.windows.net/havvarsel/")

def save_df_as_delta(df, table_name, mode="overwrite", folder_path=get_adls_folder_path()): 
    connect_to_adls()
    df.write.format("delta").mode(mode).save(f"{folder_path}/{table_name}")


def save_df_as_csv(df, table_name, mode="overwrite", folder_path=get_adls_folder_path()): 
    connect_to_adls()
    df.coalesce(1).write.format("csv").mode(mode).option("header", "true").save(f"{folder_path}/{table_name}")

def read_df_as_csv(file_name, folder_path=get_adls_folder_path()): 
    connect_to_adls()
    df = spark.read.format("csv").load(f"{folder_path}/{file_name}")
    return df

def read_df_as_delta(file_name, folder_path=get_adls_folder_path()): 
    connect_to_adls()
    df = spark.read.format("delta").load(f"{folder_path}/{file_name}")
    return df