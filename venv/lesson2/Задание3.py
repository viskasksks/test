# Отобразите продукты, которые стоят меньше 500 руб. и имеют объём 5.0 мл. 
# Выведите название и цену

import pandas as pd
prod = pd.read_csv('products.csv', sep=',', encoding='utf-8')
filter_prod = prod[((prod['price'] <500) & (prod['volume_ml']==5.0))]
print(filter_prod[['product_name', 'price']])