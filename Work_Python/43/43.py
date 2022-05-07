#  Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#  Пример: [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]

import os
import random
from tkinter import X
os.system('cls')

mas = []
for j in range(20):
    mas.append(random.randint(0, 10))
print('Исходный список = ',mas)
print()

masout = mas
poz = 0
prob = 1
         
for i in mas:
    
    for j in mas:
        if j == i:
            poz = poz + 1 
        if poz > 2:    
            y = i   
    
    print('Повторяется =', y,'повторов =', poz,'удаляем его')
   
    r = len(masout)
    while r > 1:
        if i in masout:
            masout.remove(y)
        r = r - 1
    mas = masout
   

    print('Список после удаления = ', mas)
    print()
   
    poz = 0
   

print('Список после удаления = ', masout)
print()
      
    
   
