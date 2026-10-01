import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. ตั้งค่า Style และ Font 
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

conn = sqlite3.connect("retail.db")

# 2. ดึงข้อมูล
monthly = pd.read_sql("""
SELECT strftime('%Y-%m', o.InvoiceDate) AS month,
       SUM(oi.Quantity * oi.UnitPrice) AS revenue
FROM orders o JOIN order_items oi ON o.InvoiceNo = oi.InvoiceNo
WHERE o.is_cancelled = 0 GROUP BY month ORDER BY month
""", conn)

top = pd.read_sql("""
SELECT p.Description, SUM(oi.Quantity * oi.UnitPrice) AS revenue
FROM order_items oi
JOIN orders o ON oi.InvoiceNo = o.InvoiceNo
JOIN products p ON oi.StockCode = p.StockCode
WHERE o.is_cancelled = 0
GROUP BY p.StockCode, p.Description ORDER BY revenue DESC LIMIT 10
""", conn)

# 3. วาดกราฟด้วยโทนสีและ Layout 
fig, axes = plt.subplots(2, 1, figsize=(11, 10))

# --- กราฟที่ 1: Monthly Revenue 
axes[0].plot(
    monthly["month"], 
    monthly["revenue"] / 1000, # หาร 1,000 เพื่อแสดงผลเป็น $k ให้ดูง่าย
    color="#1f77b4", 
    marker="o", 
    linewidth=2.5, 
    markersize=6
)
axes[0].set_title("Monthly Revenue ($k)", fontsize=14, fontweight='bold', pad=12, color='#333333')
axes[0].tick_params(axis="x", rotation=45, labelsize=10)
axes[0].tick_params(axis="y", labelsize=10)
axes[0].grid(True, linestyle='--', alpha=0.6)

# --- กราฟที่ 2: Top 10 Products 
bars = axes[1].barh(
    top["Description"], 
    top["revenue"] / 1000, 
    color="#2ca02c", 
    height=0.65
)
axes[1].set_title("Top 10 Products by Revenue ($k)", fontsize=14, fontweight='bold', pad=12, color='#333333')
axes[1].invert_yaxis()  # เรียงอันดับจากมากไปน้อย
axes[1].tick_params(axis="x", labelsize=10)
axes[1].tick_params(axis="y", labelsize=9)
axes[1].grid(True, linestyle='--', alpha=0.6)

# ใส่ตัวเลขแสดงมูลค่่าตรงกราฟ
for bar in bars:
    width = bar.get_width()
    axes[1].text(
        width + 1, 
        bar.get_y() + bar.get_height()/2, 
        f'${width:,.1f}k', 
        va='center', 
        fontsize=8.5, 
        color='#444444'
    )

plt.tight_layout(pad=3.0)
plt.savefig("dashboard.png", dpi=300) # ปรับความละเอียดภาพเป็น 300 DPI
conn.close()
print("Dashboard updated successfully!")