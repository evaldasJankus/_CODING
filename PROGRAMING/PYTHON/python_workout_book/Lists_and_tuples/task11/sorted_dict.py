PEOPLE = [{'first':'Reuven', 'last':'Lerner',
        'email':'reuven@lerner.co.il'},
        {'first':'Donald', 'last':'Trump',
        'email':'president@whitehouse.gov'},
        {'first':'Vladimir', 'last':'Putin',
        'email':'president@kremvax.ru'},
        {'first':'Aladimir', 'last':'Lerner',
        'email':'president@kremvax.ru'}
        ]

def sort_dict(dList):
    '''
    sorted by last name and then by first name. Using itemgetter to receive an item
    '''
    # method 1
    from operator import itemgetter
    return sorted(dList, key=itemgetter('last','first') )

    # method 2
    # return sorted(dList, key=lambda person: person['last']+person['first'])

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Given a sequence of positive and negative numbers, sort them by absolute value.
"""
def positive_negative_number(iter):
    # Sorting number by they abs value
    return sorted(iter, key=abs)

def same_as_above(iter):
    import sys
    CHAR_BIT = 8

    def find_mask(num):
        mask = num >> (sys.getsizeof(int()) // 8 * CHAR_BIT - 1)
        return (mask + num) ^ mask

    return sorted(iter, key=find_mask)

"""
 Given a list of strings, sort them according to how many vowels they contain.
"""
def volwel_number_sort(iter):
    # Sorting inner strings byt the number of vowels inside it
    vowels = ('a', 'e', 'i', 'o', 'u')
    return sorted(iter, key=lambda x: sum([x.count(ch) for ch in vowels]))

"""
 Given a list of lists, with each list containing zero or more numbers, sort by the
sum of each inner list’s numbers.
"""
def list_sort(iter):
    # Sorting inner lists by the sum of the numbers inside
    return sorted(iter, key=sum)


if __name__=='__main__':
    print(positive_negative_number([1,2,3,-5,-4,1,0,-3]))
    print(same_as_above([1,2,3,-5,-4,1,0,-3]))
    # print(sort_dict(PEOPLE))
    print(volwel_number_sort(['hello','labas','ascdaa', 'a']))
    print(list_sort([[1,2],[],[0,-1],[24],[-80,6,3,1]]))
