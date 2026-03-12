import pandas as pd
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
raw_path = os.path.join(os.path.join(base_dir,'..','data/raw'))
processed_path = os.path.join(os.path.join(base_dir,'..','data/processed'))

df = pd.read_csv(f'{raw_path}/sales_data.csv')
df['total_revenue'] = (df['unit_price'] * df['quantity']).round(2)

df.to_csv(f'{processed_path}/sales_clean.csv',index=False)