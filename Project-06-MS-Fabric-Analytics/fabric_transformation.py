# This script demonstrates the "Silver to Gold" transformation within Fabric
from pyspark.sql import functions as F

# 1. Load Raw Sales Data from the Lakehouse
# In Fabric, files are stored in 'Files/Raw'
df_raw = spark.read.format("csv").option("header", "true").load("Files/Raw/sales_data.csv")

# 2. Data Cleaning (Silver Layer)
# Standardize currency, handle missing values, and cast types
df_cleaned = df_raw.withColumn("Amount", F.col("Amount").cast("double")) \
                   .withColumn("Date", F.to_date(F.col("OrderDate"), "MM/dd/yyyy")) \
                   .filter(F.col("Amount") > 0) \
                   .fillna({"CustomerID": "Unknown"})

# 3. Aggregate for Business Insights (Gold Layer)
# Summarizing sales by region for executive reporting
df_gold = df_cleaned.groupBy("Region") \
                    .agg(F.sum("Amount").alias("TotalSales"), 
                         F.count("OrderID").alias("OrderCount"))

# 4. Save as a Delta Table
# This makes it instantly available for PowerBI via 'Direct Lake'
df_gold.write.format("delta").mode("overwrite").saveAsTable("Gold_Regional_Sales")

print("✅ Data Transformation Complete: Gold Table Created in OneLake.")
