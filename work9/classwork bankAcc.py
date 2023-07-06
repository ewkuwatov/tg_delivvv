# accaunt = { 9860: 'Temur'}
# money = { 9860: 18000}
# credits = {9860: 0}
#
# class BankAccaunt:
#     def __init__(self, name):
#         self.name = name
#         self.id_number = id_number
#         self.balance = balance
#         self.credits = credits
#     def acc_name(self):
#         admin = input('Выберите услугу:\n' + \
#                       'Введите "1" если хотите войти\n' + \
#                       'Введите "2" если хотите зарегестрироваться\n' + \
#                       'Ввести здесь ------->: ')
#         if admin == '1':
#             acc_n = input('Введите ваш ID номер: ')
#             if acc_n in id_9860:
#                 return f'Добро пожаловать, {BankAccaunt( self.name)}'
#             else:
#                 return 'Вы не зарегестрированы!'
#     def entrance(self):
#         id = int(input('Введите свой ID номер: '))
#         if id in self.id_number:
#             return f'Добро пожаловать!'
#
#     def my_balance(self):
#         return f'Ваш баланс: {self.balance}'
#
# id_9860 = BankAccaunt('Temur', 9860, 18000, 0)


# class BankAccaunt:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         return 'Вклад успешно внесен!'
#     def cash(self, money):
#         if money <= self.balance:
#             self.balance -= money
#         else:
#             return 'Недостаточно средств'
#     def my_balance(self):
#         return f'Ваш баланс: {self.balance}'
#
# client_name = input('Введите ваше имя: ')
# account1 = BankAccaunt(client_name)
# print(account1.name)
#
# while True:
#     admin = input('Что хотите сделать? ')
#     if admin.lower() == 'депозит':
#         dep = int(input('Сколько денег вы хотите вложить? '))
#         print(account1.deposit(dep))
#     elif admin.lower() == 'обналичить':
#         cas = int(input('Сколько денег вы хотите снять? '))
#         print(account1.cash(cas))
#     elif admin.lower() == 'баланс':
#         print(account1.my_balance())
#     else:
#         print('Не понял вас')