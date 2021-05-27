## IMPORTS

#-------------------------MAIN TASK--------------------------------------------
"""
Create fro classes of zoo animals: sheep, wolfs, snakes, parrots. Each class has
3 variables: species, color, number_of_legs. Number of legs and species are same
for all instances of that class, but color may vary depending on the instance call.
"""
class Animal:
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    def __str__(self): return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs'

class Sheep(Animal):
    takes_space = 3
    def __init__(self, color):
        super().__init__(color, 4)
class Wolf(Animal):
    takes_space = 4
    def __init__(self, color):
        super().__init__(color, 4)
class Snake(Animal):
    takes_space = 1
    def __init__(self, color):
        super().__init__(color, 0)
class Parrot(Animal):
    takes_space = 2
    def __init__(self, color):
        super().__init__(color, 2)

def test_animals():
    sheeps = [Sheep('white'), Sheep('black')]
    wolves = [Wolf('gray'), Wolf('black'), Wolf('brown'), Wolf('white')]
    snakes = [Snake('black'), Snake('golden'), Snake('green')]
    parrots = [Parrot('yello/blue'), Parrot('red')]
    species = [sheeps, wolves, snakes, parrots]
    for specie in species:
        for animal in specie: print(animal)

#-------------------------BEYOND THE TASK--------------------------------------

if __name__ == '__main__':
    ## TEST CODE HERE
    test_animals()
