import sys
sys.path.append('..\\task5')
from pig_latin import pig_lating

#-------------------------MAIN TASK--------------------------------------------
"""
Iterate through file and transalte each word into piglatin and rturn back string
"""
def pig_latin_translator(filename='data'):
    output_string = ''
    with open(filename) as f_reader:
        output_string = ' '.join(pig_lating(word) for line in f_reader for word in line.split())
    return output_string

#-------------------------BEYOND THE TASK--------------------------------------
"""
 In this exercise, plfile applied the plword function to every word in a file.
Write a new function, funcfile, that will take two arguments—a filename and a
function. The output from the function should be a string, the result of invoking
the function on each word in the text file. You can think of this as a generic
version of plfile, one that can return any string value
"""
def func_file(filename='data', func=pig_latin_translator):
    return func(filename)

"""
 Use a nested list comprehension to transform a list of dicts into a list of
twoelement (name-value) tuples, each of which represents one of the name-value
pairs in one of the dicts. If more than one dict has the same name-value pair,
then the tuple should appear twice.
"""
def nested_list(dict_list):
     # only this  if to make tuple with all key:value keys
    new_tuple_lsit = [(key,elem[key]) for elem in dict_list for key in elem]

    # this to remove dublicates number 2
    new_tuple = [new_tuple_lsit.remove(elem) for elem in new_tuple_lsit if new_tuple_lsit.count(elem) > 2]
    return new_tuple_lsit

"""
 Assume that you have a list of dicts, in which each dict contains two name-value
pairs: name and hobbies, where name is the person’s name and hobbies is a set
of strings representing the person’s hobbies. What are the three most popular
hobbies among the people listed in the dicts?
"""
from collections import Counter
def three_most_common_hobies():
    list_of_dicst = [{'n':'evaldas','h':set(['swim', 'run', 'bike','work'])},
                     {'n':'albert','h':set(['swim', 'run', 'money','work'])},
                     {'n':'aiste','h':set(['swim', 'run', 'bike','work','children'])},
                     {'n':'laima','h':set(['swim', 'run', 'walk','work'])}]
    # Counting manually
    new_gen = list((key for dict_elem in list_of_dicst for key in dict_elem['h']))
    new_dict = {elem:new_gen.count(elem) for elem in list(set(new_gen))}
    print(new_dict,'\n',sorted(new_dict, key=lambda x: new_dict[x], reverse=True)[:3])

    # USing Counter
    c = Counter(key for dict_elem in list_of_dicst for key in dict_elem['h'])
    print(c.most_common(3))

if __name__ == '__main__':
    # print(pig_latin_translator())
    # print(func_file())
    # print(nested_list([{'a':1},{'a':1,'b':2},{'c':1,'b':2,'a':1,'d':3}]))
    three_most_common_hobies()
