class User:
    def __init__(self,username, mail, age, number, posts=[]):
        self.username = username
        self.mail = mail
        self.age = age
        self.number = number
        self.posts = posts

    def change_name(self, new_name):
        self.username = new_name
        return user1.username

    def change_mail(self, new_mail):
        self.mail == new_mail
        return user1.mail

    def change_age(self, new_age):
        self.age == new_age
        return user1.age

    def change_number(self, new_number):
        self.number = new_number
        return user1.number

    def create_post(self, new_post):
        self.posts.append(new_post)
        return user1.posts

name1 = input()
mail1 = input()
age1 = int(input())
number1 = int(input())


user1 = User(name1, mail1, age1, number1, posts=[])

while True:
    admin = input('Что хотите сделать? ')
    if admin == '1':
        new_name1 = input()
        print(user1.change_name(new_name1))
    elif admin == '2':
        new_mail1 = input()
        print(user1.change_mail(new_mail1))
    elif admin == '3':
        new_age1 = int(input())
        print(user1.change_age(new_age1))
    elif admin == '4':
        new_number1 = int(input())
        print(user1.change_number(new_number1))
    elif admin == '5':
        new_post1 = input()
        print(user1.create_post(new_post1))








