import random

name_gamer = input('Напишите свое имя: ')

while True:

    point = input(f"{name_gamer}, cделайте выбор — камень, ножницы или бумага: ")

    possible_actions = ["камень", "бумага", "ножницы"]
    computer_action = random.choice(possible_actions)

    print(f"Вы выбрали {point}, компьютер выбрал {computer_action}.")

    if point == computer_action:
        print('У вас ничья!')
    elif point == "камень":
        if computer_action == "ножницы":
            print('Вы выиграли!')
        else:
            print('Вы проиграли')
    elif point == "бумага":
        if computer_action == "камень":
            print('Вы выиграли!')
        else:
            print('Вы проиграли')
    elif point == "ножницы":
        if computer_action == "бумага":
            print('Вы выиграли!')
        else:
            print('Вы проиграли')
    else:
        print('Ошибка')

    again = ""
    again = input("Сыграем еще? (да/нет): ")
    if again.lower() != "да":
        break
