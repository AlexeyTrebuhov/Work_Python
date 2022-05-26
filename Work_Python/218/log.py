import re


def log_to_file(result, temp):

    if 'В строчку' in result:

        with open('D:\\Обучение\\Работа в Git\\Work_Python\\218\\log1.csv', 'a+') as file:
            file.write(f'{temp[0:4]}, \n')

            # чтение из файла
        data = open(
            'D:\\Обучение\\Работа в Git\\Work_Python\\218\\log1.csv', 'r')
        sp = data.readlines()

        print()
        print('Список абонентов')
        print('Фамилия  Имя   Телефон   Комментарий')

        for line in sp:
            print(line)
        data.close()

    if 'В столбик' in result:
        with open('D:\\Обучение\\Работа в Git\\Work_Python\\218\\log2.csv', 'a+') as file:
            file.write(
                f' {temp[4],temp[0]} \n {temp[5],temp[1]} \n {temp[6],temp[2]} \n {temp[7],temp[3]} \n \n')

        # чтение из файла
        data = open(
            'D:\\Обучение\\Работа в Git\\Work_Python\\218\\log2.csv', "r")
        sp = data.readlines()
        print()
        print('Список абонентов')

        for line in sp:
            print(line)
        data.close()
