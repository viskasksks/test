# Посчитайте, сколько раз каждый продукт заказывался. Используйте 
# value_counts.
import pandas as pd

orders = pd.read_csv('orders_new.csv', sep = ',', encoding = 'utf-8')
order_count = orders['product'].value_counts().reset_index(name='order_count')
print(order_count)