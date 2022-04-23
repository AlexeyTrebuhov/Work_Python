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

handle = open("1.txt")
handle = open(r"C:\Users\mike\py101book\data\1.txt", "r")
