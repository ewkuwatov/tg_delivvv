all_products = {'Весь склад': { 'Картошка': 200,
                                'Помидор': 200}}
korzinka = []

while True:
    admin = input('Что хотите сделать:\n' + \
                  'добавить\n' + \
                  'продукты\n' + \
                  'купить\n' + \
                  '------> ')
    if admin.lower() == 'добавить':
        products = input('Введите продукт: ')
        products_count = int(input('Введите количество: '))
        if products in all_products['Весь склад']:
            x = all_products['Весь склад'][products]
            plus = x + products_count
            all_products['Весь склад'][products] = plus
        else:
            all_products['Весь склад'][products] = products_count
        print('Done')
    elif admin.lower() == 'продукты':
        print(all_products)
    elif admin.lower() == 'купить':
        products2 = input('Введите продукт: ')
        products_count2 = int(input('Введите количество: '))
        if products2 in all_products['Весь склад'] and products_count2 < all_products['Весь склад'][products2]:
            korzinka.append(products2)
            y = all_products['Весь склад'][products2]
            minus = y - products_count2
            all_products['Весь склад'][products2] = minus
            print(korzinka)
            if all_products['Весь склад'][products2] == 0:
                all_products['Весь склад'].pop(products2)
        else:
            print('Такого продукта нет на складе или нет нужного количества продукта.')
