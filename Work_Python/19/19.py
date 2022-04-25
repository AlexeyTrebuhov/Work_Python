# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

import os
os.system ('cls')

a = int(input('Наберите любое число = '))
b = - a * 3 / 4
round(b, 2)
b1 = str(float(b))

b2 = b1.split('.')
b3 = b2[0]
b4 = b2[1]

if b < 0:
    b5 = b3.split('-')
    b6 = b5[1]
else:
    b6 = b3

s1 = int(b4)
s2 = int(b3)
s = s2 - s1
if s > 1000:
    s = s/100

with open('D:\\Обучение\\Работа в Git\\Work_Python\\19\\file.txt', "r") as f:

    for line in f:
        k = int(line)

d = k*s
print('Рандомное число = ',d)
print()
print('Если снова набрать число',a,'то рандомное число будет другое')


if k > 100:
    k = - 78
if k <=100:
    k = k + 13

file = open('D:\\Обучение\\Работа в Git\\Work_Python\\19\\file.txt', "w")
file.write(str(k))
file.close()
print()