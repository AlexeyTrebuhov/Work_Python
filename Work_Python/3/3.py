# 3.	Вывести на экран числа от -N до N

import os
os.system ("cls")

print ('Введите число N')
n=int (input ())
temp=-n
while temp<=n:
    print(temp, end=' , ')
    temp=temp+1
print('\n')
