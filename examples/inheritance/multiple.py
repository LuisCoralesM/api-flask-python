class Person(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def Display(self):
        print(self.id, self.name)


class Human(object):
    def __init__(self, bloodType):
        self.bloodType = bloodType

    def Display(self):
        print(self.bloodType)

# Multiple inheritance


class Civilian(Person, Human):
    def __init__(self, id, name, bloodType):
        Person.__init__(self, id, name)
        Human.__init__(self, bloodType)
        print("Civilian")

    def printStr(self):
        print(self.name, self.id, self.bloodType)


obj = Civilian(1, "Luis", "O")
obj.printStr()
obj.Display()
