import os
os.system ("cls")

print ('Введите число a')
a=int (input ())
print ('Введите число b')
b=int (input())
c=a**2
if c==b:
    print ('Число', a ,'является квадратом', b)
else:
    print('Число', a, 'не является квадратом', b)
