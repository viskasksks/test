# Используйте файл group_orders.csv. Посчитайте общее количество заказов в каждом 
# городе. 
import pandas as pd 
gr = pd.read_csv('group_orders.csv', sep = ',', encoding='utf-8')
grouped = gr.groupby('city')['order_id'].count().reset_index(name='order_num')
print(grouped)
