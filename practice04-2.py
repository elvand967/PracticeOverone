# Практическое задание №04-2 'Кортежи' (вариант Overone)
# Создайте кортеж из случайных 10 чисел.
# Найдите индексы максимального и
# минимального элемента
import random
a = [random.randint(1,100) for i in range(10)]
a = tuple(a)
print(a)
print(a.index(min(a)),a.index(max(a)))