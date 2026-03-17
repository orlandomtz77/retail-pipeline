select
category,
store_name,
sum(revenue) as total_revenue,
count(order_id) as total_orders,
sum(quantity) as total_quantity,
avg(revenue_per_unit) as avg_revenue_per_unit
from {{ref('fct_sales')}}
group by category,store_name
