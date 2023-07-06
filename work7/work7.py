# def main():
#     print('Hello world')
#
# main()
#
# def list():
#     list_mu = []
#     print(list_mu)
#
# list()

# def created_list():
#     my_list = []
#     return my_list
#
# created_list()
# print(created_list())

# def created_list():
#     user_list = [5]
#
#     return user_list
#
# print(created_list())

# def calc(a = input(), b = input()):
#     result = a * b
#     return result
#
# print(calc(5 , 5))

# all_producs = {'Склад': {'name': 'Хлeб'}}
#
# def spam(a):
#
#     print(all_producs['Склад'][a])
#
# spam('name')
#
# def sapm(*args):
#     return args
# print(sapm('hello', 1, 3 ,4))

# def spam(**kwargs):
#     return kwargs
# print(spam(name='hello', age=23))

# def spam1(**kwargs):
#     for k, v in kwargs.items():
#         return k, v
# print(spam1(name= 'gaga', age=3))

def spam():
    x = int(input())
    if x % 2 != 0:
        return ("не четное")
    elif x % 2 == 0:
        return ("четное")
while True:
     print(spam())
