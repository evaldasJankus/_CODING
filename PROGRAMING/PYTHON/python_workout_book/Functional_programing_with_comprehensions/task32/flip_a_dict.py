## IMPORTS
from pathlib import Path

#-------------------------MAIN TASK--------------------------------------------
"""
Given dictionary reverse keys and values in reverse, key,val -> val,key
"""
def reverse_key_values_in_place(iter_dict):
    return {iter_dict[key]:key for key in iter_dict}

#-------------------------BEYOND THE TASK--------------------------------------
"""
from string separated with space, create a dict which conataisn of words as a keys
and word lengh as a len(word)
"""
def transalte_string(line):
    vowels = 'aeuoi'
    return {word:sum([1 if ch.lower() in vowels else 0 for ch in word]) for word in line.split()}

"""
Create file dict from given dictionary, keys as filename and values of file length
"""
def making_file_fict(mypath='C:\Windows\Temp'):
    file_dict = {}
    entries = Path(mypath)
    # for file in entries.iterdir():
    #     if file.is_file():
    #         with open(file) as f:
    #             file_dict[file.name] =  len(f.readlines())
            # print(file)

    file_dict = {file.name:file.stat().st_size for file in entries.iterdir() if file.is_file()}
    return file_dict

"""
 Find a configuration file in which the lines look like “name=value.” Use a dict
comprehension to read from the file, turning each line into a key-value pair.
"""
def making_dict_from_file(filenane):
    with open(filenane) as f:
        return {line.split('=')[0]:line.split('=')[1] for line in f}


if __name__ == '__main__':
    # print(reverse_key_values_in_place({'a':1, 'b':2, 'c':3, 'd':4}))
    # print(transalte_string('this is an easy test is brokoli'))
    print(making_file_fict('example_data'))
