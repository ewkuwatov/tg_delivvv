admin = int(input('Выберите задания:\n' + \
                  'Введите "1" если хотите выбрать 1 задание\n' + \
                  'Введите "2" если хотите выбрать 2 задание\n' + \
                  'Ввести здесь ------->: '))

words = []

while True:
    if admin == 1:
        new_word = input('Введите слово: ')
        if new_word != new_word[::-1]:
            print('Это слово НЕ является палиндромом')
        else:
            print('Это слово является палиндромом')
            if new_word in words:
                print('но вы это слово уже ввели')
                new_word1 = input('Введите другое слово ')
                if new_word1 in words:
                    print('много попыток')
                else:
                    if new_word != new_word[::-1]:
                        print('Это слово НЕ является палиндромом')
                    else:
                        print('Это слово является палиндромом')
                        words.append(new_word1)
            words.append(new_word)
            print(list(set(words)))
            again = ""
            again = input("Еще раз? (да/нет): ")
            if again.lower() != "да":
                admin = int(input('Выберите задания:\n' + \
                                  'Введите "1" если хотите выбрать 1 задание\n' + \
                                  'Введите "2" если хотите изменить контакт\n' + \
                                  'Ввести здесь ------->: '))
    elif admin == 2:
        x = int(input('Введите число: '))
        for y in range(1, 11):
            print(y * x)
        again = ""
        again = input("Еще раз? (да/нет): ")
        if again.lower() != "да":
            admin = int(input('Выберите задания:\n' + \
                              'Введите "1" если хотите выбрать 1 задание\n' + \
                              'Введите "2" если хотите изменить контакт\n' + \
                              'Ввести здесь ------->: '))
    else:
        print('Я не понял ваш ответ. Пожалуйста введите заного)')
        break

































