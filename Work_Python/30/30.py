# 	Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.141             10 ^ (-1)≤d≤10 ^ (-10)



import decimal
import os
os.system ('cls')
from decimal import Decimal

x = int(input( "Введите цифру от 1 до 100, определяющую уровень точности при вычислении числа 'пи' \n"))
decimal.getcontext().prec = x

a = 3
sum = 4
count = 0

while  count < 100000:
    sum = Decimal(sum) - Decimal(4/a)
    a = a + 2
    sum = Decimal(sum) + Decimal(4/a)
    a = a + 2
    count = count +1

print (sum)



