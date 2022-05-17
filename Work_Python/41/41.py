# 38.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: На сжатие: Входные данные: #WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные: 12W1B12W3B24W1B14W

from collections import Counter
import os
import random
os.system('cls')

n = random.randint(25,75) # задаем случайую длину строки с несжатыми данными

mas = []
def generate_random_string(length):
    letters = 'WWSSSSB'
    text = ''.join(random.choice(letters) for i in range(length))
    mas.append(text)
generate_random_string(n) # генерируем строку с несжатыми данными

file = open('D:\\Обучение\\Работа в Git\\Work_Python\\41\\in.txt', "w")
for item in mas:
    file.write('%s' % item)
file.close() # записали несжатые данные в файл in.txt

data = open('D:\\Обучение\\Работа в Git\\Work_Python\\41\\in.txt', "r") # Сразу же чтение из файла in.txt
sp = data.readlines()
print('Данные из файла "in.txt" : ', sp)
data.close()

a = str(sp)
#print(a)

sum = 1
min = 0
max = 1
len = len(a)
masout = []

while len > 1:
    s1 = ord(a[min])
    s2 = ord(a[max])
            
    if  s1 == s2:
            len = len - 1
            sum = sum + 1
            min = min + 1
            max = max + 1
        
    else:
            masout.append(sum)
            masout.append(a[min])
            len = len - 1
            sum = 1
            min = min + 1
            max = max + 1

del masout[0:4] # удаляем лишние первые 4 символа ( скобки и их количество)
del masout[-1:-2] # удаляем последние лишние символы (скобки и количество)

#print(masout) #тут остался список с запятыми и прочим мусором. нужно удалить лишнее

fun = ''.join(str(x) for x in masout )

print('Это сжатый файл: ', fun)

print('Запишем результат в файл "out.txt"')
file = open('D:\\Обучение\\Работа в Git\\Work_Python\\41\\out.txt', "w")
for item in fun:
    file.write('%s' % item)
file.close()
print()
