# 14.	Подсчитать сумму цифр в вещественном числе.

import os
os.system ('cls')

a = int (input(' Наберите число от 1 до 9\n'))
b = - a * 12345 / 7
b1 = str (float(b))
print ('Ваше вещественное число',b1)
b2 = b1.split('.')
b3 = b2[0]
b4 = b2[1]

b5 = b3.split('-')
b6 = b5[0]
b7 = b5[1]

print (b3)
print (b4)

sum = 0
for i in b4:
    temp = int(i)
    sum = sum + temp
for j in b7:
    temp = int(j)
    sum = sum + temp

print (sum)

z = chr(b[0])
print (z)
 



#res = [int(x) for x in str(b2[0])]
#print("The list from number is " + str(res))


