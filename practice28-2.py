# Практическое задание №28-2
# В зависимости от выбора пользователя вычислить площадь круга,
# прямоугольника или треугольника. Для вычисления площади
# каждой фигуры должна быть написана отдельная функция
import math

def area_circle(r): # для расчета площ. круга фун-ция принимает его радиус
    return round(math.pi * r ** 2, 2)
def area_rectangle(figure_list):# для расчета площ. прямоугольника
    # фун-ция принимает список(его ширину и высоту)
    return round(float(figure_list[0]) * float(figure_list[1]), 2)
def area_triangle(figure_list):# для расчета площ. треугольника фун-ция принимает
    # список с размерами 3-х сторон
    p = (float(figure_list[0]) + float(figure_list[1]) + float(figure_list[2]))/2
    # полупериметр треугольника (для метода Герона)
    return round(math.sqrt(p * (p-float(figure_list[0])) *
                           (p-float(figure_list[1])) * (p-float(figure_list[2]))), 2)

def continuation():
    repeat = input('Продолжить работу (Y/N): ')
    if repeat.upper() == 'Y' or repeat.upper() == 'Н':
        return True
    else:
        return False

while True:
    choice = int(input('Для расчета площади:\n'
                       '"круга" - введите цифру "1"\n'
                       '"прямоугольника" - введите цифру "2"\n'
                       '"треугольника" - введите цифру "3"\n'
                       'Сделайте свой выбор: '))

    if choice == 1:
        print(f'Площадь круга: {area_circle(int(input("Введите радиус круга: ")))} кв.единиц')
    elif  choice == 2:
        rectangle = input('Через пробел введите высоту и ширину прямоугольника: ')
        figure_list = rectangle.split(' ')
        print(f'Площадь прямоугольника {area_rectangle(figure_list)} кв.единиц')
    elif  choice == 3:
        triangle = input('Через пробел введите длины сторон треугольника: ')
        figure_list = triangle.split(' ')
        print(f'Площадь треугольника {area_triangle(figure_list)} кв.единиц')
    else:
        print('Неверный ввод данных.')
        if continuation():
            continue
        else:
            break

    if not continuation():
        break
print('Программа завершила свою работу.')