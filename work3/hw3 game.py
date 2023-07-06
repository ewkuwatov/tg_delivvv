import random

while True:

    point = int(input('Выберите число: '))
    comp_point = random.randint(1, 2)

    if point > comp_point:
        print('Вы не угадали! Ваше число больше, чем задумал компьютер')
    elif point < comp_point:
        print('Вы не угадали! Ваше число меньше, чем задумал компьютер')
    else:
        print('Вы угадали')

