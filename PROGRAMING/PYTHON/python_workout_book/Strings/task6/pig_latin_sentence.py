import sys
sys.path.append('..\\task5')
from pig_latin import pig_lating

def pl_sentence(sentence):
    words = sentence.split()

    #method 1
    for word in words: print(pig_lating(word), end=' ')
    else: print()

    #method 2
    for indx,word in enumerate(words):
        words[indx] = pig_lating(word)
    print(' '.join(words))

    #method 3
    # Use sentence plsit idrectly in the loop: 'for word in setence.split():'

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Take a text file, creating (and printing) a nonsensical sentence from the nth
word on each of the first 10 lines, where n is the line number.
"""
def nonsensical_setence(n):
    from random import randint, choice
    import string
    lower_letters = string.ascii_lowercase # to generate 'words'
    number_of_words = n
    number_of_lines = randint(5,15)

    #creating nonsensical_setence file
    with open('data','w') as f:
        for _ in range(number_of_lines):
            setence = []
            for _ in range(n):
                word = ''
                for _ in range(randint(2,6)):
                    word += choice(lower_letters)
                setence.append(word)
            f.write(' '.join(setence)+'\n')

    # Reading and representing file
    with open('data','r') as f:
        for indx,setence in enumerate(f):
            if indx == 10: break
            # print(setence[:-1])
            # print(setence.replace('\n', ''))
            print(setence, end='')

"""
 Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a
way that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].
"""
def reform_strings(sentences):
    #Method 1
    new_string = [[sentence.split()[x] for sentence in sentences] for x in range(len(sentences[0].split()))]
    return [' '.join(sentence) for sentence in new_string]

    #Method 2
    # new_string = []
    # for indx in range(len(sentences[0].split())):
    #     words = []
    #     for sentence in sentences:
    #         words.append(sentence.split()[indx])
    #     new_string.append(' '.join(words))
    # return new_string


if __name__ == '__main__':
    print(reform_strings(['abc def', 'jkl mno', 'stu vwx', 'asd fgh']))
    # pl_sentence('this is a test translation')
    # nonsensical_setence(5)
