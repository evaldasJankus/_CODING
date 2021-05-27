## IMPORTS

#-------------------------MAIN TASK--------------------------------------------
"""
Create fro classes of zoo animals: sheep, wolfs, snakes, parrots. Each class has
3 variables: species, color, number_of_legs. Number of legs and species are same
for all instances of that class, but color may vary depending on the instance call.
"""
# class Animal:
#     def __init__(self, color, number_of_legs):
#         self.species = self.__class__.__name__
#         self.color = color
#         self.number_of_legs = number_of_legs
#     def __str__(self): return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs'
#
# class Sheep(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
# class Wolf(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
# class Snake(Animal):
#     def __init__(self, color):
#         super().__init__(color, 0)
# class Parrot(Animal):
#     def __init__(self, color):
#         super().__init__(color, 2)

"""
solution offered in the book might be more pythonic, but takes more codes, on
the other takes advantage of __class__.__name__ was just not sure which approach
wants to be taken. My approach below:
class Animal:
    def __init__(self, color): self.color = color
    def __str__(self): return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs'

class Sheep(Animal):
    species = 'sheep'
    number_of_legs = 4
class Wolf(Animal):
    species = 'wolf'
    number_of_legs = 4
class Snake(Animal):
    species = 'snake'
    number_of_legs = 0
class Parrot(Animal):
    species = 'parrot'
    number_of_legs = 2
"""
def test_animals():
    sheeps = [Sheep('white'), Sheep('black')]
    wolves = [Wolf('gray'), Wolf('black'), Wolf('brown'), Wolf('white')]
    snakes = [Snake('black'), Snake('golden'), Snake('green')]
    parrots = [Parrot('yello/blue'), Parrot('red')]
    species = [sheeps, wolves, snakes, parrots]
    for specie in species:
        for animal in specie: print(animal)

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Instead of each animal class inheriting directly, from Animal, define several new
classes, ZeroLeggedAnimal, TwoLeggedAnimal, and FourLeggedAnimal, all of
which inherit from Animal, and dictate the number of legs on each instance.
Now modify Wolf, Sheep, Snake, and Parrot such that each class inherits from
one of these new classes, rather than directly from Animal. How does this affect
your method definitions?
"""
# class Animal:
#     def __init__(self, color, number_of_legs):
#         self.species = self.__class__.__name__
#         self.color = color
#         self.number_of_legs = number_of_legs
#     def __str__(self): return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs'
#
# class TwoLeggedAnimal(Animal):
#     def __init__(self, color):
#         super().__init__(color, 2)
# class FourLeggedAnimal(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
# class ZeroLeggedAnimal(Animal):
#     def __init__(self, color):
#         super().__init__(color, 0)
#
# class Sheep(FourLeggedAnimal): pass
# class Wolf(FourLeggedAnimal): pass
# class Snake(ZeroLeggedAnimal): pass
# class Parrot(ZeroLeggedAnimal): pass

"""
 Instead of writing an __init__ method in each subclass, we could also have a
class attribute, number_of_legs, in each subclass—similar to what we did earlier
with Bowl and BigBowl. Implement the hierarchy that way. Do you even need an
__init__ method in each subclass, or will Animal.__init__ suffice?
"""
# My first solution in main task, just use __class__.__name__ in Animal init
# and remove species atribute from the classes

"""
 Let’s say that each class’s __repr__ method should print the animal’s sound,
as well as the standard string we implemented previously. In other words,
str(sheep) would be Baa—white sheep, 4 legs. How would you use inheritance to
maximize code reuse?
"""
# pretty much same as second excercise, Add atribute to the class and udpate
# __str__/__repr__ in the animal class self.sound
class Animal:
    def __init__(self, color):
        self.color = color
        self.species = self.__class__.__name__
    def __str__(self): return f'{self.sound.capitalize()}-{self.color.capitalize()} {self.species}, {self.number_of_legs} legs'

class Sheep(Animal):
    sound = 'baa'
    number_of_legs = 4
class Wolf(Animal):
    sound = 'auuu'
    number_of_legs = 4
class Snake(Animal):
    sound = 'ssssss'
    number_of_legs = 0
class Parrot(Animal):
    sound = 'whistles'
    number_of_legs = 2


if __name__ == '__main__':
    ## TEST CODE HERE
    test_animals()
