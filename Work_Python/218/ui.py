from re import A


def initial():
    a = input('Введите фамилию: ')
    b = input('Введите имя: ')
    c = input('Введите телефон: ')
    d = input('Введите комментарий: ')
    a1 = ('Фамилия')
    b1 = ('Имя')
    c1 = ('Телефон')
    d1 = ('Комментарий')
  
    operation = input("Как вносить данные : в строчку (+), или столбик (-) ? ")
    return [operation,a,b,c,d,a1,b1,c1,d1]