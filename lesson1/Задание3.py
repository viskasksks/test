# 3.  Топ-3 продаж
# Создайте подходящий кортеж для условия ниже.
# Есть кортеж годовых продаж по месяцам. Верните кортеж трёх лучших месяцев (индексы).

sales = (100000, 150300, 223491, 527095, 162539, 915284, 716294)
new_list = sorted(sales)
first_three = new_list[-3:]
indicies = []



for element in first_three:
    num = sales.index(element)
    indicies.append(num)

print(indicies)
