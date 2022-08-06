# Практическое задание №02-1 Казино (мой вариант решения)
# Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный)
# Пользователю дается 5 попыток угадать номер и цвет
# (Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.
import random
i = n = c = num = col = 0
color = yn = ''
while i < 5:
    i += 1
    print('Bet №', i)
    n = int(input('Укажите число (от 1 до 10):'))
    c = int(input('Выберите цвет (1 - красный; 2 - черный):'))
    num = random.randint(1,10)
    col = num%2 +1 # все четные числа - красный, не четные - черный
    if col == 1:
        color = 'Red (красный)'
    else:color = 'Black (черный)'
    print('*'*20)
    print(f'Bet to play (сыграла ставка): {num} {color}')
    if n == num and c == col:
        print('!'+('-!'*20))
        print(':) Congratulations! Your bets "', n, '" have won!\n(Поздравляем! Ваши ставки "', n, color, '" выйграли!)')
        print('!'+('-!'*20))
    elif n == num and c != col:
        print(f':) Congratulations! Your bet " {n} " won!\n(Поздравляем! Ваша ставка " {n}  " выйграла!)')
    elif c == col and n!= num:
        print(f':) Congratulations! Your bet "{color}" won!\n(Поздравляем! Ваша ставка "{color}" выйграла!)')
    else: print(':( Your bets are wrong! (Ваши ставки неудачны!)')
    if i < 5:
        yn = input('Желаете продолжить (Y/N):')
        if yn == 'Y' or yn == 'y':
            print('Продолжаем!')
        else:
            i += 5 # условие завершения основного цикла "while i < 5"
else: print('Good luck!\nВсего хорошего!\nGame over')