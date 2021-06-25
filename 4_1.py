import timeit

# Для анализа использовался алгоритм задания 2.4 "Найти сумму n элементов
# следующего ряда чисел: 1 -0.5 0.25 -0.125 ..."


def sum_n(n):
    num = 1
    sum_num = 0

    for i in range(n):
        sum_num += num
        num /= -2

    return sum_num


number_executions = 100
test_value = 100

time_1 = timeit.timeit(f'sum_n({test_value})',
                       setup='from __main__ import sum_n',
                       number=number_executions)

number_executions = 100
test_value = 200

time_2 = timeit.timeit(f'sum_n({test_value})',
                       setup='from __main__ import sum_n',
                       number=number_executions)

number_executions = 100
test_value = 300

time_3 = timeit.timeit(f'sum_n({test_value})',
                       setup='from __main__ import sum_n',
                       number=number_executions)

print(f'Количество элементов и время на их сумму: \n100: {time_1:.6f} '
      f'\n200: {time_2:.6f} \n300: {time_3:.6f}')

# В результате получены следующие данные:
# Для суммы ста элементов потребуется времени: 0.000661
# Для двухсот элементов: 0.001238
# Для трехсот: 0.001886

# Алгоритм имеет линейную сложность O(N), поскольку число действий, которые
# должна совершить программа, зависит от того, сколько именно чисел в нее
# передали.

# С увеличением числа элементов время на исполнение алгоритма растет
# непропорционально, поскольку чем больше n, тем меньше меняется сумма от
# прибавления каждого следующего элемента, т.к. на каждой итерации цикла
# значение элемента уменьшается в два раза (по модулю), т.е. прибавляется
# все меньшая и меньшая величина.
