summa = int(input('Введите сумму заказа: '))

# расчет налога равен 1%'
# чаевые офицанту равен 18%

nal = summa * 0.010
chaev = summa * 0.180
sum = summa + nal + chaev

print(f'Налоговый расчет равен: {nal}')
print(f'Чаевые офицанту:{chaev}')
print(f'Общий счет заказа: {sum}')