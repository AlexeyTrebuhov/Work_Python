# 1.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#  Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import random
import os
from tkinter import Y
os.system ('cls')

mas = []
for i in range(14):
   mas.append(random.randint(1, 14))
print('Рандомный список =', mas)

k = len(mas)
temp = k-1
sum = 0
proizv = 0

while k > 0:
    x = int(mas[0])
    y = int(mas[temp])
    
    k = temp - 1
    proizv = x * y
    
    sum = sum + proizv
    del mas[0],mas [k]
    print(x, y,  'Произведение = ', proizv, 'Сумма = ', sum, 'Остатки массива = ', mas,)
    k = k - 2
    temp = k + 1
