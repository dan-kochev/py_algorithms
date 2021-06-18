input_num = input('Введите число: ')
num = int(input_num)
reverse_num = 0

while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num = num // 10

print(str(reverse_num).zfill(len(input_num)))
