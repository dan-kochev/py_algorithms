def left(n):
    if n == 1:
        return n
    elif n > 0:
        return n + left(n - 1)


def right(n):
    return n * (n + 1) // 2


num = int(input('Введите n: '))
print(f'Левая часть равенства равна: {left(num)}')
print(f'Правая часть равенства равна: {left(num)}')
