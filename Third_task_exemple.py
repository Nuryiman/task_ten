# 3. Нахождение наименьшего числа:
# Программа принимает три целых числа от пользователя и выводит значение наименьшего из них.

number1 = int(input('Введите первое число:'))
number2 = int(input('Введите второе число:'))
number3 = int(input('Введите третее число:'))

if number1 < number2 < number3:
    print('Наименьшее значение из этих чисел это', number1)

elif number2 < number1 < number3:
    print('Наименьшее значение из этих чисел это', number2)

elif number3 < number2 < number1:
    print('Наименьшее значение из этих чисел это', number3)

