#Подсчитать сумму цифр в вещественном числе.

import os
os.system('cls')
import random

a = random.uniform (111,2)
print('Вещественное число = ',a)
b1 = str(float(a)).split('.')
b = b1[0]+b1[1]  
print('Сумма чисел =', sum(int(i) for i in str(b)))
