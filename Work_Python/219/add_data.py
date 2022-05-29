from get_data import get_data
from get_data import push_data


def add_data():
    result_list = get_data()
    id = int(len(result_list))
    string = ''
    string += str(id)+';'      # list[0] - это Id ученика)
    string += input('Введите Фамилию: ')+';'
    string += input('Введите Имя: ')+';'
    string += input('Введите Класс: ')+';'
    string += input('Введите Статус: ')+';'
    string += input('Введите Ряд: ')+';'
    string += input('Введите Номер парты: ')+';'
    string += input('Введите Город: ') + ';'
    string += input('Введите Улицу: ')+';'
    string += input('Введите Дом: ')+';'
    string += input('Введите Квартира: ')+';'
    string += input('Введите Примечание: ')+';'
    print('Добавляем ученика: ', string)
    push_data(string)
