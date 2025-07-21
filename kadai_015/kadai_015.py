class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name)
        print(self.age)


person = Human("佐藤", 25)
person.printinfo()
