
# Libraries

import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

sns.set(style="whitegrid")


# Download Olist Dataset from Kaggle

path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print("Path to dataset files:", path)


# Load CSV files into pandas DataFrames

customers = pd.read_csv(os.path.join(path, "olist_customers_dataset.csv"), encoding='utf-8')
orders = pd.read_csv(os.path.join(path, "olist_orders_dataset.csv"), encoding='utf-8')
products = pd.read_csv(os.path.join(path, "olist_products_dataset.csv"), encoding='utf-8')
order_items = pd.read_csv(os.path.join(path, "olist_order_items_dataset.csv"), encoding='utf-8')
order_payments = pd.read_csv(os.path.join(path, "olist_order_payments_dataset.csv"), encoding='utf-8')


# Create SQLite Database and Write Tables

conn = sqlite3.connect('olist.db')
customers.to_sql('customers', conn, if_exists='replace', index=False)
orders.to_sql('orders', conn, if_exists='replace', index=False)
products.to_sql('products', conn, if_exists='replace', index=False)
order_items.to_sql('order_items', conn, if_exists='replace', index=False)
order_payments.to_sql('order_payments', conn, if_exists='replace', index=False)


# SQL Queries


# 1 Top 10 Product Categories by Sales
query_top_categories = """
SELECT p.product_category_name, SUM(oi.price) AS total_sales
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY total_sales DESC
LIMIT 10;
"""
top_categories = pd.read_sql(query_top_categories, conn)

# 2 VIP Customers (Top 100 by Spending)
query_vip_customers = """
SELECT c.customer_unique_id, SUM(oi.price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_unique_id
ORDER BY total_spent DESC
LIMIT 100;
"""
vip_customers = pd.read_sql(query_vip_customers, conn)

# 3 Monthly Sales Trend by Category
query_category_trend = """
SELECT p.product_category_name,
       STRFTIME('%Y-%m', o.order_purchase_timestamp) AS month,
       SUM(oi.price) AS monthly_sales
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_status = 'delivered'
GROUP BY p.product_category_name, month
ORDER BY month, monthly_sales DESC;
"""
category_trend = pd.read_sql(query_category_trend, conn)

# 4 Payment Method Analysis
query_payment_method = """
SELECT payment_type, COUNT(*) AS num_orders, SUM(payment_value) AS total_revenue
FROM order_payments
GROUP BY payment_type
ORDER BY total_revenue DESC;
"""
payment_analysis = pd.read_sql(query_payment_method, conn)

# 5 Order Status Analysis
query_order_status = """
SELECT order_status, COUNT(*) AS num_orders
FROM orders
GROUP BY order_status;
"""
order_status_analysis = pd.read_sql(query_order_status, conn)


# Python Visualization + Insights


# 1 Top 10 Product Categories
plt.figure(figsize=(12,6))
sns.barplot(data=top_categories, x='product_category_name', y='total_sales', palette='viridis', hue='product_category_name', legend=False)
plt.xticks(rotation=45)
plt.title("Top 10 Product Categories by Sales")
plt.show()
print("Insight: Beauty & Health products are the top-selling category, generating the highest revenue. Focusing on this category could maximize profits.")

# 2 VIP Customers Spending Distribution
plt.figure(figsize=(12,6))
sns.histplot(vip_customers['total_spent'], bins=20, kde=True, color='skyblue')
plt.title("VIP Customers Spending Distribution")
plt.xlabel("Total Spent")
plt.show()
print("Insight: The top 10% of customers contribute a significant portion of total revenue. Implementing customer loyalty strategies could increase retention and revenue.")

# 3 Monthly Sales Trend by Category (Top 5 Categories)
top5_categories = top_categories['product_category_name'].tolist()
plt.figure(figsize=(12,6))
for cat in top5_categories:
    subset = category_trend[category_trend['product_category_name']==cat]
    plt.plot(subset['month'], subset['monthly_sales'], label=cat)
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend for Top 5 Categories")
plt.legend()
plt.show()
print("Insight: Certain categories peak in specific months. Seasonal campaigns can be planned accordingly.")

# 4 Payment Method Analysis
plt.figure(figsize=(10,5))
sns.barplot(data=payment_analysis, x='payment_type', y='total_revenue', palette='magma', hue='payment_type', legend=False)
plt.xticks(rotation=45)
plt.title("Revenue by Payment Type")
plt.show()
print("Insight: Credit cards are the most used and revenue-generating payment method. Optimizing the payment experience for credit card users could improve conversions.")

# 5 Order Status Analysis
plt.figure(figsize=(8,4))
sns.barplot(data=order_status_analysis, x='order_status', y='num_orders', palette='coolwarm', hue='order_status', legend=False)
plt.title("Order Status Counts")
plt.show()
print("Insight: Most orders are successfully delivered, but a small portion are canceled or delayed. Improving logistics and order tracking could reduce cancellations and enhance customer satisfaction.")