# 22.	Найти сумму чисел списка стоящих на нечетной позиции

import random
import os
os.system('cls')

mas = []
for i in range(15):
   mas.append(random.randint(2, 15))
print('Это рандомный список =', mas)

sum = 0
mas1 = []
k = 0

for j in mas:
   k = int(mas[j])
   print(k)
   if k % 2 > 0:
      sum = sum + k
      mas1.append(k)

print(mas1)
print(sum)
