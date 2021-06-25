import math
import timeit

# Нахождение простого числа без использования Решета Эратосфена


def prime_num(i):
    prime_1 = [2]
    num = 3
    while len(prime_1) < i:
        flag = True
        for j in prime_1.copy():
            if num % j == 0:
                flag = False
                break
        if flag:
            prime_1.append(num)
        num += 1
    return prime_1[-1]

# Нахождение простого числа с использованием Решета Эратосфена


def prime_num_er(i):
    i_max = prime_counting_num(i)
    prime_1 = [_ for _ in range(2, i_max)]

    for num in prime_1:
        if prime_1.index(num) <= num - 1:
            for j in range(2, len(prime_1)):
                if num * j in prime_1[num:]:
                    prime_1.remove(num * j)
        else:
            break
    return prime_1[i - 1]

# Верхняя граница отрезка, на которой лежат i-е количество простых чисел


def prime_counting_num(i):
    primes = 0
    number = 2
    while primes <= i:
        primes = number / math.log(number)
        number += 1
    return number


number_executions = 1
test_value = 1000

time_1 = timeit.timeit(f'prime_num({test_value})',
                       setup='from __main__ import prime_num',
                       number=number_executions)

time_2 = timeit.timeit(f'prime_num_er({test_value})',
                       setup='from __main__ import prime_num_er',
                       number=number_executions)

print(f'Программа без использования алгоритма Решета Эратосфена быстрее \
программы с использованием алгоритма «Решето Эратосфена» в \
{round(time_2 / time_1, 2)} раз')

# Программа без использования алгоритма Решета Эратосфена быстрее
# программы с использованием алгоритма Решета Эратосфена в 90.06 раз
