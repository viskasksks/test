# Выгрузите номера заказов с суммой от 10 000 до 15 000 рублей, сделанных в 2023 году.

import pandas as pd
ord = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter = ord[((ord['total'] > 10000) & (ord['total'] < 15000))]
filter = filter[((filter['order_date'] >= '2023-01-01') & (filter['order_date'] < '2023-12-31'))]
print(filter['order_id'])