
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("RetailStoreFootfallSalesAnalysis") \
    .getOrCreate()

# Azure Data Lake Storage Gen2 path
base_path = "abfss://raw@retailstorage14.dfs.core.windows.net/"

# Read raw datasets
orders = spark.read.csv(
    base_path + "orders.csv",
    header=True,
    inferSchema=True
)

order_products = spark.read.csv(
    base_path + "order_products__prior.csv",
    header=True,
    inferSchema=True
)

products = spark.read.csv(
    base_path + "products.csv",
    header=True,
    inferSchema=True
)

aisles = spark.read.csv(
    base_path + "aisles.csv",
    header=True,
    inferSchema=True
)

departments = spark.read.csv(
    base_path + "departments.csv",
    header=True,
    inferSchema=True
)

footfall = spark.read.csv(
    base_path + "footfall.csv",
    header=True,
    inferSchema=True
)

# Display dataset information
datasets = {
    "Orders": orders,
    "Order Products": order_products,
    "Products": products,
    "Aisles": aisles,
    "Departments": departments,
    "Footfall": footfall
}

for name, df in datasets.items():
    print(f"\nDataset: {name}")
    print(f"Total Records: {df.count()}")
    df.printSchema()

print("\nRaw data processing completed!")
