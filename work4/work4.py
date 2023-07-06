# a = [1, 2, 3, 4, 5, 6]
#
# for i in a:
#     print(i + 2)

# name = 'Temur'
# for i in name:
#     print(i)
#
# p = [1, 2, 3, 4]
#
# for i in p:
#     print(i+2)
#
# w = (6, 5, 5)
#
# for i in range (1, 5):
#     print(f'w')

# names = ['Ivan', 'pavel', 'Jordan', 5]
#
# for i in range(0,20):
#     for name in names:
#         print(name)

# num = 0
#
# while num <= 10:
#     print(num)
#     num += 2

# p = ['m', 'my', 23]
# i = 0
# while i < len(p):
#     print(p[i])
#     i += 1

# names = ['Pavel', 'Ivan', 'Jordan']
#
# while True:
#     new_name = input()
#     if new_name== 'Stop':
#         break
#     elif new_name == 'Список':
#         print(names)
#     else:
#         names.append(new_name)
#         print(f'{new_name} добавлена')
#         print(names)

# names = []
# numbers = []
#
# while True:
#     point = input()
#     if point == 'Stop':
#         break
#     elif point == int():
#         numbers.append(point)
#         print(numbers)
#     elif point == str(''):
#         names.append(point)
#         print(names)

# names = []
# nums = []
# services = []
#
# while True:
#     admin = input('Что хотите сделать? ')
#     if admin == 'Имя':
#         new_name = input('Ваше имя: ')
#         if new_name in names:
#             print('Такое имя уже есть!')
#             new_name1 = input('Введите имя заново: ')
#             if new_name1 in names:
#                 print('Максимальное количество попыток!')
#             else:
#                 names.append(new_name1)
#                 print('Ваше имя успешно добавлено!')
#         else:
#             names.append(new_name)
#             print('Ваше имя успешно добавлено!')
#     elif admin == 'Номер':
#         new_num = input('Ваш номер: ')
#         if new_num in nums:
#             print('Такой номер уже есть!')
#             new_num1 = input('Введите номер заново: ')
#             if new_num1 in nums:
#                 print('Максимальное количество попыток!')
#             else:
#                 nums.append(new_num1)
#                 print('Ваш номер успешно добавлен!')
#         else:
#             nums.append(new_num)
#             print('Ваш номер успешно добавлен!')
#     elif admin == 'Услуга':
#         new_serv = input('Введите услугу: ')
#         services.append(new_serv)
#         print('Услуга успешно добавлена')
#     else:
#         print('Я вас не понял')


# words = []
#
# while True:
#     new_word = input('Введите слово: ')
#     if new_word[0] != new_word[-1] or new_word[1] != new_word[-2]:
#         print('Это слово НЕявляется палиндромом')
#     else:
#         print('Это слово является палиндромом')
#         if new_word in words:
#             print('Это слово уже есть ')
#             new_word1 = input('введите другое имя: ')
#             if new_word1 in words:
#                 print('Слишком много попыток')
#             else:
#                 if new_word[0] != new_word[-1] or new_word[1] != new_word[-2]:
#                     print('Это слово НЕявляется палиндромом')
#                 else:
#                     print('Это слово является палиндромом')
#                     words.append(new_word)
#         print(words)
#         words.append(new_word)
#
# words = []
#
# new_word = input('Введите слово: ')
# if new_word[0] != new_word[-1] or new_word[1] != new_word[-2]:
#     print('Это слово НЕ является палиндромом')
# else:
#     print('Это слово является палиндромом')
#     if new_word in words:
#         print('но вы это слово уже ввели')
#         new_word1 = input('Введите другое слово ')
#         if new_word1 in words:
#             print('много попыток')
#         else:
#             if new_word1[0] != new_word1[-1] or new_word1[1] != new_word1[-2]:
#                 print('Это слово НЕ является палиндромом')
#             else:
#                 print('Это слово является палиндромом')
#                 words.append(new_word1)
#     words.append(new_word)
#     print(list(set(words)))

new_word = [1, 2, 3]
list = new_word[::-1]
print(list)