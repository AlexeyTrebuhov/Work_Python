# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие 
# максимальное количество элементов. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]  Порядок элементов менять нельзя

import os
import random
os.system('cls')

mas = []
for j in range(9):
    mas.append(random.randint(0,9))
print('Исходный список =',mas)  # тут задали массив

indmas = [1] * 2
l = len(mas) # создали массив индексов и получили длину массива

n = 2 # это стартовая величина размера массива masmin

while n <= l: # увеличение массива masmin от 2 позиций до окончательного размера
    m = n - 1
    masmin = mas[0:n] # задается изменяемый массив
    max = mas[m]      # это последняя цифра изменяемого массива 
    indexmax = m  # это индекс последней цифры изменяемого массива
    #print('самая правая цифра =', max, 'индекс =', indexmax, )
   
    for i in range(len(masmin)-1) and range(len(indmas)-1):  # тут мы получаем цифру и индекс массива чисел
        #print('Проверяемое число и индекс',masmin[i], i, 'Проверяемые цифра и индекс массива индексов', count[i], i)      

        if max > masmin[i] and indmas[indexmax] <= indmas[i]:
            indmas[indexmax] = indmas[i] + 1  

    n = n + 1
    indmas.append(1) 

del indmas[l] # удаляем лишнее последнее прибавленное значение

z = sorted(indmas)
z.reverse()
zmax = z[0] # определяем максимально возможную длину последовательности
print('длина',zmax)
print()

# объединяем список индексов максимальной длины и список цифр.
# при этом список индексов первый. По нему будем выстраивать последовательность
dic = list(zip(indmas, masmin))
dic1 = sorted(dic) # сортируем по возрастанию длины последовательности
dic1.reverse() # разворачиваем по убыванию длины последовательности
# первое значение - макс.длина, второе - соответствующая цифра из списка "masmin"
print (dic1)

masoutx = []
masouty = []
masout = []

for x, y in dic1: # разделяем словарь на два списка
    masoutx.append(x) # это индексы максимальной длины последовательности
    masouty.append(y) # это цифры максимальной длины последовательности
print('начальное masoutx',masoutx)
print('начальное masouty', masouty)
 
temp = masouty[0] 
stopx = 1
stopy = 1
print('начальное число',temp,'длина', zmax,masout)
print()

sum = 0
while sum < l:
    print('masoutx', masoutx[sum], 'masouty', masouty[sum])
    if masoutx[sum] < zmax and  masouty[sum] < temp:
        masout.append(masouty[sum])        
        
     
    sum = sum + 1
    #temp = masouty[0]
    #zmax = zmax - 1
        
        
       
   
   
    print( masoutx)
    print( masouty) 
    print('начальное число', temp, 'длина', zmax)
    print('masout',masout)
    print()

 
    
   
        
print('masoutx = ',masoutx,'masouty',masouty, 'masout', masout)




