# words = ['Скоро', 'будет', 'контрольная']
# words = " ".join(words)
# print(words)

# Посчитайте, сколько раз встречается число 3
# nums = [3, 1, 3, 7, 3, 2]
# nums = nums.count(3)
# print(nums)

# Создайте словарь {'a': 1, 'b': 2}. Добавьте ключ 'c' со значением 3, затем увеличьте 'a' на 5.

# b = {
#     'a': 1, 
#     'b': 2
# }
# b['c'] = 3
# b['a'] += 5
# print(b)

# s = '***---Привет, мир!---***'
# s = s.strip("*-")
# print(s)

# words = ['Сегодня', 'хорошая', 'погода']
# words = " ".join(words) + "."
# print(words)

# nums = [5, 3, 8, 3, 3, 1, 7]
# nums = nums.count(3)
# print(nums)

# my_dict = {'x': 10, 'y': 20}
# my_dict['z'] = 30
# my_dict['x'] += 15
# print(my_dict)

# messy_str = '---***   Python 3.9 ***---'
# messy_str = messy_str.strip("-*")
# messy_str = messy_str.lstrip(' ')
# messy_str = messy_str.rstrip(' ')
# print(messy_str)

text = "!!!___Вот это да, снова Python?!___!!!"
text = text.strip("!_?")
print(str.lower(text))

words = ['как', 'интересно', 'изучать', 'python']
words = ' '.join(words).title()
print(words)

phrase = ['Да', 'начнётся', 'великая', 'проверка']
phrase = ''.join(phrase)
print(phrase)
print(len(phrase))

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = {
    1: nums.count(1),
    2: nums.count(2),
    3: nums.count(3),
    4: nums.count(4),
}
print(counts)