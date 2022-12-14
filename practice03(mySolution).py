# Практическое задание №03 'Список из 7 цифр' (мой вариант решения)
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
if EvenNumbers > OddNumbers:
    print(f'Четных чисел больше: {EvenNumbers}; сумма всех чисел списка {sum(mylist)} ')
else:print(f'Нечетных чисел больше: {OddNumbers}; '
           f'произведение 1 3 и 6 элемента = {mylist[0]*mylist[2]*mylist[5]}')

# Исходный список:  [6, 6, 49, 25, 85, 5, 67]
# Нечетных чисел больше: 5; произведение 1 3 и 6 элемента = 1470