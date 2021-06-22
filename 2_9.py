from random import randint


def sum_numbers(a):
    sum_num = 0
    a = str(a)
    for y in a:
        sum_num += int(y)
    return sum_num


max_num = 0
max_sum = 0

for i in range(1, 11):
    num = randint(1, 1000)
    n = sum_numbers(num)
    if n > max_sum:
        max_sum = n
        max_num = num

print(f'Максимальная сумма: {max_sum} у числа: {max_num}')
