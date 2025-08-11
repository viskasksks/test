# Вывести все заказы на продукт "C" с суммой больше 250. Использовать query и 
# арифметику.

import pandas as pd

orders = pd.read_csv('orders_new.csv', sep = ',', encoding = 'utf-8')
orders['total'] = orders['price']*orders['quantity']
filtered = orders.query('product == "C" and total >250')
print(filtered)