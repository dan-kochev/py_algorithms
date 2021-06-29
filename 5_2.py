from collections import defaultdict
from collections import deque


def dex_1(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def hex_1(num_b):
    num = deque()
    while num_b > 0:
        a = num_b % 16
        for i in table:
            if table[i] == a:
                num.append(i)
        num_b //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = dex_1(input('Введите первое число:\n ').upper())
num_2 = dex_1(input('Введите второе число :\n ').upper())

print(f'Сумма чисел: {hex_1(num_1 + num_2)}')
print(f'Произведение чисел: {hex_1(num_1 * num_2)}')
