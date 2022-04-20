# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system("cls")

n = int(input('Введите число N \n'))
s = [1] * n

a = 1
b = -3

for i in range(len(s)):
    s[i] = a
    a = a * b

print (s,'\n')

