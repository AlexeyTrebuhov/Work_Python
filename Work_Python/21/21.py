# 21.	Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

import random
import os
os.system('cls')
count = 0
mas = []

text = (input('Введите символы "q", "w", "e" в том порядке. в котором их нужно найти \n'))
words = text.split()
print(words)
while count < 20:
    for i, word in enumerate(map(list, words)):
        random.shuffle(word)
        words[i] = ''.join(word)
        count = count + 1
        mas.append(*words)

print('Это рандомный список', mas)

temp = 0
mas1 =[]
for j in mas:
    if j == words:
        temp = temp + 1
        if temp > 1:
            mas1.append(j)
print(mas1)





