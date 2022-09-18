# Практическое задание №29-1 (overone)
# Создайте класс Example. В нём пропишите 3 (метода) функции. Две переменные
# задайте статически, две динамически.
# ❖ Первая функция: создайте переменную и выведите её
# ❖ Вторая функция: верните сумму 2-ух глобальных переменных
# ❖ Третья функция: верните результат возведения первой динамической
# переменной во вторую динамическую переменную
# ❖ Создайте объект класса.
# ❖ Напечатайте обе функции
# ❖ Напечатайте переменную a

class TheExample:
    a = 2
    b = 3

    def __init__(self, t, r):
        self.t = t
        self.r = r

    def func(self):
        self.c = 5
        print(self.c)

    def func1(self):
        return self.a + self.b

    def func2(self):
        return self.t**self.r


example = TheExample(4,2)

print(example.a)
print(example.func1())
print(example.func2())
example.func()