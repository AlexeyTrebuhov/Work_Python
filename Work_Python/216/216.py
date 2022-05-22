# 	Задать список из n чисел последовательности (1+〖1/n)〗^n и 
#   вывести на экран их сумму

from re import I
import os
os.system('cls')

n = int(input('Введите число N \n'))

num = [round((1+(1/i)**i),3) for i in range(1, n+1)]
print('Получена последовательность', num)
print('Сумма чисел = ', sum(num), '\n')
