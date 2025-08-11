# Постройте сводную таблицу, где по строкам — region, по столбцам — product, а 
# значения — общая сумма заказов (цена × количество).

import pandas as pd
users = pd.read_csv('users_new.csv', sep = ',', encoding = 'utf-8')
orders = pd.read_csv('orders_new.csv', sep = ',', encoding = 'utf-8')
merged = users.merge(orders, on='user_id', how='inner')
merged['total'] = merged['price']*merged['quantity']
data_pivot = merged.pivot_table(index='region', columns='product', values='total', aggfunc='sum')
print(data_pivot)