import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sales.csv")
df = pd.read_csv(os.path.join(script_dir, "sales.csv"))

print("Raw Data")
print(df)
print(df.shape)
print("\n")
print(df.head(5))
print(df.info())
print(df.describe())
print(df.isnull().sum())

df = df.dropna(subset = ["customer_name"])
df["quantity"] = df["quantity"].fillna(1)
df["price"] = df["price"].fillna(df.groupby("product")["price"].transform("mean"))
df = df.dropna(subset = ["date"])
print("\n")
print(df)
print("\nNumber of Missing Value in each column:")
print(df.isnull().sum())

print("\n")
print("Duplicate rows:")
print(df.duplicated(subset=["customer_name", "product", "quantity", "price", "date", "region"]).sum())

df = df.drop_duplicates(subset = ["customer_name", "product", "quantity", "price", "date", "region"])
print(f"\nRows after removing duplicates: {len(df)}")

df["total"] = df["quantity"] * df["price"]
print("\nNew column added:")
print(df)

print("\nTotal Revenue:")
Total_revenue = df["total"].sum()
print(Total_revenue)
print("\nBest selling product:")
print(df["product"].value_counts().idxmax())
print("\nTop Region by Total Revenue")
top_region = df.groupby("region")["total"].sum().idxmax()
print(top_region)

def save_clean_csv(df):
    try:
        df.to_csv((os.path.join(script_dir, "sales_cleaned.csv")), index = False)
        print("\nCleaned Data Saved successfully")
    except Exception as e:
        print(f"\nError in Saving the Cleaned Data{e}")

save_clean_csv(df)



print("Done!")
