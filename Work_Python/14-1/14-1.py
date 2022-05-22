# Подсчитать сумму цифр в вещественном числе.
import os
import random
os.system("cls")

# задаем случайное вещественное число из диапазона
a = random.uniform(1, 1001)

print('Задано число:', a, '\nСумма цифр данного числа равна:', sum(
    map(int, str(a).replace('.', ''))), '\n')
