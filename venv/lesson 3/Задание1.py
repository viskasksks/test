# Выполните	фильтрацию	с	помощью	[	],	.loc[]	и	.query().	
# Объедините	таблицы	contacts,	customers,	orders.	Будьте	внимательны,	не	все	
# пользователи	делали	заказы.	
# Отберите	все	записи	о	продажах	пользователеи	из	европеиских	стран	и	России,	
# совершенных	в	первые	два	квартала	2023	года.	Оставьте	поля	order_id	и	total.	
# Определите	сумму	отобранных	продаж.	
# Сумма	продаж:	659255.0
import pandas as pd
contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_1 = contacts.merge(customers, on='customer_id', how='left')
merged_1 = merged_1.merge(orders, on='customer_id', how='left')

europe_russia = ['Russia', 'Italy', 'Germany', 'France', 'UK', 'Spain', ]

merged_1['order_date'] = pd.to_datetime(merged_1['order_date'], errors='coerce')

# фильтрация []

filtered_1 = merged_1[(merged_1['country'].isin(europe_russia)) & (merged_1['order_date'] >= '2023-01-01') & (merged_1['order_date']<= '2023-06-30')][['order_id', 'total']]
print(filtered_1)


# фильтрация .loc

mask = (merged_1.loc[:, 'order_date'].dt.year == 2023) & (merged_1.loc[:, 'order_date'].dt.month <= 6) & (merged_1.loc[:,'country'].isin(europe_russia))
filtered_2 = merged_1.loc[mask, ['order_id', 'total']]
print(filtered_2)

# фильтрация .query()
merged_1['year'] = merged_1['order_date'].dt.year
merged_1['month'] = merged_1['order_date'].dt.month
filtered_3 = merged_1.query('country.isin(@europe_russia) and year == 2023 and month <=6')[['order_id', 'total']]
print(filtered_3)

# сумма
sum_sales = filtered_3['total'].sum()
print(sum_sales)