# Известно, что пользователи из России имеют id с 68 по 88. Отберите заказы пользователей 
# из России за 2022 год. Из полученной выборки отобразите только записи с 5 по 10 
# включительно и столбцы с номером заказа и суммой заказа.

import pandas as pd
ord = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_ord = ord[((ord['customer_id']>=68) & (ord['customer_id']<=88))]
filter_ord = filter_ord[((filter_ord['order_date'] >= '2022-01-01') & (filter_ord['order_date'] <= '2022-12-31'))]
print(filter_ord[['order_id', 'total']].head(11).tail(6))