import pandas as pd


# data_1 = pd.read_csv('customers.csv', sep=',',encoding='utf-8')

# Примените к одному из файлов info(), shape(), tail(), sample(), len()

# data_1.info()


# print(data_1.shape)

# print(data_1.tail())

# print(data_1.sample())

# print(len(data_1))

# Объедините таблицы по customer_id
# Объедините таблицы customers и orders, чтобы получить только тех клиентов, которые делали заказы (используйте how='inner').


# orders = pd.read_csv('orders.csv', sep=',',encoding='utf-8')
# shop = pd.read_csv('shop.csv', sep=',',encoding='utf-8')

# merged = customers.merge(orders, on='customer_id', how='inner')
# merged_2 = merged.merge(shop, on='customer_id', how='inner')

# no_orders = merged

# print(customers.head())

# print(customers[['product_name', 'price'].head()])

# Выгрузите номера всех заказов (order_id) из файла orders, у которых стоимость заказа
# находится в диапазоне от 30 тыс. до 40 тыс. (total) включительно и при этом 
# заказы выполнены начиная с 1 января 2023 года. (order_date)
# orders = pd.read_csv('orders.csv', sep=',',encoding='utf-8')
# filter_orders = orders[((orders['total']>=30000) & (orders['total']<=40000))]
# filter_orders = filter_orders[filter_orders['order_date'] >= '2023-01-01']
# print(filter_orders['order_id'])


# Известно, что пользователи из России имеют id с 68 по 88. Отберите заказы пользователей из России за 2022 год. Из полученной 
# выборки отобразите только записи с 5 по 10 включительно и столбцы с номером заказа и суммой заказа.

# orders = pd.read_csv('orders.csv', sep=',',encoding='utf-8')
# filter_df = orders[(orders['customer_id'] >= 68) & (orders['customer_id']<=88)]
# # print(filter)
# filter_df = filter_df[(filter_df['order_date'] >= '2022-01-01')  & (filter_df['order_date'] <= '2022-12-31')]
# print(filter_df)
# print(filter_df[4:10], ['customer_id', 'total'])


# Выведите заказы клиентов с ID от 10 до 20 включительно, у которых сумма заказа больше 8000.
# Покажите order_id, customer_id и сумму.

prod = pd.read_csv('products.csv', sep=',', encoding='utf-8')
filter_df = 