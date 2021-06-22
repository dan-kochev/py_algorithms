from random import randint

a = [randint(-300, 300) for i in range(20)]
print(a)

max_idx = a.index(max(a))
min_idx = a.index(min(a))
a[max_idx], a[min_idx] = a[min_idx], a[max_idx]
print(a)
