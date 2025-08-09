# Определите, какой товар продавался в наибольшем количестве (по сумме quantity).
import pandas as pd
gr = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')
grouped = gr.groupby('product')['quantity'].sum().reset_index(name='total_quantity')
top = grouped.loc[grouped['total_quantity'].idxmax()]
print(top)