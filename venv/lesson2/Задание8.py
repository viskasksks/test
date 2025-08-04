# Найдите заказы за февраль 2023 года, где сумма заказа > 5000.

import pandas as pd
ord = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter = ord[((ord['total'] > 5000) & (ord['order_date'] > '2023-02-01') & (ord['order_date'] < '2023-02-28'))]
print(filter)