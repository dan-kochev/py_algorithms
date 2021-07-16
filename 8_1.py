import hashlib

s = input(f'Введите строку: ')
n = len(s)
r = set()

for i in range(n):
    if i == 0:
        n = len(s) - 1
    else:
        n = len(s)
    for j in range(n, i, -1):
        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

print(f'Количество подстрок: {len(r)}')
