class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def turn_on(self):
        return 'Автомобиль заведен!'
    def switch_off(self):
        return 'Автомобиль заглушен!'
    def auto_year(self):
        return car1.year
    def auto_color(self):
        return car1.color
    def auto_type(self):
        return car1.type



color1 = input()
type = input()
year1 = int(input())

car1 = Car(color1, type, year1)

while True:
    admin = input('Что хотите сделать? ')
    if admin == '1':
        print(car1.turn_on())
    elif admin == '2':
        print(car1.switch_off())
    elif admin == '3':
        print(car1.auto_year())
    elif admin == '4':
        print(car1.auto_color())
    elif admin == '5':
        print(car1.auto_type())






