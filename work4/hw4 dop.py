bottle1 = int(input('Сколько литровых бутылок у вас имеется: '))
bottle2 = int(input('Сколько 2 литровыхе бутылок у вас имеется: '))

bot1 = bottle1 * 0.10
bot2 = bottle2 * 0.25
x = bot1 + bot2

print(f'за литровых вы получите $ {bot1}')
print(f'за 2 литровых вы получите $ {bot2}')
print(f'Общ: $ {x}')
