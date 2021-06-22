from random import randint

a = [randint(0, 30) for i in range(10)]
print(a)

b = []
for i in a:
    if i % 2 == 0:
        b.append(a.index(i))

print(b)
