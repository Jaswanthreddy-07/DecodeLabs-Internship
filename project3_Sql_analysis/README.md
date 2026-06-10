# SQL Data Analysis

## Description
This project performs SQL-based analysis on an e-commerce dataset. The dataset is imported into SQLite and analyzed using SQL queries to extract business insights.

## Dataset Columns
OrderID, Date, CustomerID, Product, Quantity, UnitPrice, ShippingAddress, PaymentMethod, OrderStatus, TrackingNumber, ItemsInCart, CouponCode, ReferralSource, TotalPrice

## SQL Concepts Used
- SELECT
- WHERE
- ORDER BY
- GROUP BY
- COUNT
- SUM
- AVG
- MIN
- MAX

## How to Run

1. Install requirements
pip install -r requirements.txt

2. Create database
python scripts/create_database.py

3. Run analysis
python scripts/run_queries.py

## Project Structure
data/
scripts/
sql/
reports/
screenshots/

## Outcome
Generated insights from customer orders, products, payment methods, referral sources, and revenue.
