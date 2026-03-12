import sqlite3
import pandas as pd
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
ware_path = os.path.join(os.path.join(base_dir,'..','warehouse'))
processed_path = os.path.join(os.path.join(base_dir,'..','data/processed'))
conn = sqlite3.connect(f'{ware_path}/retail.db')
query = '''
SELECT
store_name,
SUM(total_revenue)as total_revenue
FROM sales_facts
GROUP BY store_name
ORDER BY total_revenue DESC
'''
query2 = """SELECT 
    category,SUM(total_revenue) as total_revenue
FROM sales_facts
GROUP BY category
ORDER BY total_revenue DESC"""

df = pd.read_sql_query(query,conn)
df2 = pd.read_sql_query(query2,conn)
df.to_csv(f'{processed_path}/sales_by_store.csv',index=False)
df2.to_csv(f'{processed_path}/sales_by_category.csv',index=False)