import pandas as pd
import random
import os
from faker import Faker

fake = Faker()
products = {
    'Electronics': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Shoes'],
    'Food': ['Coffee', 'Tea', 'Snacks', 'Water'],
    'Home': ['Lamp', 'Chair', 'Desk', 'Pillow'],
    'Sports': ['Yoga Mat', 'Dumbbells', 'Bike', 'Gloves']
}
def get_category():
    return random.choice(list(products.keys()))
categories = [get_category() for _  in range(2000)]
def get_product_name(category):
    return random.choice(products[category])

stores = {
    'ST-01': 'New York',
    'ST-02': 'Los Angeles',
    'ST-03': 'Chicago',
    'ST-04': 'Houston',
    'ST-05': 'Miami',
    'ST-06': 'Dallas',
    'ST-07': 'Washington'
}
def get_store_id():
    return random.choice(list(stores.keys()))
stores_id = [get_store_id() for _ in range(2000)]

def get_store_name(store_id):
    return stores[store_id]
stock_qty = [random.randint(0,999) for _ in range(2000)]
datos = {
    'product_id': [fake.bothify('SKU-##') for _ in range(2000)],
    'product_name': [get_product_name(categories[i]) for i in range(2000)],
    'category':[categories[i] for i in range(2000)],
    'unit_price':[round(random.uniform(15.50, 125.99),2) for _ in range(2000)],
    'customer_id': [fake.bothify('CST-###') for _ in range(2000)],
    'customer_name': [fake.company() for _ in range(2000)],
    'order_id':[fake.bothify('OR-####') for _ in range(2000)],
    'quantity': [random.randint(0,stock_qty[i])for i in range(2000)],
    'stock_qty':stock_qty,
    'order_date':[fake.date_this_year() for _ in range(2000)],
    'store_id': [stores_id[i] for i in range(2000)],
    'store_name': [get_store_name(stores_id[i]) for i in range(2000)]

}
df = pd.DataFrame(datos)
current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir,'..','data/raw')
normalized_path = os.path.normpath(config_dir)
df.to_csv(f'{normalized_path}/sales_data.csv',index=False)