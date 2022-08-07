# Практическое задание №04-1 'Кортежи' (мой вариант решения)
# Создайте кортеж из случайных 10 чисел.
# Найдите индексы максимального и
# минимального элемента
import random
mytuple = [random.randint(0,100) for i in range(10)]
print(mytuple)
print(f'индекс min значения "{min(mytuple)}": [{mytuple.index(min(mytuple))}],\n'
      f'индекс max значения "{max(mytuple)}": [{mytuple.index(max(mytuple))}]')