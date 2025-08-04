# Найдите всех клиентов женского пола, которые родились до 1995 года. 
# Выведите их customer_id, имя, фамилию и год рождения.

import pandas as pd
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
customers['birth_date'] = pd.to_datetime(customers['birth_date'], errors='coerce')
filter_sh = customers[((customers['gender'] =='F') & (customers['birth_date'] <='1995-12-31'))]
print(filter_sh[['customer_id', 'first_name', 'last_name', 'birth_date']])
