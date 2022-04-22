# 14.	Подсчитать сумму цифр в вещественном числе.

import os
os.system ('cls')

a = int (input(' Наберите число от -9 до 9\n'))
b = - a * 12345 / 7
b1 = str (float(b))

print ('Ваше вещественное число',b1)
b2 = b1.split('.')
b3 = b2[0]
b4 = b2[1]

if b < 0:
    b5 = b3.split('-')
    b6 = b5[1]
else:
    b6 = b3

print ('Цифры до запятой', b3)
print ('Цифры после запятой', b4)

sum1 = 0
for j in b6:
    temp = int(j)
    sum1 = sum1 + temp
print('Сумма цифр перед запятой без учета знака числа =', sum1)

c = int(b6[0])

if b < 0:
    sum2 = sum1 - 2*c
else:
    sum2 = sum1
print ('Сумма цифр перед запятой с учетом знака числа = ', sum2)

sum = 0
for i in b4:
    temp = int(i)
    sum = sum + temp
print('Сумма цифр после запятой =', sum)

print ('Общая сумма чисел вещественного числа =', sum + sum2)



 



#res = [int(x) for x in str(b2[0])]
#print("The list from number is " + str(res))


