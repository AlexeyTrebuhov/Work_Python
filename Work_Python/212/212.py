#Для натурального n создать словарь индекс-значение, состоящий из элементов 
# последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system("cls")

n = int(input('Введите число N \n'))

list1 = [i for i in range(0, n)]
list1 = list(map(lambda x: 3*x + 1, list1))
list2 =list(enumerate(list1))
del list2[0]
print(list2)
