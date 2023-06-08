class Animal:
    def __init__(self, leg_count):
        self.leg_count = leg_count
        print("Animal object was created")

    def runs(self):
        print("Running started")

    def count_legs(self):
        print("Number of legs:", self.leg_count)

    def return_legs(self):
        return self.leg_count


animal = Animal(4)


animal.runs()


animal.count_legs()


legs = animal.return_legs()
print("Number of legs:", legs)


print("Number of legs:", animal.leg_count)
