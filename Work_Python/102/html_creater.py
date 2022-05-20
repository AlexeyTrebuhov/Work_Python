from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def create(device = 1):
    style = 'stule="font-size:22px;"'
    html = '<html>\n <head></head>\n <body\n'
    html +=  '    <p {}>temperature:{} c</p>\n'\
            .format(style,temperature_view(device))
    html +=  '    <p {}>wind_speed:{} c</p>\n'\
            .format(style,wind_speed_view(device))
    html +=  '    <p {}>pressure:{} c</p>\n'\
            .format(style,pressure_view(device))
    html +=  '     </body>\n<html>'

    with open('D:\\Обучение\\Работа в Git\\Work_Python\\102\\index.html', 'w') as page:
        page.write(html)

    return html

def new_create(data, device=1):
    t, p, w =   data  
    style = 'stule="font-size:22px;"'
    html = '<html>\n <head></head>\n <body\n'
    html += '    <p {}>temperature:{} c</p>\n'\
            .format(style, t)
    html += '    <p {}>wind_speed:{} c</p>\n'\
            .format(style, w)
    html += '    <p {}>pressure:{} c</p>\n'\
            .format(style, p)
    html += '     </body>\n<html>'

    with open('D:\\Обучение\\Работа в Git\\Work_Python\\102\\new_index.html', 'w') as page:
        page.write(html)

    return data
