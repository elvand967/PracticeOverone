# Практическое задание №29-2
# Калькулятор.
# Создайте класс, где реализованы функции(методы)
# математических операций.
# А также функция, для ввод данных.
import math

class Calculator():
    def __init__(self): # метод инициализации экземпляров класса после их создания
        self.set_me() # метод ввода mathematical expression (математическое выражение)

    def c_sum(self):
        return print(float(self.me_list[0]) + float(self.me_list[2]))

    def c_sub(self):
        return print(float(self.me_list[0]) - float(self.me_list[2]))

    def c_mult(self):
        return  print(float(self.me_list[0]) * float(self.me_list[2]))

    def c_div(self):
        if float(self.me_list[2]) == 0.0:
            return print('недопустимая операция: деление на "0"')
        return  print(float(self.me_list[0]) / float(self.me_list[2]))

    def set_me(self):
        self.me = input('Введите математическое выражение: ')
        import re
        self.me = self.me.replace('+',' + ') # в случае ввода мат.оператора без пробела, обвернем его пробелом
        self.me = self.me.replace('-', ' - ')
        self.me = self.me.replace('*', ' * ')
        self.me = self.me.replace('/', ' / ')
        #self.me = self.me.replace('**', ' ** ') # -???
        self.me_list = re.split('\s+', self.me)
        self.mathematical_operator = self.me_list[1]

    def result(self):
        if self.mathematical_operator == '+':
            self.c_sum()
        if self.mathematical_operator == '-':
            self.c_sub()
        if self.mathematical_operator == '*':
            self.c_mult()
        if self.mathematical_operator == '/':
            self.c_div()

def continuation():
    repeat = input('Продолжить работу (Y/N): ')
    if repeat.upper() == 'Y' or repeat.upper() == 'Н':
        return True
    else:
        return False

while True:
    Cal = Calculator()
    #print(Cal.result())
    Cal.result()
    if not continuation(): break

print('Программа завершила свою работу.')