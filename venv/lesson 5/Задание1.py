#  Найдите всех пользователей из региона North, возраст которых младше 30, и 
# определите общее количество заказов, сделанных ими.
# region = North, age

import pandas as pd
users = pd.read_csv('users_new.csv', sep = ',', encoding = 'utf-8')
orders = pd.read_csv('orders_new.csv', sep = ',', encoding = 'utf-8')

merged = users.merge(orders, on='user_id', how='inner')
filtered = merged[(merged['age'] < 30) & (merged['region'] == 'North')]
grouped = filtered.groupby(['user_id', 'name', 'age', 'region'])['order_id'].count().reset_index(name = 'order_count')

print(grouped)

