# Выведите заказы клиентов с ID от 10 до 20 включительно, у которых сумма заказа больше 
# 8000. 
# Покажите order_id, customer_id и сумму.

import pandas as pd
ord = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_ord = ord[((ord['customer_id'] >=10) & (ord['customer_id'] <=20))]
filter_ord = filter_ord[((filter_ord['total']>8000))]
print(filter_ord[['order_id', 'customer_id', 'total']])