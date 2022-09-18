# Практическое задание №29-2
# Калькулятор.
# Создайте класс, где реализованы функции(методы)
# математических операций.
# А также функция, для ввод данных.
import math

class Calculator():
    def __init__(self): # метод инициализации экземпляров класса после их создания
        self.set_me() # метод ввода mathematical expression (математическое выражение)

    def c_sum(self,a,b):
        self.x = a + b
        return print(self.x)

    def c_sub(self,a,b):
        self.x = a - b
        return print(self.x)

    def c_mult(self, a, b):
        self.x = a * b
        return print(self.x)

    def c_div(self, a, b):
        self.x = a / b
        return print(self.x)

    def set_me(self):
        self.me = input('Введите математическое выражение:_')
        import re
        self.me = self.me.replace('+',' + ') # в случае ввода мат.оператора без пробела, обвернем его пробелом
        self.me = self.me.replace('-', ' - ')
        self.me = self.me.replace('*', ' * ')
        self.me = self.me.replace('/', ' / ')
        #self.me = self.me.replace('**', ' ** ') # -???
        self.me_list = re.split('\s+', self.me)
        self.a = None
        self.b = None
        for i in self.me_list:
            if i.isdigit():
                if self.a is None:
                    self.a = float(i)
                else:
                    self.b = float(i)
                    break
            else: self.mathematical_operator = i

    def result(self):
        if self.mathematical_operator == '+':
            self.c_sum(self.a,self.b)
        if self.mathematical_operator == '-':
            self.c_sub(self.a,self.b)
        if self.mathematical_operator == '*':
            self.c_mult(self.a,self.b)
        if self.mathematical_operator == '/':
            self.c_div(self.a,self.b)

def continuation():
    repeat = input('Продолжить работу (Y/N): ')
    if repeat.upper() == 'Y' or repeat.upper() == 'Н':
        return True
    else:
        return False

while True:
    Cal = Calculator()
    Cal.result()
    if not continuation(): break

print('Программа завершила свою работу.')