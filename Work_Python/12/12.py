# 12.	Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system ('cls')

f = int(input ('Введите число N \n'))

d = {a:a*3+1 for a in range(f+1)}
del d[0]

print (d)