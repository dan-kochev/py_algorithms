from random import randint

a = [randint(0, 300) for i in range(100)]

num = 0
max_i = 0
for i in a:
    if a.count(i) > max_i:
        max_i = a.count(i)
        num = i

print(f'Чаще всего встречается {num}, а именно {max_i} раза')
