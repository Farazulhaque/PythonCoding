class Person:
    name = ""
    gender = ""
    age = 20

    def __init__(self, address, height, weight):
        self._address = address
        self.height = height
        self.weight = weight

    def updateName(self, name):
        self.name = name

    def printAllInfo(self):
        print(f"Name = {self.name}, age = {self.age}, gender = {self.gender}")
        print(
            f"\nAddress = {self._address}, height = {self.height}, weight = {self.weight}")

    @classmethod
    def updateName(cls, name):
        cls.name = name

    @classmethod
    def updateGender(cls, gender):
        cls.gender = gender


p1 = Person("India", 154, 50)
# instance variable
p1.updateName("Faraz")
p1.printAllInfo()
# class varable
Person.updateName("Arisha")
Person.updateGender("F")
p1.printAllInfo()
