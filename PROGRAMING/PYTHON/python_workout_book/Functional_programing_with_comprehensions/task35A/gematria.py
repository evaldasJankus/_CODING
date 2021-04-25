## IMPORTS
from string import ascii_lowercase
import json

#-------------------------MAIN TASK--------------------------------------------
"""
Create dict of lower case, where key is letter and value is a value increased by
one (starting from 1)
"""
def get_letter_dict():
    # d = {}
    return {letter:indx for indx,letter in enumerate(ascii_lowercase,1)}

#-------------------------BEYOND THE TASK--------------------------------------
"""
Create dict from a file, where name and values are separated by = sign.
"""
def get_dict(myfile='config'):
    return {line.split('=')[0].strip():line.split('=')[-1].strip() for line in open(myfile)}

"""
Create dict from a file, where name and values are separated by = sign. Filter
values which can not bet turned to integers
"""
def get_dict_int(myfile='config'):
    return {line.split('=')[0].strip():int(line.split('=')[-1].strip()) for line in open(myfile) if line.split('=')[-1].strip().isdigit()}

"""
Transform json file 'cities.json' into dictionary, where keys are city name and
values are population of those cities. Second part, do the same but keys should be
tuple of state,citie_name
"""
def transform_json(myjson='cities.json'):
    d = {}
    with open(myjson) as f:
        json_reader = json.load(f)
        # Part 1
        # d = {elem['city']: elem['population'] for elem in json_reader}

        # Part 2
        d = {(elem['state'],elem['city']): elem['population'] for elem in json_reader}

    return d

if __name__ == '__main__':
    # print(get_letter_dict())
    # print(get_dict_int())
    print(transform_json())
