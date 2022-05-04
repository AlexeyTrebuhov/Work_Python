# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
import random
os.system("cls")

mas1 = []
for i in range(3):
   mas1.append(random.randint(101,113))

mas2 = []
for j in range(5):
   mas2.append(random.randint(11,13))

mas = []
mas3 = []

for k in mas1:
   for d in mas2:
      x1 = k / d
      x = round(x1,5)
      mas.append(x)
      a3 = float(x)
      a2 = str(float(a3))
      a = a2.split('.')
      mas3.append(a[1])   
     
print('Рандомный список вещественных чисел = ')
print(mas)
s1 = int(min(mas3))
s2 = int(max(mas3))
s = s2 - s1
print('Цифры после запятой: Max = ',s2, 'Min = ', s1, 'Разница = ',s)
print()


