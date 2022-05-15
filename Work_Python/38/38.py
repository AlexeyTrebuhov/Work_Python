# 	Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример: Входные данные:  'ываабв лповап абвцукв алоабвабв ываываыв'
#  Вsходные данные: 'лповап ываываыв'

import os
os.system ('cls')

text = "ываабв лповап абвцукв алоабвабв ываываыв 325валлвы 590957907абв34235233454590787"
sep = ' '
result = [x+sep for x in text.split(sep)]
print('Исходный текст =')
print(text)
a = input('Введите сочетания букв, слова с которыми нужно удалить \n')
b = len(result)
ind = 0
textout = []

while ind < b:
    if a in result[ind]:
        textout = textout
    else:
        textout.append(result[ind])
    ind = ind + 1

print('Текст после обработки =')
print(" ".join(map(str, textout)))
