# 22.	Найти сумму чисел списка стоящих на нечетной позиции

import random
import os
os.system('cls')

mas = []
for i in range(15):
   mas.append(random.randint(1, 15))
print('Рандомный список =', mas)

mas1 = mas[::2]
print('Числа на нечетных позициях =',mas1)
print ('Сумма элементов = ', end ='' )
print(sum(mas1))
