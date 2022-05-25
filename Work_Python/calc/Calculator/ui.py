from re import A


def initial():
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    operation = input("Введите операцию ( + , - , / , *): ")
    return [a, b, operation]
