# Практическое задание №06-2  (Overone)
# У вас есть словарь, где ключ – название продукта.
# Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во.
# n – выход из программы.
# Посчитать цену выбранных товаров
# и сколько товаров осталось в изначальном списке.
goods = {"Apple": [4.5, 10],
         "Orange": [6.2, 5],
         "Pineapple": [10.0, 1],
         "Mango": [7.5, 2],
         "Banana": [3.8, 10]}

for key,value in goods.items():
    print(key, '-', value[0], '-', value[1])

cost = 0
while True:
    good = input("Введите товар, который хотите купить или введите n для выхода")
    if good=='n' or good not in goods:
        break
    qty = int(input("Сколько Вы хотите купить?"))
    if qty>goods[good][1]:
        print("У нас столько нет, выберите другое количество или товар")
        continue
    cost = cost + (qty * goods[good][0])
    goods[good][1] -= qty

print(f"Вам надо заплатить {cost} р.")

for key,value in goods.items():
    print(key, '-', value[0], '-', value[1])