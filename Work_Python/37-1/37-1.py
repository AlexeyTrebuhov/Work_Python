# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие
# максимальное количество элементов. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]  Порядок элементов менять нельзя

# Это решение неверное. Список выдает не полный.

import os
from random import *
os.system('cls')

nums = [randint(1,9) for i in range(21)]
print( 'Массив несортированный', nums)

def mas(nums):
    masout = [nums[0]]
    for i in nums:
        if i > max(masout):
            masout.append(i)
    return masout

print('Максимальный список от первой цифры и до конца', mas(nums))

largest = 0 # стартовая максимальная длина списка
index = 0

for i in range(len(nums)): 
    if len(mas(nums[i:])) > largest: # бегаем в цикле по массиву и постоянно сравниваем длину
        largest = len(mas(nums[i:]))
        index = 1

print('Итого сокращенный список', nums[index:])
print('Максимальная последовательность', mas(nums[index:]),'\n')