from databricks.sdk.runtime import *
import pyspark.dbutils
from pyspark.sql import SparkSession

STORAGE_ACCOUNT = "devaquaplatformst01"
spark = SparkSession.builder.getOrCreate()

def connect_to_adls(storage_account = STORAGE_ACCOUNT): 
    spark.conf.set(
        f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
        dbutils.secrets.get(scope="terraform-created-scope", key="storage-account-key"))

def get_adls_file_path(container = "datalake", storage_account = STORAGE_ACCOUNT): 
    return (f"abfss://{container}@{storage_account}.dfs.core.windows.net/havvarsel/")


def save_df_as_delta(df, table_name, mode="overwrite", file_path=get_adls_file_path()): 
    connect_to_adls()
    df.write.format("delta").mode(mode).save(f"{file_path}/{table_name}")

def read_df_as_delta(file_name, file_path=get_adls_file_path()): 
    connect_to_adls()
    df = spark.read.format("delta").load(f"{file_path}/{file_name}")
    return df