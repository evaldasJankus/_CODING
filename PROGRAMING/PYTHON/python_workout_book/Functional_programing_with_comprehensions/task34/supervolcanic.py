## IMPORTS
# from pathlib import Path

#-------------------------MAIN TASK--------------------------------------------
"""
From given word list in a file (one word per line) return a list of all
supervocalic words. Simply put, such words contain all five vowels in English
(a, e, i, o, and u), each of them appearing once and in alphabetical order.
"""
def is_supervocalic_words(word):
    vowels = ['a','e','i','o','u']
    vowels_in_word = [letter for letter in word if letter.lower() in vowels]
    return vowels_in_word == vowels
def get_sv(myfile='supervocalic_words'):
    with open(myfile) as f:
        return {word for word in f if is_supervocalic_words(word)}

#-------------------------BEYOND THE TASK--------------------------------------
"""
 In the /etc/passwd file you used earlier, what different shells (i.e., command
interpreters, named in the final field on each line) are assigned to users? Use a
set comprehension to gather them.
"""
def find_different_shells(myfile='passwd.txt'):
    return {line.split(':')[-1].strip() for line in open(myfile) if not line.startswith('#')}

"""
 Given a text file, what are the lengths of the different words? Return a set
of different word lengths in the file.
"""
def different_length_words(myfile='supervocalic_words'):
    return {len(word.strip()) for word in open(myfile)}

"""
 Create a list whose elements are strings—the names of people in your family.
Now use a set comprehension (and, better yet, a nested set comprehension) to
find which letters are used in your family members’ names.
"""
def name_list():
    names = ['Evaldas','Aiste','Laima','Albinas']
    # return {letter.lower() for name in names for letter in name}
    return {str({letter.lower() for letter in name}) for name in names}


if __name__ == '__main__':
    # print(get_sv())
    # print(find_different_shells())
    # print(different_length_words())
    print(name_list())
