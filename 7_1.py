from random import randint


def sort(b):
    n = 1
    while n < len(b):
        for i in range(len(b) - n):
            if b[i] < b[i + 1]:
                b[i], b[i + 1] = b[i + 1], b[i]
        n += 1
    return b


a = [randint(-100, 100) for i in range(20)]
print(a)
print(sort(a))
