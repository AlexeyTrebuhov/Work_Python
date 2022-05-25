# 32.	Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

import os
os.system('cls')
import random

n = int(input('Введите число =  '))
mas = []
for i in range(n*4):
   mas.append(random.randint(0, 20))
print('Это произвольный список =', mas)
print()
mas.sort()
print('Это сортированный список =', mas)
print()

list = [1]
list[0] = mas[0]

x = int(list[0])
temp = 0

for i in range(len(mas)):
    temp = int(mas[i])
  
    if x == temp:
        x = temp
        i = i + 1

    if x < temp:
        list.append(temp)
        x = temp
        i = i + 1
print('Это неповторяющийся список',list)


