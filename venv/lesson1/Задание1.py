# 1.  Snake_Case → CamelCase
# Преобразуйте max_value_of_array → maxValueOfArray.

phrase = "max_value_of_array"
parts = phrase.split("_")
one = parts[0]
two = parts[1].capitalize()
three = parts[2].capitalize()
four = parts[3].capitalize()
camelcase = one + two + three + four
print(camelcase)