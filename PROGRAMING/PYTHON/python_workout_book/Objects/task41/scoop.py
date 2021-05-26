## IMPORTS

#-------------------------MAIN TASK--------------------------------------------
"""
Create a class Scoop which has one argument flavour and is created on iniciation
Thwn create a fucntion(create_scoops) not in class which creates 3 instances of different flacur
of scoops
"""
class Scoop:
    def __init__(self, flavour="vanila"): self.flavour = flavour
    def __str__(self): return self.flavour
    def setFlavour(self, flavour): self.flavour = flavour
    def getFlavour(self): return self.flavour

def create_scoops():
    flavours = ['vanila', 'chocolate', 'lemon','mint']
    scoops = [Scoop(fl) for fl in flavours]
    for sc in scoops: print(sc.getFlavour())

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Write a Beverage class whose instances will represent beverages. Each beverage
should have two attributes: a name (describing the beverage) and a temperature.
Create several beverages and check that their names and temperatures are all
handled correctly.
"""
class Beverage:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp
    def __str__(self): return f'STR: Beverage name is {self.name.upper()}, temperature is {self.temp}C'
    def __repr__(self): return f'REPR: Beverage name is {self.name.upper()}, temperature is {self.temp}C'
    def setTemperature(self, temp): self.temp = temp
    def setName(self, name): self.name = name
    def getName(self): return self.name
    def getTemperature(self): return self.temp

def create_beverages():
    beverages_list = [('b'+str(n),n*15) for n in range(2,7)]
    beverages = [Beverage(*elem) for elem in beverages_list]
    for beve in beverages: print(repr(beve))

"""
 Modify the Beverage class, such that you can create a new instance specifying
the name, and not the temperature. If you do this, then the temperature
should have a default value of 75 degrees Celsius. Create several beverages and
double-check that the temperature has this default when not specified.
"""
# All what changes is this line: def __init__(self, name, temp=75):

"""
 Create a new LogFile class that expects to be initialized with a filename.
Inside of __init__, open the file for writing and assign it to an attribute,
file, that sits on the instance. Check that it’s possible to write to the file via
the file attribute.
"""
class LogFile:
    def __init__(self, filename):
        self.file = open(filename,'w')
    def checkMode(self): return self.file.mode
    def closeFile(self): self.file.close()
    def isClosed(self): return self.file.closed

def create_file():
    test_file = 'file.txt'
    log = LogFile(test_file)
    print(log.checkMode())
    print(log.isClosed())
    log.closeFile()
    print(log.isClosed())

if __name__ == '__main__':
    create_scoops()
    # create_beverages()
    # create_file()
