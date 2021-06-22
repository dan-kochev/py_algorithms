from random import randint

a = [randint(-300, 300) for i in range(20)]
print(f'Массив: {a}')

num_index = -1
for i in a:
    if i < 0 and num_index == -1:
        num_index = a.index(i)
    elif 0 > i > a[num_index]:
        num_index = a.index(i)

print(f'Максимальный минимальный элемент:{a[num_index]} с индексом:{num_index}')
