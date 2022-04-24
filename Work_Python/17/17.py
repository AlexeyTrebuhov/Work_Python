# 17.	Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

import random
import os
os.system ("cls")

n = int ( input( 'Введите число N \n'))

mas = []
for i in range(n):
   mas.append(random.randint(-n, n))
print('Это список из N элементов = ', mas)

m = []
for j in range(n):
   m.append(random.randint(1,n))
print (' Это номера позиций. Они записываются в файл', m)

file = open('D:\\Обучение\\Работа в Git\\Work_Python\\17\\file.txt', "w")
for item in m: file.write('%s\n' % item) 
file.close()

temp = 0
sum = 0
file = open('D:\\Обучение\\Работа в Git\\Work_Python\\17\\file.txt', 'r')
print(' Это номера позиций. Они прочитаны из файла',file)

for i in range(len(m)):
   k = int(m[i])
   k1=k-1
   temp = mas[k1]
   sum = temp**2
   print('Это цифра на выбранной позиции =', temp, 'и ее произведение =', sum)



