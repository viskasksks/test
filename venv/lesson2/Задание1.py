# Выгрузите номера всех заказов из файла orders, у которых стоимость заказа находится в 
# диапазоне от 30 тыс. до 40 тыс. включительно и при этом заказы выполнены начиная с 1 
# января 2023 года. 

import pandas as pd
ord = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_ord = ord[((ord['total'] >=30000) & (ord['total'] <=40000))]
filter_ord = filter_ord[((filter_ord['order_date'] >= '2023-01-01'))]
print(filter_ord['order_id'])