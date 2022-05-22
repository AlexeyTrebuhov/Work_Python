#.	Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда  [1, 2, 6, 24]
import os
os.system('cls')

n = 5
list1 = [i for i in range(0, n)]
list2 = []

while n > 0:
    list2.append(1)
    n = n - 1
    list2.append(-1)
    n = n-1

list1 = list(map(lambda x, y: (3**x)*y, list1, list2))
print(list1)
