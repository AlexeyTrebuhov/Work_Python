# 1.	В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

import os
import random
os.system("cls")

start = random.randint(-1000,1000)
n = int(input('Введите число N = '))

mas = [start]
for i in range(n):
    start = start + 1
    mas.append(start)

a = random.randint(1,n)
del mas[a]

# создаем файл file.txt и записываем в него
file = open('D:\\Обучение\\Работа в Git\\Work_Python\\35\\file.txt', "w")
for item in mas:
    file.write('%s ' % item)
file.close()

# чтение из файла file.txt
data = open('D:\\Обучение\\Работа в Git\\Work_Python\\35\\file.txt', "r")
sp = data.readlines()
print('N натуральных чисел из файла "file.txt" : ' ,sp)
data.close()


f = ""

for i in sp:
    f += str(i)+ " " 

f1=list(f.split())
mas1=list(map(int,f1))

k = int(mas1[0])

for j in mas1:
    while j == k:
       k = k+1
print('В данном списке не хватает числа ',k)