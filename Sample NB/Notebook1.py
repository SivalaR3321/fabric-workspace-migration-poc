# Fabric notebook source
# METADATA ********************
# {"kernel_info": {"name": "synapse_pyspark"}}

# CELL ********************
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

rows = [
    (1, "notebook"),
    (2, "git"),
    (3, "poc"),
]

df = spark.createDataFrame(rows, ["id", "topic"])
display(df)
