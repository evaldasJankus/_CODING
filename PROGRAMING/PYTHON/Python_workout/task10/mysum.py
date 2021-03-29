    def sum_numeric(*args):
    new_sum = 0
    for elem in args:
        try:
            new_sum += int(elem)
        except Exception as e:
            pass
    return new_sum

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Write a function, mysum_bigger_than, that works the same as mysum, except that
it takes a first argument that precedes *args. That argument indicates the
threshold for including an argument in the sum. Thus, calling mysum_bigger
_than(10, 5, 20, 30, 6) would return 50—because 5 and 6 aren’t greater than
10. This function should similarly work with any type and assumes that all of the
arguments are of the same type. Note that > and < work on many different types
in Python, not just on numbers; with strings, lists, and tuples, it refers to their
sort order
"""
def mysum_bigger_than(*args):
    if not args: return args
    new_sum = args[0]
    # print(args[0])

    for elem in args[1:]:
        if elem > args[0]: new_sum += elem
    return new_sum
"""
 Write a function, sum_numeric, that takes any number of arguments. If the
argument is or can be turned into an integer, then it should be added to the
total. Arguments that can’t be handled as integers should be ignored. The
result is the sum of the numbers. Thus, sum_numeric(10, 20, 'a', '30',
'bcd') would return 60. Notice that even if the string 30 is an element in the
list, it’s converted into an integer and added to the total.
"""
def mysum(*args):
    if not args: return args
    new_sum = args[0]

    for elem in args[1:]:
        new_sum += elem
    return new_sum

"""
 Write a function that takes a list of dicts and returns a single dict that combines
all of the keys and values. If a key appears in more than one argument, the
value should be a list containing all of the values from the arguments.
"""
def my_dict(list_dict):
    new_dict = {}
    for dict1 in list_dict:
        for key in dict1:
            if key in new_dict: new_dict[key] = list(new_dict[key]) + [dict1[key]]
            else: new_dict[key] = dict1[key]
    return new_dict

if __name__=='__main__':
    print(my_dict([{1:'a',2:'b'},{1:'c',3:'d'},{1:'a',2:'b',4:'f'}]))
