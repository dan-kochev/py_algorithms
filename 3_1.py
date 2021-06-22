a = []
for i in range(2, 10):
    b = 0
    for j in range(2, 100):
        if j % i == 0:
            b += 1
    print(f'{i} кратны {b} чисел(-а)')
