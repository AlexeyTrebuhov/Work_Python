# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

import os
os.system("cls")

x = int(input('Введите координату Х       '))
y = int(input('Введите координату Y       '))

print ('\n')
print ('II     |     I')
print ('       |      ')
print('---------------')
print ('       |      ')
print('III    |    IV\n')

str1 = 'Точка расположена '
str2 = 'в позиции 0 на оси Х '
str3 = ' и в позиции 0 на оси Y'
str4 = 'и вдоль оси Y между III и IV четвертями'
str5 = 'и вдоль оси Y между I и II четвертями'
str6 = ' в начале отсчета оси Y, вдоль оси Х между I и IV четвертями'
str7 = 'в IV четверти'
str8 = 'в I четверти'
str9 = ' в начале отсчета оси Y, вдоль оси Х между II и III четвертями'
str10 = 'в III четверти'
str11 = 'во II четверти'

print (str1, end='')

if x == 0:
    print(str2, end='')
    if y == 0:
        print(str3)
    if y < 0 :
        print(str4)  
    if y > 0:
        print(str5)

if x > 0:
    if y == 0:
        print(str6)
    if y < 0:
        print(str7)
    if y > 0:
        print(str8)

if x < 0:
    if y == 0:
        print(str9)
    if y < 0:
        print(str10)
    if y > 0:
        print(str11)
print ('\n')
