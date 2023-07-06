change_list = input('Выберите услугу:\n' + \
                    'Введите "1" если хотите добавить контакт\n' + \
                    'Введите "2" если хотите изменить контакт\n' + \
                    'Введите "3" если хотите удалить контакт\n' + \
                    'Ввести здесь ------->: ')

name_user = ['Temur', 'Kamran', 'Mirshod']


if change_list == '1':
    name_user.append(input('Введите имя который хотите добавить: '))
    print(name_user)
elif change_list == '2':
    print(name_user)
    default_name = input('Напишите имя которое хотите изменить: ')
    change = name_user.index(default_name)
    new_name = input('Введите новое имя: ')
    name_user[change] = new_name
    print(name_user) 
elif change_list == '3':
    print(name_user)
    name_user.remove(input('Введите имя который хотите удалить: '))
    print(name_user)



#ЭТО ОДИН ИЗ ВАРИАНТОВ ПУНКТА ИЗМЕНЕНИЕ
#list = ['ter', 'hffh']
#change = int(input())
#list[change] = input()
#print(list)

