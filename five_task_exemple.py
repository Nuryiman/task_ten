# 5. Вычисление суммы элементов списка:
# Программа вычисляет и выводит сумму всех элементов списка, который вводит пользователь.

my_list = []
while True:
    my_number = int(input('Введите число которую хотите сложить:'))
    my_list.append(my_number)
    if my_number == 0:
        break

# for
print(sum(my_list))