# class Animal:
#     def make_sound(self, s):
#         print(s)
#
# class Horse(Animal):
#     pass
# class Horse(Animal):
#     def dibi(self):

class Human:
    def __int__(self, name, surname):
        self.name = name
        self.surname = surname

class Me(Human):
    @classmethod
    def __init__(self, height=0, weight=0):
        self.height = height
        self.weight = weight

    def change_height(cls, new_height):
        self.height = new_height
        return f'рост изменился на {new_h1}'

height_me = input('рост 1')
me1 = Me(height_me)
print(me1.height)

new_h1 = input('рост 2 ')
print(me1.change_height(new_h1))

# class Worker:
#     def __init__(self, name,  position):
#         self.name = name
#         self.position = position
#
# class HR(Worker):
#     def __init__(self, name,  position, password):
#         super().__init__(name, position)
#         self.password = password
#
#     def show_info(self, worker):
#         return worker.name
#
# worker1 = Worker('Aleks', 'Manager')
# hr1 = HR('Mich', 'HR', 123)
#
# worker_name = input()
# if worker_name == worker1.name:
#     print('Hello')
# else:
#     password = int(input())
#     if password == hr1.password:
#         action = input()
#         if action == 'Должность '
#             who = input('')
#             hr1.show_info((worker1))


class Player:
    def __init__(self, speed, sila, tochnost, vinosliv):
        self.speed = speed
        self.sila = sila
        self.tochnost = tochnost
        self.vinosliv = vinosliv

class Atack(Player):
    def __init__(self, speed, sila=0, tochnost=0, vinosliv=0):
        super().__init__(speed, sila, tochnost, vinosliv)

    def goal(self):
        return 'Забил'

ronaldo = Atack(speed=100)
print(ronaldo.goal())

