# 2.	Найти максимальное из пяти чисел

import os
os.system("cls")

list=[-5,89,37,110,5]
temp=0
for i in list:
    if i>temp:
       temp=i
print(temp)
