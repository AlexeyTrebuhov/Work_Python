# 18.	Реализовать алгоритм перемешивания списка.

import random
import os
os.system ('cls')

n = int(input('Введите число N =  '))

mas = []
for i in range(n):
   mas.append(random.randint(-1, n*10))
print('Это рандомный список из N элементов =', mas)

m = [3,4,2,0,1]
print('Это порядок премешивания списка ( по индексу )=', m,)

mas1 = [1]*n   

s = 0
sum = n 

while sum >= 5:
    a = s
    b = a + 1
    c = a + 2
    d = a + 3
    f = a + 4

    mas1[a] = mas[d]
    mas1[b] = mas[f]
    mas1[c] = mas[c]
    mas1[d] = mas[a]
    mas1[f] = mas[b]
        
    s = s + 5
    sum = sum - 5
        
if sum == 4:
    a = s
    b = a + 1
    c = a + 2
    d = a + 3
    mas1[a] = mas[c]
    mas1[b] = mas[a]
    mas1[c] = mas[d]
    mas1[d] = mas[b]

if sum == 3:
    a = s
    b = a + 1
    c = a + 2
    mas1[a] = mas[c]
    mas1[b] = mas[a]
    mas1[c] = mas[b]
           
if sum == 2:
    a = s
    b = a + 1
    mas1[a] = mas[b]
    mas1[b] = mas[a]

if sum == 1:
   a = s
   mas1[a] = mas[a]
    
print(mas1)

   
   


