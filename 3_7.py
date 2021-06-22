from random import randint

a = [randint(0, 100) for i in range(10)]
print(f'Массив: {a}')

b = a[:]
min_1 = min(b)
b.remove(min_1)
min_2 = (min(b))
print(f'Два наименьших элемента: {min_1}, {min_2}')
