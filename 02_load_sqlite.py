import sqlite3
import pandas as pd

clean = pd.read_csv("clean_retail.csv")

customers = (
    clean.dropna(subset=["CustomerID"])[["CustomerID", "Country"]]
    .drop_duplicates("CustomerID")
)
customers["CustomerID"] = customers["CustomerID"].astype(int)

products = clean[["StockCode", "Description"]].drop_duplicates("StockCode")

orders = clean[["InvoiceNo", "InvoiceDate", "CustomerID", "is_cancelled"]].drop_duplicates("InvoiceNo")
orders["CustomerID"] = orders["CustomerID"].astype("Int64")

order_items = clean[["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]]

conn = sqlite3.connect("retail.db")
customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
order_items.to_sql("order_items", conn, if_exists="replace", index=False)
conn.close()
print("done")