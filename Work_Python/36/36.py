# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

import os
import random
os.system('cls')

mas = []
for j in range(15):
    mas.append(random.randint(0,30))
print('Исходный список =  ',mas)

while len(mas) > 1:
    masout = mas
    min = mas[0]
    mas1 =[min]

    sum = 0

    for i in mas:
        sum = sum + 1
        if i > min:
            mas1.append(i)        
            min = i                 
            delet = sum -1
            del masout[delet]
    del masout[0]

    mas = masout

    print('Из верхнего списка создана последовательность =   ',mas1, '   Остаток = ', masout)
print()



