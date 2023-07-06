# class User:
#     name = 'Jordan'
#
# user1 = User()

# class Car:
#     type = 'Bugatti'
#     color = 'white'
#     max_speed = 300
#
# car1 = Car()
# print(car1.color)

# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# nexia = Car('Nexia', 'Silver', 2009)
# print(nexia.color)

# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
#     def name(self):
#         print('инстаграм Темура')
#
# coment = Comment('tima_18', 'it is so cool', 18)
# print(coment.username)
# coment.name()

# class BankAccaunt:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposite(self, amount):
#         self.balance += amount
#         return 'успешно'

class BankAccaunt:
    def init(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return 'Вклад успешно внесен!'
    def cash(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            return 'Недостаточно средств'
    def my_balance(self):
        return f'Ваш баланс: {self.balance}'

client_name = input('Введите ваше имя: ')
account1 = BankAccaunt(client_name)
while True:
    admin = input('Что хотите сделать? ')
    if admin.lower() == 'депозит':
        dep = int(input('Сколько денег вы хотите вложить? '))
        print(account1.deposit(dep))
    elif admin.lower() == 'обналичить':
        cas = int(input('Сколько денег вы хотите снять? '))
        print(account1.cash(cas))
    elif admin.lower() == 'баланс':
        print(account1.my_balance())
    else:
        print('Не понял вас')



