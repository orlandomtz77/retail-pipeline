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
order_date,
store_id,
store_name,
revenue,
(revenue / nullif(quantity,0)) as revenue_per_unit,
case
when (revenue / nullif(quantity,0))  > 500 then 1
else  0
end as is_high_value
from {{ref('stg_sales')}}