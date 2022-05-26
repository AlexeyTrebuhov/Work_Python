import names
import ui
import log


def run():
    temp = ui.initial()

    if '-' in temp[0]:
        result = ('В строчку')
    if '+' in temp[0]:
        result = ('В столбик')

    del temp[0]
    log.log_to_file(result, temp)
    return result
