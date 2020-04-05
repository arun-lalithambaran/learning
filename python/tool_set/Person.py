class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getPerson(self):
        return {
            "name": self.name,
            "age": self.age
        }