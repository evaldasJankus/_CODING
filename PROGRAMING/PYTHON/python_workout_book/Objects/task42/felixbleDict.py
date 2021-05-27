## IMPORTS

#-------------------------MAIN TASK--------------------------------------------
"""
Inherit dict and make that retrieving data my int or str value before giving up
"""
class FlexibleDict(dict):
    def __init__(self, length, *args, **kwargs):
        self.length = length
        self.update(*args, **kwargs)

    def __setitem__(self, key, value):
        print('Using __setitem__')
        if not(len(self) < self.length):
            print('Dict too big')
            self.pop(list(self.keys())[0])
        super().__setitem__(str(key), value)

    def __getitem__(self, key):
        if not (key in self):
            try:
                if int(key) in self:
                    key = int(key)
                else:
                    key = str(key)
            except ValueError:
                pass
        return super().get(key, 'Key not Found in the dict')


#-------------------------BEYOND THE TASK--------------------------------------
"""
 With FlexibleDict, we allowed the user to use any key, but were then flexible
with the retrieval. Implement StringKeyDict, which converts its keys into
strings as part of the assignment. Thus, immediately after saying skd[1] = 10,
you would be able to then say skd['1'] and get the value of 10 returned. This
can come in handy if you’ll be reading keys from a file and won’t be able to
distinguish between strings and integers.
[https://rszalski.github.io/magicmethods/]
"""
# Check __setitem__ implementation


"""
 The RecentDict class works just like a dict, except that it contains a
userdefined number of key-value pairs, which are determined when the instance is
created. In a RecentDict(5), only the five most recent key-value pairs are kept;
if there are more than five pairs, then the oldest key is removed, along with its
value. Note: your implementation could take into account the fact that modern
dicts store their key-value pairs in chronological order.
"""
# RecentDict would look pretty much same as FlexibleDict just not need __getitem__ override
# Check __init__ + __setitem__ (Added: length in __init__ and if statement in __setitem__)


""""
 The FlatList class inherits from list and overrides the append method. If
append is passed an iterable, then it should add each element of the iterable
separately. This means that fl.append([10, 20, 30]) would not add the list
[10, 20, 30] to fl, but would rather add the individual integers 10, 20, and 30.
You might want to use the built-in iter function (http://mng.bz/Qy2G) to
determine whether the passed argument is indeed iterable.
"""
class FlatList(list):
    def append(self, value):
        print('Append is caled')
        try:
            for v in iter(value): super().append(v)
        except TypeError:
            super().append(value)



if __name__ == '__main__':
    l = FlatList()
    l.append([5,6])
    l.append(6)
    print(l)
