
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark
spark = SparkSession.builder \
    .appName("RetailSilverTransformation") \
    .getOrCreate()

# Azure Data Lake Storage paths
raw_path = "abfss://raw@retailstorage14.dfs.core.windows.net/"
silver_path = "abfss://silver@retailstorage14.dfs.core.windows.net/"

# Read raw datasets
orders = spark.read.option("header", True).csv(raw_path + "orders.csv")
order_products = spark.read.option("header", True).csv(
    raw_path + "order_products__prior.csv"
)
products = spark.read.option("header", True).csv(raw_path + "products.csv")
footfall = spark.read.option("header", True).csv(raw_path + "footfall.csv")

# Remove duplicate records
orders = orders.dropDuplicates(["order_id"])
order_products = order_products.dropDuplicates(
    ["order_id", "product_id"]
)
products = products.dropDuplicates(["product_id"])
footfall = footfall.dropDuplicates()

# Remove records with missing important values
orders = orders.dropna(subset=["order_id", "user_id"])
order_products = order_products.dropna(
    subset=["order_id", "product_id"]
)
products = products.dropna(subset=["product_id"])
footfall = footfall.dropna(
    subset=["store_id", "date", "hour", "customer_count"]
)

# Convert numeric columns
orders = orders.withColumn(
    "order_id", col("order_id").cast("integer")
)

order_products = order_products \
    .withColumn("order_id", col("order_id").cast("integer")) \
    .withColumn("product_id", col("product_id").cast("integer"))

products = products.withColumn(
    "product_id", col("product_id").cast("integer")
)

footfall = footfall \
    .withColumn("store_id", col("store_id").cast("integer")) \
    .withColumn("hour", col("hour").cast("integer")) \
    .withColumn("customer_count", col("customer_count").cast("integer"))

# Save cleaned datasets in Silver layer
orders.write.mode("overwrite").parquet(silver_path + "orders/")
order_products.write.mode("overwrite").parquet(
    silver_path + "order_products/"
)
products.write.mode("overwrite").parquet(silver_path + "products/")
footfall.write.mode("overwrite").parquet(silver_path + "footfall/")

print("Silver layer transformation completed!")
