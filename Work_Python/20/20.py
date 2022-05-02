20.  # Определить, присутствует ли в заданном списке строк, некоторое число

import random
import os
os.system("cls")

x = int(input( 'Введите число от 0 до 5. которое нужно найти \n'))
mas = []
sum = 0
count = 0
mas1 = []

for i in range(25):
   mas.append(random.randint(0, 5))
print('Это рандомный список из N элементов =', mas)
for j in mas:
    if j == x:
        mas1.append(sum)
        count = count + 1
    sum = sum + 1
print('Число',x,'находится на индексах',mas1,'общим количеством',count, 'раз')

