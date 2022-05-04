# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21, 13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

import os
os.system('cls')

n = int(input('Введите число N =   '))
m = n
x = 0
temp = 1

mas1 = [0]

while n > 0:
    i = x + temp
    mas1.append(i)
    temp = x
    x = i
    n = n - 1
del mas1[0]

y = 0
temp1 = 1
mas2 = [0]

while m > 0:
    j = y + temp1
    mas2.append(j)
    temp1 = -y
    y = -j
    m = m - 1

mas3 =[]
for k in reversed(mas2):  # разворот массива
    mas3.append(k)

mas4 = []
mas4 = mas3 + mas1
print(mas4)
