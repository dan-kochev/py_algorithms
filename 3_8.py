a = []

for i in range(4):
    b = []
    sum_num = 0
    for j in range(4):
        num = int(input(f'Введите элемент i = {i + 1}, j = {j + 1}: '))
        sum_num += num
        b.append(num)
    b.append(sum_num)
    a.append(b)

for i in a:
    for j in i:
        print(f'{j:{4}}', end=' ')
    print()
