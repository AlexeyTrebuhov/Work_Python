#  Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

import random
import os
from tkinter import N
os.system ('cls')

a = int (input ('Выберите число от 1 до 9  \n'))
b = int (input ('Выберите еще одно число в том же диапазоне \n'))
s1 = random.sample(range(15),a)
s2 = random.sample(range(15),b)
s3 = []
print('Первый массив', s1)
print('Второй массив', s2)

k = 0

for i in s1:
    for j in s2:
        if i ==j:
            k = k +1
            s3.append (i)
s3.sort()  

print ('Количество одинаковых значений между массивами',k)
print ('Это значения' ,s3)
print ('\n')