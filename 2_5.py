num = 1
for i in range(32, 128):
    if num % 10 == 0:
        print(f'{i:4}: {chr(i)}')
    else:
        print(f'{i:4}: {chr(i)}', end=' ')
    num += 1
