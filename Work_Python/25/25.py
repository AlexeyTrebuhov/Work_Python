# 25.	Написать программу преобразования десятичного числа в двоичное

import os
os.system('cls')

n = int(input('Введите десятичное число N =   '))

mas = []
mas1 = []

while n > 1: 
    m1 = n / 2
    m2 = n % 2
    if m2 > 0:
        m1 = m1 - 0.5
    n = round(m1)
    mas.append(m2)
    if n == 1:
        mas.append(n)

for i in reversed(mas): # разворот массива
    mas1.append(i)

y = int(''.join(map(str, mas1)))
print('В двоичной системе это число представлено так = ', y)