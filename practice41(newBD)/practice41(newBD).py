# Практическое задание №41 (newBD)
# Создайте новую Базу данных
# В ней создайте таблицу с тремя полями, два текстовых, одно – целое число
# Число запрашивается с клавиатуры, а слова задаются статически.
# Выведите каждую запись в отдельную строку
import sqlite3
conn = sqlite3.connect('newBD.db')  # Создаём Базу данных
cur = conn.cursor() # Создаем объект cur, который позволяет нам взаимодействовать с базой данных и добавлять записи
cur.execute('''CREATE TABLE IF NOT EXISTS newBD(
idBD INTEGER PRIMARY KEY AUTOINCREMENT,
txt_field1 TEXT,
txt_field2 TEXT,
num_field3 INT)
''')
conn.commit()

num = int(input('Введите номер практического задания: '))
cur.execute('''INSERT INTO newBD(txt_field1, txt_field2, num_field3)
VALUES (?, ?, ?)''',('practical', 'task', num))
conn.commit()

# cur.execute('''SELECT txt_field1 FROM newBD;''')  # создаем запрос 1-го поля
# field = cur.fetchone()
# print(field)
# cur.execute('''SELECT txt_field2 FROM newBD;''')  # создаем запрос 2-го поля
# field = cur.fetchone()
# print(field)
# cur.execute('''SELECT num_field3 FROM newBD;''')  # создаем запрос 3-го поля
# field = cur.fetchone()
# print(field)
cur.execute('''SELECT* FROM newBD;''')  # создаем запрос всех полей
conn.commit()
field = cur.fetchone()
for i in field:
    print(i)
# Введите номер практического задания: 41
# 1
# practical
# task
# 41