# 2. Определение чётности числа:
# Пользователь вводит целое число, а программа определяет, является ли оно чётным или нечётным,
# и выводит соответствующее сообщение.

number = int(input('Введите число:'))

if number % 2 == 0:
    print('Это число четное')

else:
    print('Это число нечетное')
