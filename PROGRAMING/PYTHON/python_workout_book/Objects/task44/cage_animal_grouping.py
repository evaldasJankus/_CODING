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
class CageExceptions(Exception): pass
class CageFull(CageExceptions): pass
class CageWrongSpecies(CageExceptions): pass

class Cage:
    animals_group_dict = {'Wolf':['Sheep', 'Snake'],'Sheep':['Wolf'],'Snake':['Parrot'], 'Parrot':['Snake']}
    def __init__(self, id):
        self.id = id
        self.animals = []
        self.current_taken_space = 0
        # self.animals_group_dict = animals_group_dict

    def add_animals(self, *args):
        for animal in args:
            if (self.current_taken_space + animal.takes_space) <= self.limit:
                if not self.animals:
                    self.animals.append(animal)
                    self.current_taken_space += animal.takes_space
                elif animal.__class__.__name__ in self.animals_group_dict[self.animals[0].__class__.__name__] or animal.__class__.__name__ == self.animals[0].__class__.__name__:
                    # print(animal.__class__.__name__, animals_group_dict[self.animals[0].__class__.__name__], animal.__class__.__name__, self.animals[0].__class__.__name__)
                    self.animals.append(animal)
                    self.current_taken_space += animal.takes_space
                else:
                    raise CageWrongSpecies('Wrong species')
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
    # small_cages = [SmallCage(n) for n in range(randint(3,10))]
    big_cages = [BigCage(n) for n in range(randint(2,10))]
    # -- SMAL CAGE TEST --
    # for cage in small_cages:
    #     for num_animals in range(randint(0,5)):
    #         try:
    #             cage.add_animals(choice(choice(species)))
    #         except CageExceptions: pass
    # for cage in small_cages: print(cage)
    # -- BIG CAGE TEST --
    for cage in big_cages:
        for num_animals in range(randint(7,35)):
            try:
                cage.add_animals(choice(choice(species)))
            except CageExceptions: pass
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
class SmallCage(Cage): limit = 15
class BigCage(Cage): limit = 35

"""
Our zookeepers have a macabre sense of humor when it comes to placing animals
together, in that they put wolves and sheep in the first cage, and snakes
and birds in the other cage. (The good news is that with such a configuration,
the zoo will be able to save on food for half of the animals.) Define a dict
describing which animals can be with others. The keys in the dict will be classes,
and the values will be lists of classes that can compatibly be housed with the
keys. Then, when adding new animals to the current cage, you’ll check for
compatibility. Trying to add an animal to a cage that already contains an
incompatible animal will raise an exception
"""
# Implemented above


if __name__ == '__main__':
    test_cage()
