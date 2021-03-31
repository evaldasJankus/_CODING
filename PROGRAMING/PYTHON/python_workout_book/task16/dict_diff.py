def dict_diff(d1, d2):
    '''
    Get difference between two dictionaries, returns empty dict {} if dictionaries are exact the same,
    return different elements missing values marked as "None".
    '''
    # all_elem_set = set(d1).union(set(d2))
    all_elem_set = d1.keys() | d2.keys() # dict_keys format has similar functions liek set: |-union, & - difference
    new_dict = {elem: [d1.get(elem,None)] + [d2.get(elem,None)] for elem in all_elem_set if not (d1.get(elem,None) == d2.get(elem,None))}
    return new_dict


#-------------------------BEYOND THE TASK--------------------------------------
def join_N_dict(*args):
    '''
    Join any number of dictionaries.
     The dict.update method merges two dicts. Write a function that takes any
    number of dicts and returns a dict that reflects the combination of all of them.
    If the same key appears in more than one dict, then the most recently merged
    dict’s value should appear in the output.
    '''
    new_dict = {}
    # Method 1
    # for d in args:
    #     new_dict.update(d)

    # Method 2
    for d in args:
        new_dict = {**new_dict, **d}
    return new_dict


"""
 Write a function that takes any even number of arguments and returns a dict
based on them. The even-indexed arguments become the dict keys, while the
odd-numbered arguments become the dict values. Thus, calling the function
with the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being
returned.
"""
def make_dict(*args):
    return {key:value for key,value in zip(args[::2],args[1::2])}


"""
 Write a function , dict_partition, that takes one dict (d) and a function (f) as
arguments. dict_partition will return two dicts, each containing key-value
pairs from d. The decision regarding where to put each of the key-value pairs
will be made according to the output from f, which will be run on each keyvalue pair in d. If f returns True, then the key-value pair will be put in the first
output dict. If f returns False, then the key-value pair will be put in the second
output dict.
"""
def dict_partition(d, f):
    first_dict, second_dict = {}, {}
    for k,v in d.items():
        if f(k,v): first_dict[k] = v  #first_dict.update({k:v})
        else: second_dict[k] = v
    return first_dict,second_dict

if __name__ == '__main__':
    dict1 = {'a':1, 'b':2, 'c':3}
    dict2 = {'a':1, 'b':2, 'c':4}

    d3 = {'a':1, 'b':0, 'd':3}
    d4 = {'a':1, 'b':2, 'c':4}

    d5 = {'a':1, 'b':2, 'd':4}
    # print(dict_diff(dict1,d5))
    # print(join_N_dict(dict1,dict2,d3,d4))
    # print(make_dict('1',2,'3',4,'5',6,'7',8,'9',8,'9'))
    print(dict_partition(d3,lambda x,y: y==0))
