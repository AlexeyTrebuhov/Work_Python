# 34.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random
import os
import string
os.system('cls')

#k = int(input('Укажите степень K \n'))
k = 4
s = ' * (x**'
s1 = ')'
s2 = ' * '
s3 = 'x'

#  инициализация первого многочлена
mas = []
for i in range(12):
    mas.append(random.randint(0, 100))

a = int(mas[3])
b = int(mas[7])
c = int(mas[0])

if c == 0:      mas[0] = 9
if a % 2 == 0:  mas[4] = ' +'
else:           mas[4] = ' -'
if b % 2 == 0:  mas[8] = ' +'
else:           mas[8] = ' -'

mas[1] = s
mas[2] = k
mas[3] = s1
mas[6] = s2
mas[7] = s3
mas[10] = ' = '
mas[11] = 0

z = ''.join(str(x) for x in mas)
print('Это рандомный многочлен с натуральной степенью k :',z, 'и он сейчас будет записан в файл "1.txt"')
file = open('D:\\Обучение\\Работа в Git\\Work_Python\\34\\1.txt', "w")
for item in z:
    file.write('%s' % item)
file.close()

# инициализация второго многочлена
mas1 = []
for j in range(12):
    mas1.append(random.randint(0, 100))

d = int(mas1[3])
e = int(mas1[7])
f = int(mas1[0])

if f == 0:      mas1[0] = 9
if d % 2 == 0:  mas1[4] = ' +'
else:           mas1[4] = ' -'
if e % 2 == 0:  mas1[8] = ' +'
else:           mas1[8] = ' -'

mas1[1] = s
mas1[2] = k
mas1[3] = s1
mas1[6] = s2
mas1[7] = s3
mas1[10] = ' = '
mas1[11] = 0

z1 = ''.join(str(y) for y in mas1)
print('Это рандомный многочлен с натуральной степенью k :',z1, 'и он сейчас будет записан в файл "2.txt"')
print()
file1 = open('D:\\Обучение\\Работа в Git\\Work_Python\\34\\2.txt', "w")
for item in z1:
    file1.write('%s' % item)
file1.close()

# чтение из файла 1.txt
data = open('D:\\Обучение\\Работа в Git\\Work_Python\\34\\1.txt', "r")
sp = data.readlines()
print('Данные из файла "1.txt" : ' ,sp)
data.close()

# Чтение из файла 2.txt
data1 = open('D:\\Обучение\\Работа в Git\\Work_Python\\34\\2.txt', "r")
sp1 = data1.readlines()
print('Данные из файла "2.txt" : ', sp1)
data1.close()

# Расчет суммы многочленов

number = str(sp)
number1 = number.split("'")
number2 = number1[1].split(" ")

sum1 = int(number2[0])
sum2 = int(number2[3])
sum3 = int(number2[6])

znak = str(sp1)
znak1 = znak.split("'")
znak2 = znak1[1].split(" ")

sum4 = int(znak2[0])
sum5 = int(znak2[3])
sum6 = int(znak2[6])

s0 = sum1 + sum4
s3 = sum2 + sum5
s6 = sum3 + sum6

# Расчет суммарного выражения
mas2 = mas

mas2[0] = s0
if s3 < 0:
    mas2[4] = ' - '
    mas2[5] = -s3
if s3 >0:
    mas2[4] = ' + '
    mas2[5] = s3

if s6 < 0:
    mas2[8] = ' - '
    mas2[9] = -s6
if s6 > 0:
    mas2[8] = ' + '
    mas2[9] = s6

z7 = ''.join(str(k) for k in mas2)
print()
print('Это сумма из двух вышеуказанных многочленов      :', z7, 'и сейчас записана в файл "out1.txt"')
file = open('D:\\Обучение\\Работа в Git\\Work_Python\\34\\out.txt', "w")
for item in z7:
    file.write('%s' % item)
file.close()




