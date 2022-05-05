# 29.	Найти НОК двух чисел

from math import trunc
import os
os.system('cls')

min = int(input(' Введите число А = '))
max= int(input(' Введите число B = '))

if min > max:
    temp = min
    min = max
    max = temp

k = min + 1

while max % k > 0:
    k = k -1
    if min % k == 0 and max % k == 0:
        n = min * max / k
    else:
        n = trunc(min * max)
print('Наименьшее общее кратное = ',n)           