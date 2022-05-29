from get_data import get_data
from add_data import add_data


def operations():
    print('Работа с базой: \nПрочитать данные = 1 \nВнести данные    = 2\nВыход - любая клавиша\n')
    a = input('Выберите действие: ')
 
    while True:
        if a == '1':
            print(get_data())
            operations()
        if a == '2':
            add_data()
            operations()
        else:
            exit()
