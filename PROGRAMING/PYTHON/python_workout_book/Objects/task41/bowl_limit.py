## IMPORTS
from scoop import Scoop
#-------------------------MAIN TASK--------------------------------------------
"""
Add bowl limit for scoops to have max 3 flavours(or 3 scoops)
"""
class Bowl:
    MAX = 3
    def __init__(self):
        self.scoops = []
        # self.scoops_count = 0
    def add_scoop(self, *args):
        for s in args:
            if len(self.scoops) < self.__class__.MAX:
                self.scoops.append(s)
            else:
                print('Bowl is full (For Loop)')
                break

    def remove_scoop(self, r_scoop):
        flavours = [s.getFlavour() for s in self.scoops]
        if not (r_scoop in flavours):
            print(f'Bowl does not have flavour <{r_scoop}>')
        else:
            self.scoops.pop(flavours.index(r_scoop))
            # self.scoops_count -= 1

    def __str__(self):
        return 'Bowl is Empty' if not self.scoops else 'Bowl with flavour(s): '.upper() + ','.join([s.getFlavour() for s in self.scoops])


def test_bowl():
    s1, s2, s3 = Scoop(), Scoop('Choco'), Scoop('strawbery')
    b = Bowl()
    print(b)
    b.add_scoop(s1, s2, s1, s3)
    print(b)
    # b.add_scoop(s3)
    # print(b)
    b.remove_scoop('vanila')
    b.add_scoop(s3)
    print(b)
    b.add_scoop(s3)
    # b.remove_scoop('Choco')
    # print(b)


#-------------------------BEYOND THE TASK--------------------------------------
"""Define a Person class, and a population class attribute that increases each time
you create a new instance of Person. Double-check that after you’ve created five
instances, named p1 through p5, Person.population and p1.population are
both equal to 5"""
class Person:
    population = 0
    def __init__(self):
        Person.population += 1
    def __del__(self):
        Person.population -= 1
        # Person.__del__()

def test_population():
    person_list = [Person() for p in range(5)]
    print(Person.population,'\n------------')
    for p in person_list: print(p.population)
    del person_list[2]
    print('--------------')
    for p in person_list: print(p.population)

"""
Modify your Person class
such that when a Person instance is deleted, the population count decrements
by 1. I
"""
# Check Person class above

"""
Define a Transaction class, in which each instance represents either a deposit
or a withdrawal from a bank account. When creating a new instance of Transaction,
you’ll need to specify an amount—positive for a deposit and negative for a
withdrawal. Use a class attribute to keep track of the current balance, which
should be equal to the sum of the amounts in all instances created to date.
"""
class Transaction:
    current_balance = 0
    all_balance = 0
    def __init__(self, amount):
        Transaction.current_balance += amount
        Transaction.all_balance += abs(amount)
        print('amount changed: ',amount)

def test_transaction():
    from random import randint
    sign = [1,-1]
    transaction_list = [Transaction((sign[randint(0,1)] * randint(15,30))) for _ in range(5) ]
    print(Transaction.current_balance, transaction_list[0].current_balance)
    print(Transaction.all_balance, transaction_list[0].all_balance)


if __name__ == '__main__':
    test_transaction()
    # test_population()
    # test_books_shelfs()
    # test_bowl()
