import pandas as pd

# load dataset
df = pd.read_csv(
    "/home/friend/my_jupyter_project/MCA1/Aman sidar/PYTHON/PRACTICAL 1/sales_data.csv"
)

# create Total_Revenue column
df["Total_Revenue"] = df["Quantity"] * df["Price"]

# total revenue for each product
print("\nTotal Revenue by Product:")
print(df.groupby("Product")["Total_Revenue"].sum())

# total quantity sold for each category
print("\nTotal Quantity Sold by Category:")
print(df.groupby("Category")["Quantity"].sum())

# average price per category
print("\nAverage Price per Category:")
print(df.groupby("Category")["Price"].mean())

# product with maximum quantity sold
print("\nProduct with Maximum Quantity Sold:")
print(df.loc[df["Quantity"].idxmax()])

# monthly total revenue
print("\nMonthly Total Revenue:")
print(df.groupby("Month")["Total_Revenue"].sum())

# products where quantity > 40
print("\nProducts with Quantity > 40:")
print(df[df["Quantity"] > 40])

# sort by total revenue
print("\nSorted by Total Revenue (Descending):")
print(df.sort_values(by="Total_Revenue", ascending=False))
