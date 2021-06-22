from random import randint

a = [randint(-10, 10) for i in range(5)]
print(f'Массив: {a}')

max_idx = a.index(max(a))
min_idx = a.index(min(a))
sum_num = 0

if max_idx > min_idx:
    for i in a[min_idx + 1: max_idx: 1]:
        sum_num += i
else:
    for i in a[max_idx + 1: min_idx: 1]:
        sum_num += i
print(f'Сумма между элементами равна: {sum_num}')
