import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/Global_Superstore.csv", encoding="latin1")

print(df.head())
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with missing Customer ID
df = df.dropna(subset=["Customer ID"])

print("\nMissing values removed successfully.")

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicates removed.")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

print(df.dtypes)

reference_date = df["Order Date"].max() + pd.Timedelta(days=1)

print("Reference Date:", reference_date)

rfm = df.groupby("Customer ID").agg({
    "Order Date": lambda x: (reference_date - x.max()).days,
    "Order ID": "count",
    "Sales": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

print(rfm.head())
rfm.to_csv("data/processed/rfm_analysis.csv")

print("RFM Analysis saved successfully!")