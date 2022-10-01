# Практическое задание №42-1 (BDnumber4)
# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества записей в БД, то
# удалите четвёртую запись БД
import sqlite3
import random
conn = sqlite3.connect('BDnumber4.db')    # Создаём/подключаем Базу данных
cur = conn.cursor() # создаем курсор к подключенной БД conn
# в БД создаем таблицу tabl1, с полем автоиндекса и 2-мя полями(колонками) типом INT (Целочисленные)
cur.execute('''CREATE TABLE IF NOT EXISTS tabl1(
id INTEGER PRIMARY KEY AUTOINCREMENT,
col01 INTEGER,
col02 INTEGER) ''')
conn.commit() # зафиксируем нашу таблицу
# numberRecords = 10 # допустимое количество записей в таблице
# cur.execute('''SELECT Count(*) FROM tabl1''') # запрос количества записей в таблице
# field = cur.fetchone() # fetchone() – возвращает первую запись для запроса Count(*) - кол-во записей в таблице
# numberRecords -= field[0]
# for i in range(numberRecords):
for i in range(4):
    a = random.randint(0,9)
    b = random.randint(0,9)
    cur.execute('''INSERT INTO tabl1(col01,col02) VALUES (?, ?)''',(a,b))
conn.commit() # зафиксируем

cur.execute('''SELECT col01,col02 FROM tabl1''') # запрос записей в таблице
field = cur.fetchall() # fetchall() – возвращает число записей в виде упорядоченного списка
print(field)

sum_field = 0
for i in field:
    sum_field += sum(i)
average = sum_field/(len(field)*2) # среднее арифметическое всех элементов без учёта id
if  average > len(field):
    cur.execute(f'''DELETE FROM tabl1 WHERE col01 = {field[3][0]} AND col02 = {field[3][1]}''')
    conn.commit()  # зафиксируем
    #print(f'WHERE col01 = {field[3][0]} AND col02 = {field[3][1]}')
    print(f'сумма всех({len(field)*2}) элементов кортежей списка = {sum_field}\n'
          f'среднее арифметическое всех элементов без учёта id:  {average} ')
    cur.execute('''SELECT col01,col02 FROM tabl1''') # запрос записей в таблице
    field = cur.fetchall() # fetchall() – возвращает число записей в виде упорядоченного списка
else:
    print(f'среднее арифметическое {average} не больше количества записей ({len(field)}) в БД')

print(field)
cur.execute('''DELETE FROM tabl1''')
conn.commit() # зафиксируем
# [(5, 1), (0, 1), (4, 2), (8, 5)]
# среднее арифметическое 3.25 не больше количества записей (4) в БД
# [(5, 1), (0, 1), (4, 2), (8, 5)]

# [(4, 3), (3, 8), (6, 8), (9, 8)]
# сумма всех(8) элементов кортежей списка = 49
# среднее арифметическое всех элементов без учёта id:  6.125
# [(4, 3), (3, 8), (6, 8)]