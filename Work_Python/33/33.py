# 33.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:  k = 2 = > 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
os.system('cls')
import random

k = int(input('Укажите степень K \n'))
s = ' * (x**'
s1 = ')'
s2 = ' * '
s3 = 'x'

mas = []
for i in range(12):
    mas.append(random.randint(0, 100))

a = int(mas[3])  
b = int(mas[7])
c = int(mas[0])

if c ==0:
    mas[0] = 9

if a % 2 == 0:
    mas[4] = ' + '
else: mas[4] = ' - '

if b % 2 == 0:
    mas[8] = ' + '
else:
    mas[8] = ' - '

mas[1] = s
mas[2] = k
mas[3] = s1
mas[6] = s2
mas[7] = s3
mas[10] = ' = '
mas[11] = 0

s = ''.join(str(x) for x in mas)
print('Это рандомный многочлен с натуральной степенью k :', s, 'и он сейчас будет записан в файл "file.txt"')
print()

file = open('D:\\Обучение\\Работа в Git\\Work_Python\\33\\file.txt', "w")
for item in s:
    file.write('%s' % item)
file.close()
