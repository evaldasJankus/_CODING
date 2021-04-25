## IMPORTS
from string import ascii_lowercase
# import json

#-------------------------MAIN TASK--------------------------------------------
"""
Create dict of lower case, where key is letter and value is a value increased by
one (starting from 1)
"""
def get_letter_dict():
    # d = {}
    return {letter:indx for indx,letter in enumerate(ascii_lowercase,1)}
"""
create a fucntion which will produce a list of words which gematria score is
equal to given word. one function should be gematria_score - returns score of one
word. another function gematria_list() - returns list of words described earlier .
"""
def gematria_score(word):
    d = get_letter_dict()
    return sum([d.get(letter,0) for letter in word])
def gematria_list(base_word):
    base_score = gematria_score(base_word)
    with open('supervocalic_words') as f:
        return [word.strip() for word in f if base_score == gematria_score(word.strip())]


#-------------------------BEYOND THE TASK--------------------------------------
"""
 Create a dict whose keys are city names, and whose values are temperatures in
Fahrenheit. Now use a dict comprehension to transform this dict into a new
one, keeping the old keys but turning the values into the temperature in
degrees Celsius.
"""
def far_to_celc():
    d_far = {'Miami, Florida':77, 'Phoenix, Arizona': 75, 'Tampa, Florida':73,
            'Orlando, Florida':73, 'Houston, Texas':70, 'New Orleans, Louisiana':70,
            'San Antonio, Texas':70,'Austin, Texas':69}
    return {k:round((v-32)*(5/9)) for k,v in d_far.items()}

"""
 Create a list of tuples in which each tuple contains three elements: (1) the
author’s first and last names, (2) the book’s title, and (3) the book’s price in
U.S. dollars. Use a dict comprehension to turn this into a dict whose keys are
the book’s titles, with the values being another (sub-) dict, with keys for (a) the
author’s first name, (b) the author’s last name, and (c) the book’s price in
U.S. dollars.
"""
def tuple_list_to_dict():
    list_of_tuples = [('a b','title1',32),('c d','title2',21)]
    return {t:{a:p} for a,t,p in list_of_tuples}

"""
 Create a dict whose keys are currency names and whose values are the price of
that currency in U.S. dollars. Write a function that asks the user what currency
they use, then returns the dict from the previous exercise as before, but with its
prices converted into the requested currency.
"""
def conver_val():
    # using euros instead of USD
    d = {'lt':0.28,'us':0.83}
    value = input('Enter price and currency, to translate it to euros: ')
    return  round(int(value.strip().split()[0]) * d.get(value.strip().split()[-1]),2) if d.get(value.strip().split()[-1], 0) else 'Currency unknown'


if __name__ == '__main__':
    # print(gematria_list('EvaldasJankuszAndSomemilijon'))
    # print(far_to_celc())
    # print(tuple_list_to_dict())
    print(conver_val())
