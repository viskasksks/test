# Выведите топ-3 города с самой высокой средней стоимостью одного заказа (total).
import pandas as pd
gr = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')
grouped = gr.groupby('city')['total'].mean().reset_index(name='total_avg')
grouped_1 = grouped.sort_values(by='total_avg', ascending=False)
print(grouped_1.head(3))