class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def check_adult(self):
        if 20 <= self.age:
            print(self.name)


people = [
    Human("佐藤", 18),
    Human("佐々木", 20),
    Human("田中", 25),
    Human("山本", 16),
    Human("高橋", 30)
]

for person in people:
    person.check_adult()
