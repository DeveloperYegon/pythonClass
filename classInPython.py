class Person:
    def __init__(self, name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
        print(f"My name is {self.name},{self.age} and {self.gender} gender")

person1=Person("Gideon",21,"male")
person1.introduce()