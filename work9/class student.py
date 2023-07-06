class Students:
    def __init__(self, name, age, groupNumber):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name


    def getAge(self):
        return self.age

    def setGroupNumber(self):
        return self.groupNumber

    def SetNameAge(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
        return new_age, new_name

    def setGroupNumber(self, new_groupNum):
        self.groupNumber = new_groupNum
        return new_groupNum


temur = Students('Temur', 23, '10A')
print(temur.name)
kamran = Students('Kamran', 23, '10A')
print(kamran.SetNameAge('Kamran', 24))
mirshod = Students('Mirshod', 24, '9B')
print(mirshod.getAge())
jordan = Students('Jordan', 34, '8V')
print(jordan.getName())
lebron = Students('Lebron', 11, '11D')
print(lebron.setGroupNumber('10D'))















