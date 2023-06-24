class Animal:
    def __init__(self, legs):
        self._number_of_legs = legs

    def get_legs(self):
        return self._number_of_legs


class Dog(Animal):
    def __init__(self, name, legs):
        super().__init__(legs)
        self._name = name

    def bark(self):
        print("Woof woof")

    def get_name(self):
        return self._name


dog = Dog("Buddy", 4)
print("Name of the dog:", dog.get_name())
dog.bark()
print("Number of legs:", dog.get_legs())
