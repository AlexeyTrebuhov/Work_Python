# 34.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import os
import string
os.system('cls')

mas = ""
data = open('D:\\Обучение\\Работа в Git\\Work_Python\\34\\1.txt', "r")
for line in data:
    mas += str(line)
print('Данные из файла "1.txt" : ' ,mas)
print()
   
number = str(mas)
number1= number.split('=')
data.close()

mas1 = ""
data1 = open('D:\\Обучение\\Работа в Git\\Work_Python\\34\\2.txt', "r")
for line in data1:
    mas1 += str(line)
print('Данные из файла "2.txt" : ', mas1)
print()
data1.close()

j = '+ '
m = number1[0] + j + mas1
print('Это сумма многочленов из файла 1 и 2 :', m)
print('Выражение записано в файл "out.txt"')
print()

file = open('D:\\Обучение\\Работа в Git\\Work_Python\\34\\out.txt', "w")
for item in m:
    file.write('%s' % item)
file.close()




