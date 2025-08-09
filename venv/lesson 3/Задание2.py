# Выполните	фильтрацию	с	помощью	.query().	
# Отберите	все	записи	продаж	пользователеи,	прошедших	регистрацию	начиная	
# с	2022	года	и	совершивших	заказы	в	2023	году	на	сумму	более	30000	руб.	Оставьте	
# поля	с	ФИО	и	total.	Подсчитаите	количество	таких	продаж.

import pandas as pd
contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_1 = contacts.merge(customers, on='customer_id', how='left')
merged_1 = merged_1.merge(orders, on='customer_id', how='left')

merged_1['order_date'] = pd.to_datetime(merged_1['order_date'], errors='coerce')
merged_1['registration_date'] = pd.to_datetime(merged_1['registration_date'], errors='coerce')

merged_1['reg_year'] = merged_1['registration_date'].dt.year


merged_1['order_year'] = merged_1['order_date'].dt.year


filtered_1 = merged_1.query('reg_year >= 2022 and order_year == 2023 and total > 30000')[['first_name', 'last_name', 'total']]
print(filtered_1)
print('Количество продаж:', len(filtered_1))