class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print(self.name, self.id)

obj1 = Person("Luis", 1)
obj1.Display()
