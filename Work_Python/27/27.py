# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

import os
import random
os.system("cls")

mas = []
for i in range(19):
   mas.append(random.randint(10,99))

f = ""

for i in mas:
    f += str(i)+ " " 

print('Строка из чисел через пробел = ', f)

f1=list(f.split())
mas1=list(map(int,f1))

s1 = int(min(mas1))
s2 = int(max(mas1))

print ('Меньшее число =',s1,', Большее число = ',s2)
