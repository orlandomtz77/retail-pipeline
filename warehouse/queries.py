import sqlite3
import pandas as pd
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(f'{base_dir}/retail.db')
query = """SELECT 
    category,SUM(total_revenue) as total_revenue
FROM sales_facts
GROUP BY category
ORDER BY total_revenue DESC"""
query2 = """SELECT 
    product_name,
    SUM(quantity) as quantity   
FROM sales_facts
GROUP BY product_name
ORDER BY quantity DESC
LIMIT 5
"""
query3 = '''
SELECT
store_name,
SUM(total_revenue)as total_revenue
FROM sales_facts
GROUP BY store_name
ORDER BY total_revenue DESC
'''
df = pd.read_sql_query(query,conn)
df2 = pd.read_sql_query(query2,conn)
df3 = pd.read_sql_query(query3,conn)
print(df)
print(df2)
print(df3)