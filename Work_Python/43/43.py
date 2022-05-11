#  Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#  Пример: [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]

import os
import random
from tkinter import X
os.system('cls')

print('Дублирующиеся цифры в процессе работы меняем на 404')
mas = []
for j in range(25):
    mas.append(random.randint(0,9))
print('Исходный список =  ',mas)
print()

y = mas[0]  
count = 0
start = 1

while start > 0:
    for i in mas:
            for j in mas:   
                if i == j:
                    count = count + 1  #Здесь находим. что внутри списка число i находится более 2 раз
            
            # Как только узнали, что число i дублируется, то запускается перебор массива с условием:
            # число = числу, если оно не равно i ( != i). Иначе новое имя( 404) для числа в массиве 
            if count > 1:                
                if i in mas:
                    new_name = 404
                    mas = [name if name != i else new_name for name in mas]
                    print('Число',i, 'повторяется',count,'раз')
                
            for w in mas:
                if w == 404:
                    mas.remove(404)
                    #print('Список после чистки',mas)
            count = 0
    start = 0

print()
print('Cписок без дублей = ', mas)  
print()

