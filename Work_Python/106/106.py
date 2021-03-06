# Создайте программу для игры в "Крестики-нолики".
# Игра начинается с хода компьютера, который ставит нолики

import random
from tkinter import *
import os
os.system("cls")

root = Tk()         # делаем окно с заголовком
root.title('Почти Рэндзю')

game_run = True     # если будет победитель, будет False
field = []          # в массиве храним состояние поля
cross_count = 0     # Подсчитываем количество крестиков на поле, максимально 5


def new_game():     # поле и переменные обнуляются
    for row in range(17):
        for col in range(17):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0
    field[8][8]['text'] = 'O'
    field[8][8]['background'] = '#FCA25B'


def click(row, col):        # ставим крестик и считаем
    # если поле пустое можем поставить Х и поменять цвет
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        field[row][col]['background'] = '#7CF5E9'
        global cross_count
        cross_count += 1
        field[15][20]['text'] = cross_count
        check_win('X')   # проверка на победу по символу Х
        if game_run and cross_count < 289:
            computer_move()  # если поле не заполнено, ходит комп
            check_win('O')  # проверка на победу по символу О

# проверка победы по всем направлениям


def check_win(smb):
    for n in range(17):
        for m in range(14):
            check_line(field[n][m], field[n][m+1],
                       field[n][m+2], field[n][m+3], smb)
            check_line(field[m][n], field[m+1][n],
                       field[m+2][n], field[m+3][n], smb)

            check_line(field[m][n], field[m+1][n+1],
                       field[m+2][n+2], field[m+3][n+3], smb)
    for n in range(14):
        for m in range(14):

            check_line(field[m+3][n], field[m+2][n+1],
                       field[m+1][n+2], field[m][n+3], smb)

# на входе четыре поля и символ, если символ есть в этих четырех полях,
# то меняем цвет полей на другой ( их палитры цветов) и остановка игры


def check_line(a1, a2, a3, a4, smb):  # Меняется цвет выигрышных кнопок
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = a4['background'] = '#605BFC'
        global game_run
        game_run = False


def can_win(a1, a2, a3, a4, smb):   # проверка на победу
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == ' ':
        a4['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ' and a4['text'] == smb:
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb and a4['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


def computer_move():
    for n in range(17):
        if can_win(field[n][0], field[n][1], field[n][2], field[n][3], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], field[3][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], field[3][3], 'O'):
        return
    if can_win(field[3][0], field[2][1], field[1][2], field[0][3], 'O'):
        return

    while True:  # случайным образом перебираются поля, пока не выпадет свободное
        row = random.randint(0, 16)
        col = random.randint(0, 16)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            field[row][col]['background'] = '#FCA25B'
            break


for row in range(17):  # создаем поле кнопок
    line = []
    for col in range(21):
        button = Button(text=' ', width=6, height=3,
                        font=('Verdana', 7, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
field[8][8]['text'] = 'O'
field[8][8]['background'] = '#FCA25B'


new_button = Button(text='Новая игра', font=(
    'times', 12, 'bold'), background='#FAE237', command=new_game)
new_button.grid(row=16, column=17, columnspan=15, sticky='nsew')

text_button = Button(text='Правила игры', font=(
    'times', 14, 'bold'), background='#9CD8F0')
text_button.grid(row=0, rowspan=2, column=17, columnspan=4, sticky='nsew')

text_button = Button(text='Не дайте компьютеру \n поставить четыре фишки \nв ряд или \n по диагонали\n\n Вы тоже не имеете\n права ставить в один ряд \n больше четырех фишек\n\nВаш ход', font=(
    'times', 12, 'bold'), background='#9CD8F0')
text_button.grid(row=2, rowspan=4, column=17, columnspan=4, sticky='nsew')

text_button = Button(text='', font=(
    'times', 12, 'bold'), background='#9CD8F0')
text_button.grid(row=6, rowspan=9, column=17, columnspan=4, sticky='nsew')

text_button = Button(text='Номер хода', font=(
    'times', 12, 'bold'), background='#9CD8F0')
text_button.grid(row=15, rowspan=1, column=17, columnspan=3, sticky='nsew')

root.mainloop()
