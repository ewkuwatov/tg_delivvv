# a = lambda x: x**2
# print(a(10))
#
# a = lambda x: x**3
# print(a(5))
#
# x = ['Hello', 'Pavel']
# a = map(lambda d: d*2, x)
# print(list(a))

# nam1 = int(input())
# math_oper = input()
# nam2 = int(input())
#
# plus = lambda x,y: x+y
# minus = lambda x,y: x-y
# d = lambda x,y: x*y
# m = lambda x,y: x/y
#
# if math_oper == '+':
#     print(plus(nam1, nam2))
# elif math_oper == '-':
#     print(minus(nam1, nam2))
# elif math_oper == '*':
#     print(d(nam1, nam2))
# elif math_oper == '/':
#     print(m(nam1, nam2))

# while True:
    # word1 = input('Первое слово ')
    # word2 = input('Второе слово ')
    #
    # a = lambda d, r: d+r
    # print(a(word1, word2))
    # word = input()
    # e = lambda d: d[::-1]
    # print(e(word))

# x = [-34, 45, 12, -8 , 23, -10]
# a = filter(lambda d: d>0, x)
# print(list(a))

# x = [-1, -2, -4, -4 , -7, 4, 15, 18, 19, 21, -98]
# a = filter(lambda d: d>0, x)
# print(list(a))

# #1
# x = 'Hello World'
# print(x)

# def add(ter, der):
#     return ter ** der
# print(add(5, 2))

# nums = [12, 13, 39, 65, 339, 102, 225]
# a = filter(lambda d: d % 13 == 0, nums)
# print(list(a))


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# while True:
#     y = int(input())
#     if y == 1 or  y ==2 or y ==12:
#         print('Winter')
#     elif y == 3 or  y == 4 or y == 5:
#         print('spring')
#     elif y == 6 or  y == 7 or y == 8:
#         print('summer')
#     elif y == 1 or y ==2 or y == 12:
#         print('autumn')

# dict = {}
# def spam1(**kwargs):
#     return kwargs
# print(spam1(name= 'my1', age= 23))



































# students = {'Классы': {'A': {'Temur Eshkuwatov': {'Возраст': 23 ,
#                                                 'Группа': 'A',
#                                                 'Предмет': 'Физика'},
#
#                             'Mirshod Safarov': {'Возраст': 24,
#                                                 'Группа': 'A',
#                                                 'Предмет': 'Математика'}},
#
#                         'B':
#                             {'Kamran Rustamov': {'Возраст': 23,
#                                                 'Группа': 'Б',
#                                                 'Предмет': 'Физика'},
#
#                             'Muxammadamin Baxadirov': {'Возраст': 24,
#                                                         'Группа': 'Б',
#                                                         'Предмет': 'Физ-ра'}}}}
#
#
# def add_student():
#     name_stud = input('Введите ФИО сдудента: ')
#     age_stud = int(input('Введите возраст сдудента: '))
#     group_stud =  input('Введите группу сдудента: ')
#     subject_stud = input('Введите интересущий предмет сдудента: ')
#     if group_stud in students['Классы']:
#         students['Классы'][group_stud][name_stud]['Возраст'] = age_stud
#         students['Классы'][group_stud][name_stud]['Предмет'] = subject_stud
#         print('Студент успешно добавлен.')
#     else:
#         print('Класс который вы ввели не существует. Пожадуйста выберите другой класс или создайте сначала класс!')
#     again = input("Еще раз? (да/нет): ")
#     if again.lower() != "да":
#         pass
#     else:
#         add_student()
#
#
# def remove_student():
#     name_stud = input('Введите ФИО сдудента: ')
#     age_stud = int(input('Введите возраст сдудента: '))
#     group_stud = input('Введите группу сдудента: ')
#     if name_stud in students['Школа']['Классы'][group_stud]:
#         students['Школа']['Классы'][group_stud].pop(name_stud)
#         print('Студент успешно удален!')
#     else:
#         print('Студент не найден!')
#     again = input("Еще раз? (да/нет): ")
#     if again.lower() != "да":
#         pass
#     else:
#         remove_student()
#
#
# def get_student_info():
#     name_stud = input('Введите ФИО сдудента: ')
#     group_stud =  input('Введите группу сдудента: ')
#     if name_stud in students['Школа']['Классы'] or group_stud in students['Школа']['Классы']:
#         print(students['Школа']['Классы'][group_stud][name_stud])
#     else:
#         print('Студент не найден!')
#     again = input("Еще раз? (да/нет): ")
#     if again.lower() != "да":
#         pass
#     else:
#         get_student_info()
#
# def update_student_age():
#     name_stud = input('Введите ФИО сдудента: ')
#     group_stud = input('Введите группу сдудента: ')
#     if name_stud in students['Школа']['Классы'] or group_stud in students['Школа']['Классы']:
#         change_admin = input('Что хотите изменить? \n ' + \
#                              'Возраст \n' + \
#                              'Предмет')
#         if change_admin == 'Возраст':
#             update_age = int(input('Введите возраст: '))
#             if update_age == '':
#                 students['Школа']['Классы'][group_stud][name_stud] = students['Школа']['Классы'][group_stud][name_stud]['Возраст']
#             else:
#                 students['Школа']['Классы'][group_stud][name_stud] = update_age
#                 print('Данные успешно изменены!')
#         elif change_admin == 'Предмет':
#             update_subject = int(input('Введите предмет: '))
#             if update_subject == '':
#                 students['Школа']['Классы'][group_stud][name_stud] = students['Школа']['Классы'][group_stud][name_stud]['Возраст']
#             else:
#                 students['Школа']['Классы'][group_stud][name_stud] = update_subject
#                 print('Данные успешно изменены!')
#     again = input("Еще раз? (да/нет): ")
#     if again.lower() != "да":
#         pass
#     else:
#         update_student_age()
#
# def get_all_students():
#     all_stud_1 = students['Школа']['Классы']['A'].keys()
#     all_stud_2 = students['Школа']['Классы']['B'].keys()
#     print(all_stud_1 + all_stud_2)
#
# def count_students():
#     all_stud_1 = students['Школа']['Классы']['A'].keys()
#     all_stud_2 = students['Школа']['Классы']['B'].keys()
#     print(len(all_stud_1) + len(all_stud_2))
#
#
#
#
# while True:
#     admin = input('Что хотите сделать: ')
#     if admin == '1':
#         add_student()
#     elif admin == '2':
#         remove_student()
#     elif admin == '3':
#         get_student_info()
#     elif admin == '4':
#         update_student_age()
#     elif admin == '5':
#         get_all_students()
#     elif admin == '6':
#         count_students()
