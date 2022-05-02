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

text = (input('Введите любые символы или цифры в том порядке. в котором их нужно найти \n'))
words = text.split()

while count < 10:
    for i, word in enumerate(map(list, words)):
        random.shuffle(word)
        words[i] = ''.join(word)
        count = count + 1
        mas.append(*words)

print('Это рандомный список', mas)

temp = 0
mas1 =[]

for j in mas:
    if j == text:
        mas1.append(temp)
    temp = temp + 1

if len(mas1) > 1:
    del mas1[0]
    print('Значение', text, 'имеет второе и следующие вхождения на индексах', mas1)
else:
    print('Значение', text, 'имеет второе и следующие вхождения на индексах', -1)
     
    
    






