# Найдите среднюю сумму заказа по каждому городу.
import pandas as pd 
gr = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')
grouped = gr.groupby('city')['total'].mean().reset_index(name='avg_total')
print(grouped)