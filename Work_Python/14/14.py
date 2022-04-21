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

print (b3)
print (b4)

sum = 0
for i in b4:
    temp = int(i)
    sum = sum + temp
print (sum)


#res = [int(x) for x in str(b2[0])]
#print("The list from number is " + str(res))


