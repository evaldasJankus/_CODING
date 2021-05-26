## IMPORTS
from scoop import Scoop
from bowl_limit import Bowl
#-------------------------MAIN TASK--------------------------------------------
"""
Implement BigBowl for this exercise, such that the only difference between it and
the Bowl class we created earlier is that it can have five scoops, rather than three.
"""
class BigBowl(Bowl):
    MAX = Bowl.MAX + 2
    def __str__(self):
        return 'BigBowl is Empty' if not self.scoops else 'BigBowl with flavour(s): '.upper() + ','.join([s.getFlavour() for s in self.scoops])


def test_big_bowl():
    s1, s2, s3 = Scoop(), Scoop('Choco'), Scoop('strawbery')
    b = BigBowl()
    # b = Bowl()
    print(b)
    b.add_scoop(s1, s2, s1, s3)
    print(b)
    b.add_scoop(s3)
    print(b)
    b.add_scoop(s3)
    print(b)
    b.remove_scoop('sherbet')
    # b.add_scoop(s3)
    print(b)
    # b.add_scoop(s3)
    # b.remove_scoop('Choco')
    # print(b)

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Write an Envelope class, with two attributes, weight (a float, measuring grams)
and was_sent (a Boolean, defaulting to False). There should be three methods: (1)
send, which sends the letter, and changes was_sent to True, but only
after the envelope has enough postage; (2) add_postage, which adds postage
equal to its argument; and (3) postage_needed, which indicates how much
postage the envelope needs total. The postage needed will be the weight of the
envelope times 10. Now write a BigEnvelope class that works just like Envelope
except that the postage is 15 times the weight, rather than 10.
[POSTAGE - pašto išlaidos]
"""

class Envelope:
    TIMES = 10
    def __init__(self, weight, was_sent=False):
        self.weight = weight # in grams (g)
        self.was_sent = was_sent
        self.postage = 0
    def __str__(self): return f'{"*"*15}\nEnvelope weight: {self.weight}, SENT: {self.was_sent}\ncurrent postage: {self.postage}\npostage needed {self.postage_needed()}'
    def send(self):
        if not self.was_sent:
            self.was_sent = True if self.postage >= self.postage_needed() else False
            return 'Postage is not enough!' if not self.was_sent else 'Envelope has been sent!'
        return 'WARNING! Envelope has already been sent.'
    def add_postage(self, amount): self.postage += amount
    def postage_needed(self): return self.weight * self.__class__.TIMES

def test_envelope():
    e, e2 = Envelope(0.2), Envelope(1.3)
    # print(e,'\n',e2)
    print(e.send())
    e.add_postage(1.4)
    print(e.send())
    e.add_postage(0.6)
    print(e.send())
    print(e.send())
    # print(e.postage)

class BigEnvelope(Envelope):
    TIMES = 15

def test_big_envelope():
    e, e2 = BigEnvelope(0.2), BigEnvelope(1.3)
    # print(e,'\n',e2)
    print(e.send())
    e.add_postage(1.4)
    print(e.send())
    e.add_postage(0.6)
    print(e.send())
    print(e.send())
    print(e)
    e.add_postage(4)
    print(e.send())

"""
 Create a Phone class that represents a mobile phone. (Are there still nonmobile
phones?) The phone should implement a dial method that dials a phone number
(or simulates doing so). Implement a SmartPhone subclass that uses the
Phone.dial method but implements its own run_app method. Now implement
an iPhone subclass that implements not only a run_app method, but also its
own dial method, which invokes the parent’s dial method but whose output is
all in lowercase as a sign of its coolness
"""
class Phone:
    def dial(self, number): return f"DIALING NUMBER: <{number}>"

class SmartPhone(Phone):
    def run_app(self, app): return f"APP >{app}< IS RUNNING"

class Iphone(Phone):
    def dial(self, number): return Phone.dial(self,number).lower()
    def run_app(self, app): return f"Iphone App >{app}< Is Running"

def test_phones():
    phones = [Phone(), SmartPhone(), Iphone()]
    for phone in phones: print(phone.dial(+71120202020))
    for phone in phones[1:]: print(phone.run_app('Calculator'))

"""
 Define a Bread class representing a loaf of bread. We should be able to invoke a
get_nutrition method on the object, passing an integer representing the
number of slices we want to eat. In return, we’ll receive a dict whose key-value
pairs will represent calories, carbohydrates, sodium, sugar, and fat, indicating
the nutritional statistics for that number of slices. Now implement two new
classes that inherit from Bread, namely WholeWheatBread and RyeBread. Each
class should implement the same get_nutrition method, but with different
nutritional information where appropriate.
"""
class Bread:
    nutritions = {'calories': 82, 'carbohydrates':13.8, 'sodium':0.144, 'sugar':1.4, 'fat':1.1}
    def get_nutrition(self, slices): return {k:round(v*slices,1) for k,v in self.nutritions.items()}

class WholeWheatBread(Bread):
    nutritions = {'calories': 90, 'carbohydrates':16, 'sugar':3, 'fat':2}
    def __init__(self):
        WholeWheatBread.nutritions = {**Bread.nutritions, **WholeWheatBread.nutritions}

class RyeBread(Bread):
    nutritions = {'calories': 83, 'carbohydrates':16, 'fat':1}
    def __init__(self):
        RyeBread.nutritions = {**Bread.nutritions, **RyeBread.nutritions}

def test_bread():
    from random import randint
    breads = [Bread(), WholeWheatBread(), RyeBread()]
    for bread in breads: print(bread.__class__.__name__, bread.get_nutrition(randint(2,6)))

if __name__ == '__main__':
    test_bread()
    # test_phones()
    # test_big_envelope()
