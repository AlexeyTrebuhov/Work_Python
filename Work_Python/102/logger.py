from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{}; temperature;{}'
                        .format(time,data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{}; pressure;{}'
                        .format(time,data))

def win_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{}; win_speed;{}'
                        .format(time,data))