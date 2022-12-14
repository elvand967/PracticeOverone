# Практическое задание №07  (Overone)
# 1. Создать множество
# 2. Создать неизменяемое множество
# 3. Выполнить операцию объединения созданных множеств
# 4. Выполнить операцию пересечения созданных множеств

# Единственное отличие set от frozenset заключается в том, что set - изменяемый тип данных, а frozenset - нет.
a = {1,3,4,2,8,3}     # изменяемый тип данных
b = frozenset([2,17,3,4,9,5]) # неизменяемый тип данных

# операции объединения созданных множеств
c = a|b
print(a.union(b))
print(c)

# операции пересечения созданных множеств
print(a&b)
print(a.intersection(b))

for i in b:
    print(i)