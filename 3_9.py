from random import randint

a = []
for i in range(5):
    a.append([])
    a[i].extend([randint(0, 50) for j in range(5)])

for i in a:
    for j in i:
        print(f'{j:{3}}', end=' ')
    print()

mx = -1
for j in range(5):
    mn = 50
    for i in range(5):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print(f'Максимальный элемент среди минимальных: {mx}')
