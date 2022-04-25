# 17.	Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

import random
import os
os.system ("cls")

n = int ( input( 'Введите число N =  '))

mas = []
for i in range(n):
   mas.append(random.randint(-n, n))
print('Это рандомный список из N элементов =', mas)

m = []
for j in range(n):
   m.append(random.randint(1,n))
print ('Это рандомные номера позиций        =', m,'и они сейчас будут записаны в файл "file.txt"')

file = open('D:\\Обучение\\Работа в Git\\Work_Python\\17\\file.txt', "w")
for item in m: file.write('%s\n' % item) 
file.close()

temp = 1
sum = 1

data = open('D:\\Обучение\\Работа в Git\\Work_Python\\17\\file.txt', "r")
print()
print('А это данные, уже извлеченные из файла "file.txt" =')
print()
for line in data:
 
   k = int(line)
   k1=k-1
   temp = mas[k1]
   sum = sum * temp
   print('Из рандомного списка,число', temp, 'соответствует номеру позиции', line)
data.close()


temp = 1
sum = 1

data = open('D:\\Обучение\\Работа в Git\\Work_Python\\17\\file.txt', "r")
print()
print('Итоговое произведение всех цифр =')
for line in data:
 
   k = int(line)
   k1=k-1
   temp = mas[k1]
   sum = sum * temp
   print(temp, '*', end = ' ')
data.close()
   
print('=',sum)   
print()




