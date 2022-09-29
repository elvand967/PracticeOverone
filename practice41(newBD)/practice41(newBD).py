# Практическое задание №41 (newBD)
# Создайте новую Базу данных
# В ней создайте таблицу с тремя полями, два текстовых, одно – целое число
# Число запрашивается с клавиатуры, а слова задаются статически.
# Выведите каждую запись в отдельную строку
import sqlite3

num = int(input('Введите номер практического задания: '))
conn = sqlite3.connect('new_BD.db')  # Создаём/подключаем Базу данных
cur = conn.cursor() # Создаем объект cur, который позволяет нам взаимодействовать с базой данных и добавлять записи
cur.execute('''CREATE TABLE IF NOT EXISTS new_tablBD(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
txt_field1 TEXT, 
txt_field2 TEXT, 
num_field3 INT)''')
cur.execute('''INSERT INTO new_tablBD(txt_field1, txt_field2, num_field3)
VALUES ('practical', 'task', ?)''',(num,))
conn.commit()
cur.execute('''SELECT* FROM new_tablBD''')  # создаем запрос всех полей
field = cur.fetchall()
print(field)

