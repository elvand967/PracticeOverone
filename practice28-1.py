# Практическое задание №28-1
# Написать функцию, которая определяет количество
# разрядов введенного целого числа
def StrNum(str_num):
    return str_num.isdigit()  # проверка Состоит ли строка из цифр

def continuation():
    repeat = input('Продолжить работу (Y/N): ')
    if repeat.upper() == 'Y' or repeat.upper() == 'Н':
        return True
    else:
        return False

while True:
    str_num = input('Введите любое многоразрядное целое число: ')
    digits = 0
    if StrNum(str_num):
        str_num = int(str_num)
        while str_num > 0:
            str_num = str_num // 10
            digits += 1
        print(f'иследуемое число имеет {digits} разряд(ов)')
        if continuation():
            continue
        else: break
    else:
        print('Неверный ввод данных.')
        if continuation():
            continue
        else: break
print('Программа завершила свою работу.')