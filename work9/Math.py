class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, x, y):
        return x + y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return  x / y

    def subtraction(self, x, y):
        return x - y

while True:
    x = int(input())
    y = int(input())
    user1 = Math(x, y)

    print(user1.addition(x, y))
    print(user1.multiplication(x, y))
    print(user1.division(x, y))
    print(user1.subtraction(x, y))
