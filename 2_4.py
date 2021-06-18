n = int(input('Количество элементов: '))
num = 1
sum_num = 0

for i in range(n):
    sum_num += num
    num /= -2

print(sum_num)
