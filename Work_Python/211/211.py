# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system("cls")

n = int(input('Введите число N \n'))

list1 = [i for i in range(0, n)]
list2 = []

while n >0:
    list2.append(1)
    n = n -1
    list2.append(-1)
    n = n-1

list1 = list(map(lambda x,y: (3**x)*y, list1, list2))
print(list1)



