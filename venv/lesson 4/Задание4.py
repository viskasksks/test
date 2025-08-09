# Сгруппируйте данные по месяцу заказа и найдите общую выручку в каждом месяце. 
import pandas as pd
gr = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')
gr['order_date'] = pd.to_datetime(gr['order_date'], errors= 'coerce')
gr['order_month'] = gr['order_date'].dt.to_period('M')
grouped = gr.groupby('order_month')['total'].sum().reset_index(name='total_income')
print(grouped)