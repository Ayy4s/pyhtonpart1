class Animal:
    def __init__(self, species, legs):
        self._species = species
        self._number_of_legs = legs

    def get_number_of_legs(self):
        return self._number_of_legs

    def display_legs(self):
        print(f"The {self._species} has {self.get_number_of_legs()} legs.")



animal = Animal("Dog", 4)


animal.display_legs()
