import pandas as pd

def load_data():
    excel_file = pd.ExcelFile("Index Match Python Problem.xlsx")
    orders = pd.read_excel(excel_file, sheet_name="Orders")
    order_details = pd.read_excel(excel_file, sheet_name="OrderDetails")
    products = pd.read_excel(excel_file, sheet_name="Products")

    return orders, order_details, products


def get_order_information(id, customer_name):
    orders, order_details, products = load_data()

    order = orders.loc[
        (orders['OrderID'] == id) & 
        (orders['Customer'] == customer_name)
    ]

    order_info = pd.merge(
        left=order,
        right=order_details,
        on="OrderID",
        how="inner"
    )

    order_info = pd.merge(
        left=order_info,
        right=products,
        left_on="ProductID",
        right_on="ID"
    )

    order_info["TotalPrice"] = order_info["ListPrice"] * order_info["Quantity"]
    order_info.drop(columns=["ID", "ListPrice"], inplace=True)
    products = order_info.groupby(["OrderID"])["ProductName"].agg(list)

    order_info = order_info \
        .groupby(["OrderID", "Customer"])['ProductName', 'TotalPrice'].agg(sum) \
        .reset_index()

    order_info["Products"] = products.values
    
    print(order_info)

    order_info.to_csv(f"outputs/order-information-for-id-{id}.csv", index=False)


if __name__ == "__main__":
    get_order_information(id=4, customer_name="Mike")