# 	Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму	

from re import I


import os
os.system ('cls')

n = int (input('Введите число N \n '))
sum = 0
i = 1

while i <= n:
    b = (1 + 1/i) **i
    print (b)
    i = i +1
    sum = sum + b
print ('Сумма этих чисел = ',sum)




