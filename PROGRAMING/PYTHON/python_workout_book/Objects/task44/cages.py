## IMPORTS
from animals import Sheep, Wolf, Snake, Parrot

#-------------------------MAIN TASK--------------------------------------------
"""
Create class Cage, which has unique care number on initiation (uniqueness don't
have to be forced, it is just for the task to separate cages). In cages can be
put any number of animals with method named add_animals(*args).  I also want you
to define a __repr__ method so that printing a cage prints not just the cage ID,
but also each of the animals it contains.
"""
class CageFull(Exception): pass

class Cage:
    def __init__(self, id):
        self.id = id
        self.animals = []
        self.current_taken_space = 0
    def add_animals(self, *args):
        for animal in args:
            if (self.current_taken_space + animal.takes_space) <= self.limit:
                self.animals.append(animal)
                self.current_taken_space += animal.takes_space
            else:
                raise CageFull('Cage is Full')
    def __repr__(self):
        out_end = '\n\t----------\n\tNo animals in the cage' if not self.animals else '\n\t----------\n\t' +'\n\t'.join(str(a) for a in self.animals)
        out_end += f'\n\tTAKEN SPACE: {self.current_taken_space}\n\tALLOWED SPACE: {self.limit}'
        return 'Cage' + str(self.id) + out_end

def test_cage():
    from random import choice, randint

    sheeps = [Sheep('white'), Sheep('black')]
    wolves = [Wolf('gray'), Wolf('black'), Wolf('brown'), Wolf('white')]
    snakes = [Snake('black'), Snake('golden'), Snake('green')]
    parrots = [Parrot('yello/blue'), Parrot('red')]
    species = [sheeps, wolves, snakes, parrots]
    small_cages = [SmallCage(n) for n in range(randint(3,10))]
    big_cages = [BigCage(n) for n in range(randint(2,4))]
    # -- SMAL CAGE TEST --
    for cage in small_cages:
        for num_animals in range(randint(0,5)):
            try:
                cage.add_animals(choice(choice(species)))
            except CageFull: pass
    for cage in small_cages: print(cage)
    # -- BIG CAGE TEST --
    for cage in big_cages:
        for num_animals in range(randint(7,12)):
            try:
                cage.add_animals(choice(choice(species)))
            except CageFull: pass
    for cage in big_cages: print(cage)

#-------------------------BEYOND THE TASK--------------------------------------
"""
 As you can see, there are no limits on how many animals can potentially be put
into a cage. Just as we put a limit of three scoops in a Bowl and five in a BigBowl,
you should similarly create Cage and BigCage classes that limit the number of
animals that can be placed there.
FOR MY PURPOSE i WILL USE SAME CAGE CLASS AS SUPER CLASS AND IMPLEMENT TWO MORE
CALSSES: SmaleCage, BigCage. To avoid reimplementing new Cage
"""
class SmallCage(Cage): limit = 5
class BigCage(Cage): limit = 15

"""
 It’s not very realistic to say that we would limit the number of animals in a cage.
Rather, it makes more sense to describe how much space each animal needs
and to ensure that the total amount of space needed per animal isn’t greater
than the space in each cage. You should thus modify each of the Animal subclasses
to include a space_required attribute. Then modify the Cage and BigCage classes
to reflect how much space each one has. Adding more animals than the cage can
contain should raise an exception
"""
# Updated Animal subclasses to have atriibute takes_spaces, which tells how much
# space does an animal takes. And then update super class Cage __init__, by
# adding one instance atriibute current_taken_space and updaiting add_animals
# method to meed space requirements in the task

"""
For the last take will create different file, not to loose in the implementation
"""


if __name__ == '__main__':
    test_cage()
