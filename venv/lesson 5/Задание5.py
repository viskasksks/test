# Найдите пользователей, сделавших более 1 заказа, и выведите их имена и 
# количество заказов. name, order_id.count
import pandas as pd
users = pd.read_csv('users_new.csv', sep = ',', encoding = 'utf-8')
orders = pd.read_csv('orders_new.csv', sep = ',', encoding = 'utf-8')

merged = users.merge(orders, on='user_id', how='inner')
grouped = merged.groupby('name')['order_id'].count().reset_index(name='order_count')
filtered = grouped[grouped['order_count']>1]
print(filtered)
