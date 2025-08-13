# Найдите заказы клиентов, родившихся в 1990 году. Выведите order_id и customer_id. 


import pandas as pd
cust = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
ord = pd.read_csv('orders.csv', sep=',', encoding='utf-8')


merged = cust.merge(ord, on='customer_id', how='inner')
filter = merged[((merged['birth_date'] >= '1990-01-01') & (merged['birth_date'] <= '1990-12-31'))]
print(filter[['order_id', 'customer_id']])