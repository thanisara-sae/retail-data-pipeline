# Retail Data Pipeline (ETL & Analytics)

โปรเจกต์ระบบจัดเก็บ ทำความสะอาด และวิเคราะห์ข้อมูลการขายปลีก (Retail Transactions) ด้วยกระบวนการ ETL (Extract, Transform, Load) พร้อมระบบตรวจสอบคุณภาพข้อมูลและแดชบอร์ดสรุปผลการวิเคราะห์

---

## Overview

โปรเจกต์นี้จัดทำขึ้นเพื่อสาธิตการทำงานของ Data Pipeline แบบครบวงจร โดยมีขั้นตอนหลัก ดังนี้:

1. **Extract & Clean Data:** ดึงข้อมูลการขาย ทำความสะอาดข้อมูล จัดการค่าที่สูญหาย และทำการตรวจสอบคุณภาพข้อมูล (Data Quality Checks)
2. **Load to Database:** แปลงและนำข้อมูลที่ผ่านการทำความสะอาดแล้ว เข้าสู่ฐานข้อมูลเชิงสัมพันธ์ **SQLite**
3. **Analyze & Visualize:** ประมวลผลวิเคราะห์ข้อมูลด้วย **SQL** และสร้าง **Dashboard** แสดงตัวชี้วัดสำคัญทางการค้า

---

## ข้อมูลที่ใช้ในโปรเจกต์ (Dataset)

* **แหล่งที่มา:** [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail) จาก UCI Machine Learning Repository
* **หมายเหตุเรื่องไฟล์ข้อมูล:** เนื่องจากไฟล์ข้อมูลต้นฉบับ (`online_retail.xlsx`), ไฟล์ข้อมูลที่ทำความสะอาดแล้ว (`clean_retail.csv`) และไฟล์ฐานข้อมูล (`retail.db`) มีขนาดใหญ่ จึงไม่ได้ทำการ Push ขึ้นบน Repository นี้ตามแนวทางการจัดการ Git

---

## ขั้นตอนการรันสคริปต์ (Execution Steps)

กรุณารันสคริปต์ตามลำดับขั้นตอนต่อไปนี้:

### 1. Extract & Clean Data
ดึงข้อมูล ทำความสะอาด จัดการข้อมูลที่ไม่สมบูรณ์ และส่งออก data_quality_report.csv

```bash
python 01_extract_clean.py
```


### 2. Load to Database
แปลงข้อมูล นำเข้าฐานข้อมูล SQLite และจัดเตรียมตารางสำหรับสอบถามข้อมูล

```bash
python 02_load_sqlite.py
```

### 3. Analyze & Visualize
ประมวลผลวิเคราะห์ข้อมูลด้วยคำสั่ง SQL และสร้างภาพสรุปผลบนแดชบอร์ด

```bash
python 03_dashboard.py
```
