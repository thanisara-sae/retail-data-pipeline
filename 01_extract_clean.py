import pandas as pd

# 1) Extract
df = pd.read_excel("online_retail.xlsx")
print(df.shape)
print(df.dtypes)
print(df.head())

# 2) Data quality checks (นับปัญหาก่อนแก้)
issues = {
    "missing_customer_id": df["CustomerID"].isna().sum(),
    "missing_description": df["Description"].isna().sum(),
    "duplicate_rows": df.duplicated().sum(),
    "negative_or_zero_quantity": (df["Quantity"] <= 0).sum(),
    "zero_or_negative_price": (df["UnitPrice"] <= 0).sum(),
    "cancelled_invoices": df["InvoiceNo"].astype(str).str.startswith("C").sum(),
}
report = pd.Series(issues, name="rows").to_frame()
report["pct_of_total"] = (report["rows"] / len(df) * 100).round(2)
report.to_csv("data_quality_report.csv")
print(report)

# 3) Clean
clean = df.drop_duplicates().copy()
clean = clean[clean["UnitPrice"] > 0]
clean = clean.dropna(subset=["Description"])
clean["InvoiceNo"] = clean["InvoiceNo"].astype(str)
clean["is_cancelled"] = clean["InvoiceNo"].str.startswith("C").astype(int)
clean["revenue"] = clean["Quantity"] * clean["UnitPrice"]

print("rows before:", len(df), "| rows after:", len(clean))
clean.to_csv("clean_retail.csv", index=False)