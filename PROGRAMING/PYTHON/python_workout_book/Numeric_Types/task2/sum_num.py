def sum_recursively(nlist, total=0):
    if len(nlist) == 0: return total

    if isinstance(nlist[0], list):
        total += sum_recursively(nlist[0])
    else:
        total += nlist[0]
    return sum_recursively(nlist[1:], total)

def sum_recursively_nototal(nlist):
    if len(nlist) == 0: return 0

    if isinstance(nlist[0], list):
        return summ(nlist[0]) + summ(nlist[1:])

    return nlist[0] + summ(nlist[1:])

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Write a function that takes a list of Python objects. Sum the objects that either
are integers or can be turned into integers, ignoring the others.
"""
def sum_all(olist):
    total = 0
    # Method #1 (Using exception handling is much simpier and better solution)
    # for num in olist:
    #     try:
    #         total += int(num)
    #     except:
    #         pass

    # Method #2
    def isnumbers(number):
        numbers = '1234567890.'
        for x in number:
            if not (x in numbers): return False
        return True

    for num in olist:
        if isinstance(num, int) or isinstance(num, float):
            total += int(num)
        elif isinstance(num, str) and isnumbers(num):
            total += int(float(num))
    return total

"""
 The built-in version of sum takes an optional second argument, which is used as
the starting point for the summing. (That’s why it takes a list of numbers as its
first argument, unlike our mysum implementation.) So sum([1,2,3], 4) returns
10, because 1+2+3 is 6, which would be added to the starting value of 4. Reimplement
your mysum function such that it works in this way. If a second argument is not
provided, then it should default to 0. Note that while you can write
a function in Python 3 that defines a parameter after *args, I’d suggest avoiding
it and just taking two arguments—a list and an optional starting point.
"""
def mysum(*args, n=0):
    total = n
    for num in args:
        total += num
    return total

"""
 Write a function that takes a list of numbers. It should return the average (i.e.,
arithmetic mean) of those numbers.
"""
def average(nlist):
    avg = 0
    for num in nlist:
        avg += num
    return avg / len(nlist)

"""
 Write a function that takes a list of words (strings). It should return a tuple
containing three integers, representing the length of the shortest word, the length
of the longest word, and the average word length.
"""
def word_list_info(wlist):
    word_lengths = list(map(lambda x: len(x), wlist))
    word_lengths.sort()
    return word_lengths[0], word_lengths[-1], round(average(word_lengths), 2)


if __name__=='__main__':
    # from random import randint
    # numbers = [randint(-10, 50) for _ in range(5)]
    # print('List of numbers:',numbers,'sum of those numbers:' , mysum(*numbers))
    # print('List of numbers:',numbers,'avg of those numbers:' , average(numbers))
    # words_list = ['Hello', 'how', 'are', 'is', 'doing','evaldas', 'Jankus']
    # print('List of words:',words_list,'(shortest word|longest word| average of all words length):' , word_list_info(words_list))
    # object_list = ['hello', 12, '5', '[1,2]','1.0', 3.5,('hi','bye')]
    # print('List of objects:',object_list,'sum of all numbers:', sum_all(object_list))
    numbers = [1,[0,[1,2]],2,[3,4],1,5]
    print(summ(numbers))
