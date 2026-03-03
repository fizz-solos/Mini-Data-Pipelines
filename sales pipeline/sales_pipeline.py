import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sales.csv")
df = pd.read_csv(os.path.join(script_dir, "sales.csv"))

# =============================================
# TASK 1: Load the CSV and inspect it
# =============================================
# Load sales.csv into a DataFrame called df
# Then print:
#   - the first 5 rows
#   - df.info() to see column types and missing values
#   - df.describe() to see basic stats
print("Raw Data")
print(df)
print(df.shape)
print("\n")
print(df.head(5))
print(df.info())
print(df.describe())





# =============================================
# TASK 2: Find missing values
# =============================================
# Print the number of missing values in each column
# Hint: use df.isnull().sum()
print(df.isnull().sum())


# =============================================
# TASK 3: Handle missing values
# =============================================
# - Drop rows where customer_name is missing (can't have an order without a customer)
# - Fill missing quantity with 1 (assume 1 item ordered)
# - Fill missing price with the average price of that product
#   Hint: use df.groupby("product")["price"].transform("mean")
# - Drop rows where date is missing
df = df.dropna(subset = ["customer_name"])
df["quantity"] = df["quantity"].fillna(1)
df["price"] = df["price"].fillna(df.groupby("product")["price"].transform("mean"))
df = df.dropna(subset = ["date"])
print("\n")
print(df)
print("\nNumber of Missing Value in each column:")
print(df.isnull().sum())


# =============================================
# TASK 4: Remove duplicates
# =============================================
# Print how many duplicate rows exist before removing them
# Then drop duplicates and print how many rows are left
print("\n")
print("Duplicate rows:")
print(df.duplicated(subset=["customer_name", "product", "quantity", "price", "date", "region"]).sum())

df = df.drop_duplicates(subset = ["customer_name", "product", "quantity", "price", "date", "region"])
print(f"\nRows after removing duplicates: {len(df)}")

# =============================================
# TASK 5: Add a derived column
# =============================================
# Add a new column called "total" = quantity * price
# This is the total revenue for each order
df["total"] = df["quantity"] * df["price"]
print("\nNew column added:")
print(df)


# =============================================
# TASK 6: Basic analysis
# =============================================
# Print:
#   - Total revenue (sum of "total" column)
#   - Best selling product (most rows after cleaning)
#   - Top region by total revenue
# Hint: use df.groupby("region")["total"].sum()
print("\nTotal Revenue:")
Total_revenue = df["total"].sum()
print(Total_revenue)
print("\nBest selling product:")
print(df["product"].value_counts().idxmax())
print("\nTop Region by Total Revenue")
top_region = df.groupby("region")["total"].sum().idxmax()
print(top_region)





# =============================================
# TASK 7: Save cleaned data
# =============================================
# Save the cleaned DataFrame to "sales_clean.csv" in the same folder
# Use index=False
def save_clean_csv(df):
    try:
        df.to_csv((os.path.join(script_dir, "sales_cleaned.csv")), index = False)
        print("\nCleaned Data Saved successfully")
    except Exception as e:
        print(f"\nError in Saving the Cleaned Data{e}")

save_clean_csv(df)



print("Done!")
