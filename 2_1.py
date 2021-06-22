while True:
    num_1 = int(input('Первое число: '))
    num_2 = int(input('Второе число: '))
    sign = input('Знак: ')
    if sign == '+':
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
    elif sign == '-':
        print(f'{num_1} - {num_2} = {num_1 - num_2}')
    elif sign == '*':
        print(f'{num_1} * {num_2} = {num_1 * num_2}')
    elif sign == '/':
        if num_2 != 0:
            print(f'{num_1} / {num_2} = {num_1 / num_2}')
        else:
            print(f'На ноль делить нельзя!')
    elif sign == '0':
        break
    else:
        print(f'Неверный знак, попробуйте еще раз!')
