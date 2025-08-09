import pandas as pd
# prod = pd.read_csv('products.csv', sep=',', encoding='utf-8')
# print(prod[4:10])

# Вывести заказы 2023 года, где сумма (total) превышает 8000
# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# shop['order_date'] = pd.to_datetime(shop['order_date'], errors='coerce')
# mask = shop.loc[(shop['order_date'].dt.year==2023) & (shop['total'] > 8000)]
# print(mask['order_id'].count())

# Вывести строки с 5-й по 14-ю включительно (то есть индексы 5–14) с помощь
#  .iloc[] для customer_id

# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# mask = shop.iloc[5:15]
# print(mask['customer_id'])



# Найти клиентов, которые не зарегистрировались в 2023 году.
# Столбцы: customer_id, registration_date.

# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# shop['registration_date'] = pd.to_datetime(shop['registration_date'], errors='coerce')
# mask = shop.loc[(shop['registration_date'].dt.year != 2023)]
# print(mask[['customer_id', 'registration_date']].count())



# Вывести товары с volume_ml == 5.0 из строк с индексами от 20 до 30.
# Столбцы: product_name, volume_ml. 
# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# mask = shop.loc[(shop['volume_ml'] ==5.0)]
# result = mask.iloc[21:31]
# print(result[['product_name', 'volume_ml']])

# QUERY
# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# filter_df = shop.query('country == "Russia" and category == "Absolute"')[['order_id']]
# print(filter_df.head())

# ЛИБО
# filter_df_1 = shop[(shop['country'] =='Russia') & (shop['category'] == 'Absolute')]['order_id']
# print(filter_df_1.head(1))

# # ЛИБО ЧЕРЕЗ loc 
# filter_df_2 = shop.loc[(shop['country'] == 'Russia')&(shop['category'] == 'Absolute'), ['order_id']]
# print(filter_df_2.head(1))

# ЧЕРЕЗ ЛИМИТ С СОБАЧКОЙ @
# limit_price = 1000
# print(shop.query('price>@limit_price')[['product_name', 'price']])

# categories = ['Perfume concentrate', 'Absolute']
# limit_price = 1000
#  print(shop.query('category in @categories and price >@limit_price')[['product_name']])

# С ИНДЕКСОМ
# print(shop.query('5 <= index <= 8') [['product_name', 'price']])


# ДУБЛИКАТЫ
# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# print(shop[['product_name', 'price']].head())
# print(shop[['product_name', 'price']].duplicated().head()) 
# print(shop[['product_name', 'price']].duplicated().sum())

# # считаем сколько всего строк
# count_all = len(shop[['product_name', 'price']]) 
# # print(count_all)
# count_duplicates = shop[['product_name', 'price']].duplicated().sum()
# print(count_all - count_duplicates)

# УДАЛЕНИЕ ДУБЛИКАТОВ

# customer = shop.loc[:, 'customer_id':'contact_information'].drop_duplicates()
# print(len(customer))

# print(shop['category'].unique())
# print(shop['category'].sort_values().unique())
# print(shop.sort_values(by = 'category', ascending = True)) 

# Вывести заказы 2023 года с total > 10 000 через query(). Выведите 10 строк

# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# shop['order_date'] = pd.to_datetime(shop['order_date'], errors='coerce')
# shop['year'] = shop['order_date'].dt.year
# filter_shop = shop.query('year == 2023 and total > 10000')[['order_id']]
# print(filter_shop.head(10))

# Вывести продукты категории "Absolute" и объёмом 2.5 мл через query() и 
# с drop_duplicates()
# shop = pd.read_csv('shop.csv', sep=',', encoding='utf-8')
# filter_shop = shop.query('category == "Absolute" and volume_ml == 2.5')[['product_name', 'volume_ml', 'category']].drop_duplicates()
# print(filter_shop)

# Загрузите данные из csv-файла в датафрейм c помощью 
# библиотеки pandas.
# Изучите общую информацию о полученном датафрейме.
# Рассмотрите типы данных в каждом столбце.
cars = pd.read_csv('cars.csv', sep=',', encoding='utf-8')

# print(cars.head())
# Изучите уникальные значения в столбцах с названием 
# ренда автомобиля и цвета. Устраните неявные дубликаты 
# и некорректные значения. Например, для колонки brand 
# значения «BMV» и «bmv» – это одно и то же значение.

cars['brand'] = cars['brand'].str.lower().str.strip().replace({'bmv':'bmw'})
cars['color'] = cars['color'].str.lower().str.strip()
# # print(cars['color'].unique())
duplicates = cars[cars.duplicated()]
cars = cars.drop_duplicates()
# print(cars.count())

# рассчитываем долю покупок. 
brand = cars['brand'].value_counts(normalize=True)*100
print(brand.round(1))

# определите топ 3 цвета у покупателей 
color = cars['color'].value_counts(normalize=True)*100
print(color.round(1).head(3))

# Создайте переменную filtered_orders. Занесите 
# в нее датафрейм, который содержит только те заказы, в 
# которых бренд автомобиля BMW представлен в холодных 
# тонах.
# Посчитайте количество таких заказов. 
# (Если все шаги до этого выполнены верно, то должно 
#  получиться 28 заказов)
cold_colors = ['blue', 'grey']
filtered_orders = cars[(cars['brand'] == 'bmw') & (cars['color'].isin(cold_colors))]
print(len(filtered_orders))