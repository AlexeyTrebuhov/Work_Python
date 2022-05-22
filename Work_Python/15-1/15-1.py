# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
import os
from itertools import accumulate
import operator
import random
os.system("cls")

n = random.randint(8, 16)

print(' Задать последовательность из', n, 'элементов\n',
      'Последовательность:', *list(accumulate([x for x in range(1, n + 1)], operator.mul)), '\n')
