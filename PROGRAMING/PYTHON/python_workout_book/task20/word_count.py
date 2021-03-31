#-------------------------MAIN TASK--------------------------------------------
"""
o write a wordcount function that mimics the wc
Unix command. The function will take a filename as input and will print four lines
of output:
1 Number of characters (including whitespace)
2 Number of words (separated by whitespace)
3 Number of lines
4 Number of unique words (case sensitive, so “NO” is different from “no”)
"""
def word_count(filename='data_file'):
    # Method 1 we wanted to store data in list and them comprehend dict
    # dict_keys = ['lines','characters', 'words','unique words']
    # counter = [0 for _ in range(len(dict_keys))]
    # counter[3] = set()
    # # dict_info = {k:0 for k in dict_keys}
    # with open(filename) as f:
    #     for line in f:
    #         counter[0] += 1
    #         counter[1] += len(line)#.strip())
    #         counter[2] += len(line.split())
    #         counter[3].update(set(line.split()))
    # dict_info = {dict_keys[x]:(counter[x] if x != 3 else len(counter[x])) for x in range(len(dict_keys))}
    # print(dict_info)

    # Method 2: Only with dict:
    dict_keys = ['characters', 'words', 'lines','unique words']
    unique_words = set()
    dict_info = {k:0 for k in dict_keys}
    with open(filename) as f:
        for line in f:
            dict_info[dict_keys[2]] += 1
            dict_info[dict_keys[0]] += len(line)#.strip())
            dict_info[dict_keys[1]] += len(line.split())
            unique_words.update(line.split())
    dict_info[dict_keys[3]] = len(unique_words)
    print(dict_info)

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Ask the user to enter the name of a text file and then (on one line, separated by
spaces) words whose frequencies should be counted in that file. Count how
many times those words appear in a dict, using the user-entered words as the
keys and the counts as the values.
"""
def count_words_from_user():
    from os import path
    values = input('Enter file name to check, and words separated by space: ').split()
    filename = values[0]
    if not path.exists(filename):
        print(f'file does not exists, word count is not valid')
        return

    # NOTE: remove lower() to get key sensitive search
    word_counter = {k.lower():0 for k in values[1:]}
    with open(filename) as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if word.lower() in word_counter: word_counter[word.lower()] += 1
    print(word_counter)

"""
 Create a dict in which the keys are the names of files on your system and the values are the sizes of those files. To calculate the size, you can use os.stat
(http://mng.bz/dyyo).
"""
# To get file list from directer:
# 1) os.listdir() - for earlier python up until 3, returs list working in python 3.8
# 2) os.scandir() - was introduced in Python 3.5 and is documented in PEP 471, returns iterator
# 3 pathlib.Path.iterdir()	Returns an iterator of all the objects in a directory including file attribute information (from pathlib import Path)
def files_size(cpath='.'):
    import os
    # Method 1: Using os.listdir()
    # NOTE: Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.
    # file_dict = {}
    # for file in os.listdir(cpath):
    #     file_dict[file] = os.stat(file).st_size
    # print(file_dict)

    # Method 2: Using os.scandir()
    # file_dict = {}
    # for file in os.scandir(cpath):
    #     file_dict[file.name] = file.stat().st_size
    # print(file_dict)

    # Method 3: Using pathlib.Path.iterdir()
    from pathlib import Path
    file_dict = {}
    for file in Path(cpath).iterdir():
        if file.is_dir(): continue
        file_dict[file.name] = file.stat().st_size
    print(file_dict)

"""
 Given a directory, read through each file and count the frequency of each letter.
(Force letters to be lowercase, and ignore nonletter characters.) Use a dict
to keep track of the letter frequencies. What are the five most common letters
across all of these files?
"""
def most_commont_letter_key_isensitive(cpath='.'):
    from pathlib import Path
    letters = {}
    for file in Path(cpath).iterdir():
        if file.name.endswith('.py'): continue
        with open(file) as f:
            for line in f:
                for ch in line:
                    if ch.isalpha(): letters[ch.lower()] = letters.get(ch.lower(),0) + 1
        print(f'file <{file.name}>. COMPLETED!')
    for letter in sorted(letters, key=lambda x: letters[x])[:-6:-1]:
        print(letter,' => ',letters[letter])


if __name__ == '__main__':
    most_commont_letter_key_isensitive()
    # files_size('C:\Windows')
    # count_words_from_user()
