lid = {'Посетители': {7: 'Mirshod',
                      1 :'Temur',
                      5: 'Kamran'}}

def add_lid():
    lid_name = input('Введите имя: ')
    room_numb = int(input('Введите номер комнаты: '))
    if room_numb in lid['Посетители']:
        print('Комната занята. Пожалуйста введите другой номер ')
        room_numb1 = int(input('Введите номер комнаты: '))
        if room_numb1 in lid['Посетители']:
            print('Слишком много попыток!')
        else:
            lid['Посетители'][room_numb1] = lid_name
            print('Клиент успешно добавлен!')
    else:
        lid['Посетители'][room_numb] = lid_name
        print('Клиент успешно добавлен!')

def del_lid():
    lid_name = input('Введите имя: ')
    room_numb = int(input('Введите номер комнаты: '))
    if room_numb in lid['Посетители'] and lid['Посетители'][room_numb] == lid_name:
        lid['Посетители'].pop(room_numb)
        print('Комната свободна!')
    else:
        print('Вы не правильно ввели номкр комнаты или имя клиента. Пожалуйста введите заново.')
        lid_name2 = input('Введите имя: ')
        room_numb2 = int(input('Введите номер комнаты: '))
        if room_numb2 in lid['Посетители'] and lid['Посетители'][room_numb2] == lid_name2:
            lid['Посетители'].pop(room_numb2)
            print('Комната свободна!')
        else:
            print('Вы не правильно ввели номeр комнаты или имя клиента. Пожалуйста введите заново.')

def rooms():
    print(lid)

while True:
    hotel = input('Выберите услугу:\n' + \
                '"1" Добавить клиента\n' + \
                '"2" Удалить клиента\n' + \
                '"3" Увидеть занятые номера\n' + \
                'Ввести здесь ------->: ')
    if hotel == '1':
        add_lid()
    elif hotel == '2':
        del_lid()
    elif hotel == '3':
        rooms()
    else:
        print('Неверный ввод!')



