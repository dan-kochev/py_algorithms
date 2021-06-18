from random import randint

num = randint(0, 100)
print('Отгадайте число от 0 до 100. У вас 10 попыток')
n = 1

while n <= 10:
    ans = int(input('Введите число: '))
    if ans != num:
        if ans > num:
            print('Число должно быть меньше!')
        elif ans < num:
            print('Число должно быть больше!')
        print(f'У вас осталось: {10 - n} попыток')
        n += 1
    else:
        print('Вы отгадали!')
        break

print(f'Правильное число: {num}')
