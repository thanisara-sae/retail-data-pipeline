-- Q1: ยอดขายรายเดือน (ไม่รวมใบยกเลิก)
SELECT strftime('%Y-%m', o.InvoiceDate) AS month,
       ROUND(SUM(oi.Quantity * oi.UnitPrice), 2) AS revenue
FROM orders o
JOIN order_items oi ON o.InvoiceNo = oi.InvoiceNo
WHERE o.is_cancelled = 0
GROUP BY month
ORDER BY month;

-- Q2: Top 10 สินค้าตามยอดขาย
SELECT p.StockCode, p.Description,
       ROUND(SUM(oi.Quantity * oi.UnitPrice), 2) AS revenue
FROM order_items oi
JOIN orders o ON oi.InvoiceNo = o.InvoiceNo
JOIN products p ON oi.StockCode = p.StockCode
WHERE o.is_cancelled = 0
GROUP BY p.StockCode, p.Description
ORDER BY revenue DESC
LIMIT 10;

-- Q3: ยอดขายแยกตามประเทศ
SELECT c.Country,
       ROUND(SUM(oi.Quantity * oi.UnitPrice), 2) AS revenue
FROM order_items oi
JOIN orders o ON oi.InvoiceNo = o.InvoiceNo
JOIN customers c ON o.CustomerID = c.CustomerID
WHERE o.is_cancelled = 0
GROUP BY c.Country
ORDER BY revenue DESC;

-- Q4: สินค้าขายช้า (จำนวนขายรวมน้อย)
SELECT p.StockCode, p.Description, SUM(oi.Quantity) AS total_qty
FROM order_items oi
JOIN orders o ON oi.InvoiceNo = o.InvoiceNo
JOIN products p ON oi.StockCode = p.StockCode
WHERE o.is_cancelled = 0
GROUP BY p.StockCode, p.Description
HAVING total_qty > 0
ORDER BY total_qty ASC
LIMIT 20;

-- Q5: อัตราการยกเลิกรายเดือน
SELECT strftime('%Y-%m', InvoiceDate) AS month,
       COUNT(*) AS total_invoices,
       SUM(is_cancelled) AS cancelled,
       ROUND(100.0 * SUM(is_cancelled) / COUNT(*), 2) AS cancel_rate_pct
FROM orders
GROUP BY month
ORDER BY month;

-- Q6: รายการที่จำนวนผิดปกติ (อาจเป็น bulk order หรือข้อมูลผิด)
SELECT InvoiceNo, StockCode, Quantity, UnitPrice
FROM order_items
WHERE Quantity > 1000
ORDER BY Quantity DESC;