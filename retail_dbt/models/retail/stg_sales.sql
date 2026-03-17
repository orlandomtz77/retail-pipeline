select
product_id,
product_name,
category,
unit_price,
customer_id,
customer_name,
order_id,
quantity,
stock_qty,
CAST(order_date as DATE) as order_date,
store_id,
store_name,
total_revenue as revenue
from sales_facts

