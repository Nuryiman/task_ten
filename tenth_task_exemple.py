# 10. Угадай рандомное число:
# Программа генерирует случайное число и предлагает пользователю угадать его.
# При каждой попытке программа подсказывает,
# больше или меньше загаданное число введенного пользователем числа.

import random


random_number = random.randint(1, 101)

def ugadalka():
    for i in range(7):
        my_number = int(input('Угадайте моё число:'))
        if my_number > random_number:
            print('Моё число меньше чем ваша')
        elif my_number < random_number:
            print('Моё число больше чем ваша')
        else:
            print('ВЫ УГАДАЛИ МОЁ ЧИСЛО')
            break
ugadalka()

