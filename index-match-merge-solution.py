import pandas as pd

excel_file = pd.ExcelFile("Index Match Python Problem.xlsx")
orders = pd.read_excel(excel_file, sheet_name="Orders")
order_details = pd.read_excel(excel_file, sheet_name="OrderDetails")
products = pd.read_excel(excel_file, sheet_name="Products")

df = pd.merge(
    left=order_details,
    right=products,
    left_on="ProductID",
    right_on="ID",
    how="left"
)

df["TotalPrice"] = df["ListPrice"] * df["Quantity"]
df.to_csv("outputs/merge-output.csv", index=False)