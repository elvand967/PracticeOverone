# Практическое задание №02-2 Казино (Overone вариант решения)
# Казино. Числа от 1 до 10 и цвета от 1 до 2( 1 - красный, 2 - чёрный). У пользователя 5 попыток
import random
a = random.randint(1,10)
b = random.randint(1,2)
i = 0
while i<5:
    i = i + 1# i +=1
    c = int(input("Введите число от 1 до 10: "))
    d = int(input("Введите цвет от 1 до 2 ( 1 - красный, 2 - чёрный): "))
    if a ==c and b ==d:
        print(f'Вы угадали цвет и число: {c}{d}')
        break
    elif a!=c and b == d:
        print(f'Вы не угадали число: {a}, но угадали цвет: {b}')
    elif a ==c and b !=d:
        print(f'Вы не угадали цвет: {b},  но угадали число: {a} ')
    else:
        print(f'Вы не угадали цвет и число: {a}{b}. Попробуйте ещё раз')
else:
    print(f'Вы не угадали цвет и число: {a}{b}. Ваши попытки закончились')