
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, sum, round
)

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("RetailGoldAnalysis") \
    .getOrCreate()

# Azure Data Lake Storage paths
silver_path = "abfss://silver@retailstorage14.dfs.core.windows.net/"
gold_path = "abfss://gold@retailstorage14.dfs.core.windows.net/"

# Read Silver layer datasets
footfall = spark.read.parquet(silver_path + "footfall/")

# Read the prepared hourly sales dataset
# It must contain store_id, date, hour and total_sales.
sales = spark.read.parquet(silver_path + "sales/")

# Aggregate footfall by store, date and hour
footfall_agg = footfall.groupBy(
    "store_id", "date", "hour"
).agg(
    sum("customer_count").alias("total_footfall")
)

# Aggregate sales by store, date and hour
sales_agg = sales.groupBy(
    "store_id", "date", "hour"
).agg(
    sum("total_sales").alias("total_sales")
)

# Combine sales and footfall
store_performance = sales_agg.join(
    footfall_agg,
    on=["store_id", "date", "hour"],
    how="inner"
)

# Calculate conversion rate
store_performance = store_performance.withColumn(
    "conversion_rate",
    round(
        col("total_sales") /
        col("total_footfall") * 100,
        2
    )
)

# Save Gold layer data
store_performance.write \
    .mode("overwrite") \
    .format("parquet") \
    .save(gold_path + "store_performance/")

# Display final results
store_performance.show(10, truncate=False)

print("Gold layer analysis completed!")
