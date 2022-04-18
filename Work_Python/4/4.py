# 4.	Показать первую цифру дробной части числа

import os
os.system("cls")

number = float(input('Введите число '))
number = str(float(number))
number2 = number.split('.')
print('Часть числа до разделителя =', number2[0])
print('Часть числа после разделителя =', number2[1])
number3 = number2[1]
print('Первая цифра дробной части числа =', number3[0])
