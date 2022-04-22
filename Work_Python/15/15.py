# 15.	Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда  [1, 2, 6, 24]

import os
os.system ('cls')

n = int(input( "Введите число N \n"))
count = 0
s = 1

while count < n:
    count = count +1
    s = s*count
    print (s, end = ' , ')
print('\n')






