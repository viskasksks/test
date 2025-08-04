# Найдите заказы клиентов, родившихся в 1990 году. Выведите order_id и customer_id. 
# 
# 
# 
# (ЗАМЕТКА: в файле customers.csv нет order_id, поэтому вывела данные из файла shop.csv)

import pandas as pd
shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
filter = shop[((shop['birth_date'] >= '1990-01-01') & (shop['birth_date'] <= '1990-12-31'))]
print(filter[['order_id', 'customer_id']])