amount = int(input('Чисел в последовательности: '))
num = int(input('Искомое число: '))
sum_num = 0

for i in range(1, amount + 1):
    i_num = int(input(f'{i}-е число: '))
    while i_num > 0:
        if i_num % 10 == num:
            sum_num += 1
        i_num //= 10

print(f'Цифра {num} встречается {sum_num} раз(а)')
