# 17.	Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

import random
import os
os.system ("cls")

n = int ( input( 'Введите число N \n'))

mas = []
for i in range(n):
   mas.append(random.randint(-n, n))
print(mas)

m = []
for j in range(n):
   m.append(random.randint(1,n))
print (m)

file = open('D:\\Обучение\\Работа в Git\\Work_Python\\17\\file.txt', "w")
for item in m: file.write('%s\n' % item) 
file.close()

temp = 0
sum = 0
file = open('D:\\Обучение\\Работа в Git\\Work_Python\\17\\file.txt', 'r')
for j in file:
   #for i in mas:
      temp = j
      print (temp)
      sum = mas[j]      
      print (sum)
      #temp = mas(i)**2
      #sum = sum + temp
      #print (sum)

