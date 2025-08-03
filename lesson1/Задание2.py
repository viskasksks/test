# 2.  Уникальный порядок
# Создайте список самостоятельно и удалите дубликаты из него (дубликаты в исходном списке должны быть), но сохраните исходный 
# порядок появления элементов.

nums = [1, 3, 4, 1, 4, 3, 1, 2, 3]
duplicates = [] 




for element in nums:
    if element not in duplicates:
        duplicates.append(element)

print(duplicates)
