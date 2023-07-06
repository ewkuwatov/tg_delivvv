s = int(input('Сколько сувениров вы выбрали: '))
b = int(input('Сколько безделушек вы выбрали: '))

suv = s * 75
bez = b * 112
x = suv + bez

if s > 4:
    print(f'{s} сувениров весит: {suv}г')
elif s > 1:
    print(f'{s} сувенира весит: {suv}г')
else:
    print(f'{s} сувенир равен: 75г')

if b > 1:
    print(f'{b} безделушек весит: {bez}г')
else:
    print(f'{s} безделушка равен: 112г')

print(f'Общий вес равен: {x}г')