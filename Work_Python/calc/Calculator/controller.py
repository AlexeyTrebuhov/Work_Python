import calc_complex
import calc_float
import ui
import log


def run():
    temp = ui.initial()
    if 'j' in temp[0] and 'j' in temp[1]:
        result = calc_complex.calc(temp[0], temp[1], temp[2])
    else:
        result = calc_float.calc(temp[0], temp[1], temp[2])
    print(result,'sss')
    
    log.log_to_file(temp, result)
    return result
