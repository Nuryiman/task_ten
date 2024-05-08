# 6. Нахождение максимального элемента в списке:
# Программа находит и выводит самый большой элемент в списке.

my_list = [5, 10, 3, 8, 16, 7]
max_number = 0
for item in my_list:
    if item > max_number:
        max_number = item

print(max_number)
