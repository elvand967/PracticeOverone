# Практическое задание №01/1
# Удалить букву из строки, ввод с клавиатуры
s = input('Введите строку: ')
l = input('Введите букву которую нужно удалить: ')
c =''
for i in s:
    if i == l:
        continue
    c += i
print(c)