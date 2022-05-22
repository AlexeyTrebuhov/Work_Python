# 31.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system('cls')

n = int(input('Введите число N: \n'))
list = []
for i in range(2,n):
    while n % i ==0:
        list.append(i)
        n = n / i
    if n == 1:
        break

if len(list) > 0:
    print('Список множителей',list)
    print()
    

