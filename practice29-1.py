# Практическое задание №29-1
# Создайте класс Example. В нём пропишите 3 (метода) функции. Две переменные
# задайте статически, две динамически.
# ❖ Первая функция: создайте переменную и выведите её
# ❖ Вторая функция: верните сумму 2-ух глобальных переменных
# ❖ Третья функция: верните результат возведения первой динамической
# переменной во вторую динамическую переменную
# ❖ Создайте объект класса.
# ❖ Напечатайте обе функции
# ❖ Напечатайте переменную a

class Example(): # перевод - пример
    a = 2  # статистическая переменная
    b = 3  # статистическая переменная
    def __init__(self,c, d): # метод инициализации экземпляров класса после их создания
        self.c = c # динамическая переменная
        self.d = d # динамическая переменная
    def method1(self, x = a):
        return x

    def method2(self,a = a, b = b):
        return a+b

    def method3(self):
        return self.c**self.d
Ex = Example(7, 9)

print(Ex.method1())
print(Ex.method1(8))
print(Ex.method2())
print(Ex.method2(8,4))
print(Ex.method3())
