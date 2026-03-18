# Brazilian E-Commerce Analysis – Olist Dataset

## Project Overview
This project provides a comprehensive end-to-end analysis of the Brazilian e-commerce dataset from Olist, which contains information on customers, orders, products, order items, and payment methods.  
We selected this dataset for its **multi-table structure and real-world complexity**, allowing a demonstration of both **SQL querying skills** and **Python data analysis & visualization** in a complete workflow.

## Project Objectives
The main goals of this project are:  
1. Identify the **top-selling product categories**.  
2. Discover the **highest spending customers**.  
3. Analyze **monthly sales trends by category** to understand seasonal patterns.  
4. Examine **payment method usage and revenue contribution**.  
5. Investigate **order statuses** to assess fulfillment efficiency.  

By combining SQL queries and Python visualizations, this project illustrates how **raw e-commerce data can be transformed into actionable business insights** from start to finish.

## Insights & Findings
- **Top Categories:** Beauty & Health products are the highest revenue-generating category, suggesting focus areas for marketing and inventory planning.  
- **VIP Customers:** The top 10% of customers contribute a significant portion of total revenue, highlighting the importance of customer loyalty.  
- **Monthly Trends:** Certain categories peak during specific months (e.g., Furniture & Decor in October), showing opportunities for seasonal campaigns.  
- **Payment Methods:** Credit cards dominate in both usage and revenue, suggesting prioritization for payment optimization.  
- **Order Statuses:** Most orders are successfully delivered, but some cancellations and delays exist, indicating potential areas for logistics improvement.

## Workflow
1. **Data Acquisition:** Download the dataset from Kaggle using the `kagglehub` Python library.  
2. **Data Loading:** Load CSV files into **SQLite** and **pandas DataFrames**.  
3. **SQL Analysis:** Execute aggregation queries and JOINs to summarize sales, customers, payments, and orders.  
4. **Python Analysis:** Visualize results using **Matplotlib** and **Seaborn**, highlighting trends, top categories, VIP customers, and order/payment patterns.  
5. **Insight Extraction:** Translate the visualizations into **actionable business insights**, demonstrating a full end-to-end analysis workflow.

## Requirements
- Python 3.x  
- pandas  
- matplotlib  
- seaborn  
- kagglehub  
- sqlite3
