# Методом	value_counts()	подсчитаите	сколько	заказов	в	период	2022
# 2023	годов	было	осуществлено	пользователями	мужского	пола	и	сколько	
# пользователями	женского	пола.

import pandas as pd
contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_1 = contacts.merge(customers, on='customer_id', how='left')
merged_1 = merged_1.merge(orders, on='customer_id', how='left')

merged_1['order_date'] = pd.to_datetime(merged_1['order_date'], errors='coerce')

merged_1['year'] = merged_1['order_date'].dt.year

filtered_1 = merged_1.query('year == 2022 or year == 2023')
gen_num = filtered_1['gender'].value_counts()
print(gen_num)