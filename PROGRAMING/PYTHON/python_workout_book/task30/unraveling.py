#-------------------------MAIN TASK--------------------------------------------
"""
Just flatten the the list from 2 level lsit make 1 level list
"""
def unraveling(list_2lelve):
    return [elem for inner in list_2lelve for elem in inner]
#-------------------------BEYOND THE TASK--------------------------------------
"""
Same as main task, but filter all all odd integers.
"""
def unraveling__only_odds(list_2lelve):
    return [int(float(elem)) for inner in list_2lelve for elem in inner \
            if (isinstance(elem,(int,float)) and elem % 2) or \
            (isinstance(elem, str) and (elem.isdigit() or elem.replace('.','').isdigit()) \
            and float(elem) % 2)]

"""
Define dict which consists of parents, childrens and grandchildrens, Return all
grandchildrens in one list.
"""
def unraveling_dict(family_tree):
    # family_tree = {'A':['B','C','D'], 'E':['F','G']}
    return [value for key in family_tree for value in family_tree[key]]

"""
Same as above, jsut dict values should consists of grandchildrens name and age
as a value. Return list of grandchildrens names sorted by age
"""
def unraveling_dict_sorting_by_age():
    family_tree = {'A':{'B':12,'C':7,'D':13}, 'E':{'F':14,'G':1}}
    grandchildrens = {inner_key:family_tree[key][inner_key] for key in family_tree for inner_key in family_tree[key]}
    print(grandchildrens)
    return sorted(grandchildrens, key=lambda x: grandchildrens[x])

if __name__ == '__main__':
    # print(unraveling([[1,2],[3,4]]))
    # print(unraveling__only_odds([[1,2],[3,4],['1.2','a',[],3]]))
    # print(unraveling_dict())
    print(unraveling_dict_sorting_by_age())
