# Практическое задание №03-1 'Список из 7 цифр' (мой вариант решения)
# Список из 7 цифр
# Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 элемента
from random import randint
# создаем список из 7 элементов, с случайными числами от 0 до 100 при помощи генератора списков
OddNumbers = 0
EvenNumbers = 0
mylist = [randint(0,100) for i in range(7)]
print('Исходный список: ',mylist)
for i in mylist:
    if i%2: OddNumbers += 1
    else: EvenNumbers += 1
if EvenNumbers < OddNumbers:
    print('Четных чисел: ',EvenNumbers)
else:print('Нечетных чисел: ',OddNumbers)